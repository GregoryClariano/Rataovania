class DynamicObject:
    def __init__(self, possition, sprite):
        self.possition = pygame.Vector2(possition)
        self.sprite = sprite
        
    def update(self, dt, keys, platforms):
        pass
    
    def draw(self, screen):
        screen.blit(self.sprite, self.possition)