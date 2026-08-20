# pylint: disable=import-error
import pygame

from gameObject.character import Character
from core.physics import Rigidbody

class Player(Character):

    def __init__(self, x, y):

        super().__init__(pygame.Vector2(x, y), None)

        self.rect = pygame.Rect(x, y, 50, 50)

        self.speed = 300
        self.jump_force = -500
        self.remaining_jumps = 1

        self.on_ground = False

        self.rb = Rigidbody()
        

    def update(self, dt, keys, platforms):
        moving = False
        self.rb.acceleration[0] = 0

        if keys[pygame.K_LEFT]:
            self.rb.acceleration[0] = -1000
            moving = True

        if keys[pygame.K_RIGHT]:
            self.rb.acceleration[0] = 1000
            moving = True

        if keys[pygame.K_SPACE]:
            if  self.remaining_jumps > 0 and self.on_ground:
                self.rb.velocity[1] = self.jump_force
                self.on_ground = False
                self.remaining_jumps -= 1
                    

        self.rb.apply_gravity()

        if not moving:
            self.rb.apply_friction(dt)

        self.rb.update(dt)

        self.rect.x += int(self.rb.velocity[0] * dt)


        for platform in platforms:

            if self.rect.colliderect(platform.hitbox):

                if self.rb.velocity[0] > 0:
                    self.rect.right = platform.hitbox.left

                elif self.rb.velocity[0] < 0:
                    self.rect.left = platform.hitbox.right

                self.rb.velocity[0] = 0
            
        self.rect.y += int(self.rb.velocity[1] * dt)

        self.on_ground = False  


        for platform in platforms:

            if self.rect.colliderect(platform.hitbox):

                if self.rb.velocity[1] > 0:

                    self.rect.bottom = platform.hitbox.top

                    self.on_ground = True
                    self.remaining_jumps = 1

                elif self.rb.velocity[1] < 0:

                    self.rect.top = platform.hitbox.bottom

                self.rb.velocity[1] = 0

    def draw(self, screen):

        pygame.draw.rect(screen, (255, 200, 50), self.rect)
