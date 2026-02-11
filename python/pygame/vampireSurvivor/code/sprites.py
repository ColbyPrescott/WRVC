from settings import *
from math import atan2, degrees

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surf, pos, direction, groups):
        super().__init__(groups)

        angle = degrees(atan2(-direction.y, direction.x))
        self.image = pygame.transform.rotate(surf, angle)
        self.rect = self.image.get_frect(center = pos)
        
        self.direction = direction.normalize()
        self.speed = 1000

        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000
    
    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.move(dt)

        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        # Player connections
        self.player = player
        self.distance = 100
        self.player_direction = pygame.Vector2(1, 0)

        # Sprite setup
        super().__init__(groups)
        self.gun_surf = pygame.image.load(join("images", "gun", "gun.png")).convert_alpha()
        self.image = self.gun_surf
        self.rect = self.image.get_frect(center = self.player.rect.center + self.player_direction * self.distance)
    
    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        offset = mouse_pos - player_pos
        if offset:
            self.player_direction = offset.normalize()
    
    def rotate_gun(self):
        angle = degrees(atan2(-self.player_direction.y, self.player_direction.x))
        new_surf = self.gun_surf
        new_surf = pygame.transform.flip(new_surf, False, self.player_direction.x < 0)
        new_surf = pygame.transform.rotozoom(new_surf, angle, 1)
        self.image = new_surf
    
    def shoot(self, groups):
        speed = 100
        bullet = Bullet(self.rect.topright, self.player_direction * speed, groups)

    def update(self, _):
        self.get_direction()
        self.rotate_gun()
        self.rect.center = self.player.rect.center + self.player_direction * self.distance

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, player, collision_sprites):
        super().__init__(groups)
        self.player = player

        # Image
        self.frames, self.frames_index = frames, 0
        self.image = self.frames[self.frames_index]
        self.animation_speed = 6

        # Rect
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-20, -40)
        self.collision_sprites = collision_sprites
        self.direction = pygame.Vector2()
        self.speed = 350

        self.death_time = 0
        self.death_duration = 100

    def animate(self, dt):
        self.frames_index += self.animation_speed * dt
        self.image = self.frames[int(self.frames_index) % len(self.frames)]
    
    def move(self, dt):
        # Get direction
        player_pos = pygame.Vector2(self.player.rect.center)
        enemy_pos = pygame.Vector2(self.rect.center)
        self.direction = player_pos - enemy_pos
        if self.direction:
            self.direction.normalize_ip()

        # Update rect position and do collision
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collisions("horizontal")
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collisions("vertical")
        self.rect.center = self.hitbox_rect.center
    
    def collisions(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == "horizontal":
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                if direction == "vertical":
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top

    def destroy(self):
        # Start timer
        self.death_time = pygame.time.get_ticks()
        # Change the image
        surf = pygame.mask.from_surface(self.frames[0]).to_surface()
        surf.set_colorkey("black")
        self.image = surf
    
    def death_timer(self):
        if pygame.time.get_ticks() - self.death_time >= self.death_duration:
            self.kill()

    def update(self, dt):
        if self.death_time != 0:
            self.death_timer()
            return
        
        self.move(dt)
        self.animate(dt)

