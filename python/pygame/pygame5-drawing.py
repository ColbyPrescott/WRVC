import pygame
pygame.init()

# Window setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Drawing App")

# Colors
color = (200, 200, 200)
radius = 5

drawing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
    
    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, (mouse_x, mouse_y), radius)
    
    pygame.display.flip()

pygame.quit()