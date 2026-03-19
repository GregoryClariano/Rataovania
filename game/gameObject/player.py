# pylint: disable=import-error
import pygame

from core.physics import Rigidbody

class Player:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 50, 50)

        self.speed = 300
        self.jump_force = -500

        self.on_ground = False

        self.rb = Rigidbody()

    def update(self, dt, keys, ground):
        # INPUT
        moving = False
        self.rb.acceleration[0] = 0

        if keys[pygame.K_a]:
            self.rb.acceleration[0] = -1000
            moving = True

        if keys[pygame.K_d]:
            self.rb.acceleration[0] = 1000
            moving = True

        # PULO
        if keys[pygame.K_SPACE] and self.on_ground:
            self.rb.velocity[1] = self.jump_force
            self.on_ground = False

        # GRAVIDADE
        self.rb.apply_gravity()

        # ATRITO (se não estiver apertando nada)
        if not moving:
            self.rb.apply_friction(dt)

        # ATUALIZA FÍSICA
        self.rb.update(dt)

        # MOVIMENTO
        self.rect.x += int(self.rb.velocity[0] * dt)
        self.rect.y += int(self.rb.velocity[1] * dt)

        # COLISÃO
        if self.rect.colliderect(ground):

            self.rect.bottom = ground.top
            self.rb.velocity[1] = 0
            self.on_ground = True

    def draw(self, screen):

        pygame.draw.rect(screen, (255, 200, 50), self.rect)
