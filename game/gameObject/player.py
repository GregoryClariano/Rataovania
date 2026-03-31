# pylint: disable=import-error
import pygame

from core.physics import Rigidbody

class Player:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 50, 50)

        self.speed = 300
        self.jump_force = -500
        self.remaining_jumps = 1

        self.on_ground = False

        self.rb = Rigidbody()
        
        self.jump_pressed_last_frame = False

    def update(self, dt, keys, platforms):
        moving = False
        self.rb.acceleration[0] = 0

        if keys[pygame.K_LEFT]:
            self.rb.acceleration[0] = -1000
            moving = True

        if keys[pygame.K_RIGHT]:
            self.rb.acceleration[0] = 1000
            moving = True

        jump_pressed = keys[pygame.K_SPACE]

        if jump_pressed and not self.jump_pressed_last_frame:
            if self.on_ground or self.remaining_jumps > 0:
                self.rb.velocity[1] = self.jump_force
                self.on_ground = False
                self.remaining_jumps -= 1

        self.jump_pressed_last_frame = jump_pressed

        self.rb.apply_gravity()

        if not moving:
            self.rb.apply_friction(dt)

        self.rb.update(dt)

        # MOVIMENTO
        self.rect.x += int(self.rb.velocity[0] * dt)

        for platform in platforms:
            if self.rect.colliderect(platform):

                if self.rb.velocity[0] > 0:
                    self.rect.right = platform.left

                elif self.rb.velocity[0] < 0:
                    self.rect.left = platform.right

                self.rb.velocity[0] = 0
            
        self.rect.y += int(self.rb.velocity[1] * dt)

        self.on_ground = False  # reset

        for platform in platforms:
            if self.rect.colliderect(platform):

                if self.rb.velocity[1] > 0:  # caindo
                    self.rect.bottom = platform.top
                    self.on_ground = True

                    self.remaining_jumps = 1
                    
                elif self.rb.velocity[1] < 0:  # subindo
                    self.rect.top = platform.bottom

                self.rb.velocity[1] = 0

    def draw(self, screen):

        pygame.draw.rect(screen, (255, 200, 50), self.rect)
