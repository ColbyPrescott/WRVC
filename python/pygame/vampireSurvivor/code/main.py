from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from groups import AllSprites

from random import randint, choice

class Game:
    def __init__(self):
        # Setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivor")
        self.clock = pygame.time.Clock()
        self.running = True

        self.difficulty = 1

        # Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        # Gun
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 200

        # Enemy spawn timer
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, 200, 1)
        self.spawn_positions = []

        # Audio
        self.music = pygame.mixer.Sound(join("audio", "music.wav"))
        self.music.set_volume(0.7)
        self.music.play(loops = -1)
        self.shoot_sound = pygame.mixer.Sound(join("audio", "shoot.wav"))
        self.shoot_sound.set_volume(0.3)
        self.impact_sound = pygame.mixer.Sound(join("audio", "impact.ogg"))
        self.game_over_sound = pygame.mixer.Sound(join("audio", "gameOver.mp3"))

        # World setup
        self.load_images()
        self.setup()
    
    def load_images(self):
        self.bullet_surf = pygame.image.load(join("images", "gun", "bullet.png")).convert_alpha()

        folders = list(walk(join("images", "enemies")))[0][1]
        self.enemy_frames = {}
        for folder in folders:
            for folder_path, _, file_names in walk(join("images", "enemies", folder)):
                self.enemy_frames[folder] = []
                for file_name in sorted(file_names, key=lambda name: int(name.split(".")[0])):
                    full_path = join(folder_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames[folder].append(surf)

    def setup(self):
        map = load_pygame(join("data", "maps", "world.tmx"))

        for x, y, image in map.get_layer_by_name("Ground").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name("Objects"):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name("Collisions"):
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        for obj in map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
                self.gun = Gun(self.player, self.all_sprites)
            elif obj.name == "Enemy":
                self.spawn_positions.append((obj.x, obj.y))

    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            pos = self.gun.rect.center + self.gun.player_direction * 30
            Bullet(self.bullet_surf, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.shoot_sound.play()
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def gun_timer(self):
        self.gun_cooldown = (1 - 0.75 * self.difficulty) * 300
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_cooldown:
                self.can_shoot = True
    
    def bullet_collision(self):
        for bullet in self.bullet_sprites:
            collision_sprites = pygame.sprite.spritecollide(bullet, self.enemy_sprites, False)
            kill_bullet = False
            for sprite in collision_sprites:
                if sprite.death_time == 0:
                    sprite.destroy()
                    kill_bullet = True
            if kill_bullet:
                bullet.kill()
                self.impact_sound.play()
    
    def player_collision(self):
        collision_sprites = pygame.sprite.spritecollide(self.player, self.enemy_sprites, False, pygame.sprite.collide_mask)
        for collision_sprite in collision_sprites:
            if collision_sprite.death_time == 0:
                self.end_game()
                return
    
    def end_game(self):
        self.game_over_sound.play()
        self.music.stop()
        pygame.time.wait(1000)
        self.running = False

    def run(self):
        while self.running:
            # Delta time
            dt = self.clock.tick() / 1000

            self.difficulty = 1 - 1 / (0.01 * pygame.time.get_ticks() / 1000 + 1)

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.enemy_event:
                    delay = int(max(2, (1 - self.difficulty) * 200))
                    pygame.time.set_timer(self.enemy_event, delay, 1)
                    for i in range(3):
                        pos = choice(self.spawn_positions)
                        if abs(pos[0] - self.player.rect.centerx) < WINDOW_WIDTH / 2 or abs(pos[1] - self.player.rect.centery) < WINDOW_HEIGHT / 2:
                            continue
                        Enemy(pos, choice(list(self.enemy_frames.values())), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites)
                        break
            
            # Update
            self.gun_timer()
            self.input()
            self.all_sprites.update(dt)
            self.bullet_collision()
            self.player_collision()

            # Draw
            self.display_surface.fill("black")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()