from gameObject.static_objects import StaticObject


class Platform(StaticObject):

    def __init__(self, position, sprite, hitbox):

        super().__init__(
            position,
            sprite,
            hitbox
        )
