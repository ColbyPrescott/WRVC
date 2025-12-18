# My own idea, try combining the drawing and snowflake exercises

import pygame
import math
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Snowflake")

# Colors
BACKGROUND = (20, 20, 40)
SNOW = (240, 240, 255)

# Brush
brush_radius = 5
spokes = 6
mirror_spokes = True


# Draw a dot on the screen, mirroring and rotating as needed
def transform_draw_point(point, mirror, angle, color):
    point = pygame.math.Vector2(point)
    point -= (WIDTH / 2, HEIGHT / 2)
    if mirror:
        point.x *= -1
    point = point.rotate_rad(angle)
    point += (WIDTH / 2, HEIGHT / 2)
    pygame.draw.circle(screen, color, point, brush_radius)

# Draw a dot on the screen, duplicating and transforming it with a "snowflake transformation"
def draw_snowflake_point(point, color):
    for i in range(spokes):
            transform_draw_point(mouse_pos, False, i * 2*math.pi / spokes, color)
            if mirror_spokes:
                transform_draw_point(mouse_pos, True, i * 2*math.pi / spokes, color)

# Init
print("Left mouse: Draw")
print("Right mouse: Erase")
print("Space: Clear")
screen.fill(BACKGROUND)

# Draw loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Clear
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.fill(BACKGROUND)
    
    # Draw
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        draw_snowflake_point(mouse_pos, SNOW)
    # Erase
    elif pygame.mouse.get_pressed()[2]:
        mouse_pos = pygame.mouse.get_pos()
        draw_snowflake_point(mouse_pos, BACKGROUND)
        
    pygame.display.flip()
    # clock.tick(200) # Comment out for smoother lines

pygame.quit()