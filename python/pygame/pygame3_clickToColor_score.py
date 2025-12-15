import pygame
import random
pygame.init()

# Window setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click to Change Color")
DEFAULT_FONT = pygame.font.SysFont("arial", 30)

# Circle settings
x = WIDTH / 2
y = HEIGHT / 2
radius = 60
color = (0, 255, 0)
clicks = 0

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
                clicks += 1
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
    
    pygame.draw.circle(screen, color, (x, y), radius)
    text_surface = DEFAULT_FONT.render(str(clicks), True, (0, 0, 0))
    text_size = pygame.font.Font.size(DEFAULT_FONT, str(clicks))
    screen.blit(text_surface, (x - text_size[0] / 2, y - text_size[1] / 2))
    pygame.display.flip()

pygame.quit()