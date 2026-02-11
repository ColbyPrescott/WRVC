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
        self.distance = 140
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