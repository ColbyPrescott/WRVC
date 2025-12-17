import pygame
import math
pygame.init()

# Window setup
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Snowflake")

# Colors
WHITE = (240, 240, 255)
BACKGROUND = (20, 20, 40)

clock = pygame.time.Clock()

angle = 0
time = 0
spokes = 6

def draw_snowflake(cx, cy, radius, rotation):
    for i in range(spokes):
        a = rotation + i * (math.pi / (spokes / 2))

        # Main arm
        x = cx + radius * math.cos(a)
        y = cy + radius * math.sin(a)
        pygame.draw.line(screen, WHITE, (cx, cy), (x, y), 3)

        # Branches
        bx = cx + radius * 0.65 * math.cos(a)
        by = cy + radius * 0.65 * math.sin(a)

        left = a + math.pi / spokes
        right = a - math.pi / spokes

        pygame.draw.line(
            screen, WHITE,
            (bx, by),
            (bx + 25 * math.cos(left), by + 25 * math.sin(left)),
            2
        )
        pygame.draw.line(
            screen, WHITE,
            (bx, by),
            (bx + 25 * math.cos(right), by + 25 * math.sin(right)),
            2
        )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BACKGROUND)

    # Animation math
    time += 1
    angle += 0.01
    pulse = 90 + 8 * math.sin(time * 0.05)

    draw_snowflake(WIDTH // 2, HEIGHT // 2, pulse, angle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()