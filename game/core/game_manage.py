import pygame

from core.game_world import GameWorld



class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Metroidvania TCC")

        self.clock = pygame.time.Clock()
        self.running = True
        
        self.world = GameWorld()

    def run(self):

        while self.running:

            dt = self.clock.tick(60) / 1000

            self.handle_events()
            keys = pygame.key.get_pressed()
            self.world.update(dt, keys)
            self.render()

        pygame.quit()

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):

        self.screen.fill((30, 30, 30))

        self.world.render(self.screen)

        pygame.display.flip()
