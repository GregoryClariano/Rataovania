from gameObject.tile import Tile


class TileMap:

    def __init__(self, tile_size=32):

        self.tile_size = tile_size

        self.tiles = []

        self.create_map()

    def create_map(self):

        map_data = [
            "..........",
            "..........",
            "...###....",
            "..........",
            "##########"
        ]

        for row, line in enumerate(map_data):

            for column, value in enumerate(line):

                if value == "#":

                    x = column * self.tile_size
                    y = row * self.tile_size

                    tile = Tile(
                        x,
                        y,
                        self.tile_size
                    )

                    self.tiles.append(tile)

    def draw(self, screen):

        for tile in self.tiles:
            tile.draw(screen)
