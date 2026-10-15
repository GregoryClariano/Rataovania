import pygame

from gameObject.player import Player
from core.tilemap import TileMap
from core.camera import Camera


class GameWorld:

    def __init__(self):

        self.player = Player(100, 300)
        
        self.camera = Camera(1280, 720)

        self.tile_map = TileMap()
        
        self.entities = [
            self.player
        ]

    def update(self, dt, keys):

        for entity in self.entities:
            entity.update(
                dt,
                keys,
                self.tile_map.tiles
            )
        self.camera.update(self.player)

    def render(self, screen):
        self.tile_map.draw(screen, self.camera)
        
        self.player.draw(screen)