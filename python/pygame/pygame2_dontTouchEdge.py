import pygame
pygame.init()

# Window setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Touch the Edge!")

# Player settings
x = 400
y = 300
speed = 0.5
size = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    # Bounds
    if x < 0 or x + size > WIDTH or y < 0 or y + size > HEIGHT:
        print("!!! GAME OVER !!!")
        print("You found the edge")
        running = False
    
    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (0, 200, 255), (x, y, size, size))
    pygame.display.flip()

pygame.quit()