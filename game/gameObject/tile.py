from gameObject.static_objects import StaticObject

class Tile(StaticObject):
    def __init__(self, position, sprite, hitbox, solid = True):
        super().__init__(
            position,
            sprite,
            hitbox
        )
        
        self.solid = solid