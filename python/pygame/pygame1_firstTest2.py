import pygame
pygame.init()

def lerp(a, b, t):
    return a + (b - a) * t

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the Box")
clock = pygame.time.Clock()

# Player stuffz
x = 400
y = 300
speed = 0.02

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # x -= speed
        x = lerp(x, 1, speed)
    if keys[pygame.K_RIGHT]:
        # x += speed
        x = lerp(x, 800 - 50 - 1, speed)
    if keys[pygame.K_UP]:
        # y -= speed
        y = lerp(y, 1, speed)
    if keys[pygame.K_DOWN]:
        # y += speed
        y = lerp(y, 600 - 50 - 1, speed)
    
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()