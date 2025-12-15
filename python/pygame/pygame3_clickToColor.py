import pygame
import random
pygame.init()

# Window setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click to Change Color")

# Circle settings
x = WIDTH / 2
y = HEIGHT / 2
radius = 60
color = (0, 255, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click detection
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dist = ((mouse_x - x) ** 2 + (mouse_y - y) ** 2) ** 0.5
            if dist < radius:
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
    
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()

pygame.quit()