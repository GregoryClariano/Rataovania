from gameObject.dynamic_object import DynamicObject

class Character(DynamicObject):
    def __init__(self, possition, sprite):
        super().__init__(possition, sprite)
