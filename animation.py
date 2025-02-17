import pygame

#classe pour animer un sprite
class AnimateSprite(pygame.sprite.Sprite):
        
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f"assets/{sprite_name}/{sprite_name}1.png")
            