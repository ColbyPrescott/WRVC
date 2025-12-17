import pygame
import random
pygame.init()

# Window setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Falling Block")

# Player
player_size = 50
player_x = WIDTH / 2
player_y = HEIGHT - player_size
player_speed = 500

# Block
block_size = 50
block_x = random.randint(0, WIDTH - block_size)
block_y = 0 - block_size
block_speed = 500

running = True
clock = pygame.time.Clock()
delta_time = 60 / 1000
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed * delta_time
    if keys[pygame.K_RIGHT] and player_x + player_size < WIDTH:
        player_x += player_speed * delta_time
    
    # Block movement
    block_y += block_speed * delta_time
    if block_y > HEIGHT:
        block_y = -block_size
        block_x = random.randint(0, WIDTH - block_size)

    # Collision
    if (
        player_x + player_size > block_x and
        player_x < block_x + block_size and
        player_y + player_size > block_y and
        player_y < block_y + block_size
    ):
        print("!!! GAME OVER !!!")
        print("You got squished into a very slim pancake. Use your newfound powers for good, never for evil.")
        running = False
    
    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, (255, 0, 0), (block_x, block_y, block_size, block_size))
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000

    if not running:
        pygame.time.wait(400)

pygame.quit()