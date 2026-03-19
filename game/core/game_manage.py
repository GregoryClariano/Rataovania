import pygame

from gameObject.player import Player


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Metroidvania TCC")

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(100, 300)

        # chão simples (x, y, largura, altura)
        self.ground = pygame.Rect(0, 500, 3000, 100)

    def run(self):

        while self.running:

            dt = self.clock.tick(60) / 1000

            self.handle_events()
            self.update(dt)
            self.render()

        pygame.quit()

    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):

        keys = pygame.key.get_pressed()
        self.player.update(dt, keys, self.ground)

    def render(self):

        self.screen.fill((30, 30, 30))

        pygame.draw.rect(self.screen, (100, 255, 100), self.ground)
        self.player.draw(self.screen)

        pygame.display.flip()
