import pygame
import random
pygame.init()

# Window setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Falling Block")
FONT = pygame.font.SysFont("Arial", 30)

# Player
player_size = 10
player_x = WIDTH / 2
player_y = HEIGHT / 2
player_speed = 300

blocks = []

def end_game():
    global running
    if not running:
        return
    running = False
    print("!!! GAME OVER !!!")
    print("You were obliterated by the evil block of blockiness.")
    print("Final time: ", pygame.time.get_ticks() / 1000)

def spawn_block():
    blocks.append(Block())

class Block:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = random.randint(30, 60)
        self.speed_x = 0
        self.speed_y = 0
        self.color = (
            random.randint(150, 255), 
            0, 
            0
        )

        direction = random.randint(0, 3)
        speed = random.randint(100, 200)
        if direction == 0: # Top
            self.x = random.randint(0, WIDTH - self.size)
            self.y = -self.size
            self.speed_y = speed
        elif direction == 1: # Bottom
            self.x = random.randint(0, WIDTH - self.size)
            self.y = HEIGHT
            self.speed_y = -speed
        elif direction == 2: # Left
            self.x = -self.size
            self.y = random.randint(0, HEIGHT - self.size)
            self.speed_x = speed
        else: # Right
            self.x = WIDTH
            self.y = random.randint(0, HEIGHT - self.size)
            self.speed_x = -speed

    def destroy(self):
        spawn_block()
        blocks.remove(self)
    
    def tick(self):
        self.x += self.speed_x * delta_time
        self.y += self.speed_y * delta_time

        if (
            self.x > WIDTH + 5 or
            self.x + self.size < -5 or
            self.y > HEIGHT + 5 or
            self.y + self.size < -5 
        ):
            self.destroy()
        
        if (
            player_x + player_size > self.x and
            player_x < self.x + self.size and
            player_y + player_size > self.y and
            player_y < self.y + self.size
        ):
            end_game()
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Start game with one block
blocks.append(Block())

running = True
clock = pygame.time.Clock()
delta_time = 60 / 1000
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed * delta_time
    if keys[pygame.K_RIGHT]:
        player_x += player_speed * delta_time
    if keys[pygame.K_UP]:
        player_y -= player_speed * delta_time
    if keys[pygame.K_DOWN]:
        player_y += player_speed * delta_time
    
    # Bound player inside window
    if player_x < 0:
        player_x = 0
    if player_x + player_size > WIDTH:
        player_x = WIDTH - player_size
    if player_y < 0:
        player_y = 0
    if player_y + player_size > HEIGHT:
        player_y = HEIGHT - player_size
    
    # Player and background
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_size, player_size))

    if random.random() < 0.3 * delta_time:
        spawn_block()

    # Tick and draw all blocks
    for block in reversed(blocks):
        block.tick()
        block.draw()
    
    # Draw timer
    timer_surface = FONT.render(str(pygame.time.get_ticks() // 100 / 10), True, (255, 255, 255))
    screen.blit(timer_surface, (10, 10))
    
    # Finish frame
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000

    # Delay when the player loses, so they can see how they lost
    if not running:
        pygame.time.wait(400)

pygame.quit()