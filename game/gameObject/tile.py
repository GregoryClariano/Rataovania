from static_objects import StaticObject


class tile(StaticObject):
    def __init__(self, position, sprite, hitbox, solid = True):
        super().__init__(
            position,
            sprite,
            hitbox
        )
        
        self.solid = solid