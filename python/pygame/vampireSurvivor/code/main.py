from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivor")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # Delta time
            dt = self.clock.tick()

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Update

            # Draw
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()