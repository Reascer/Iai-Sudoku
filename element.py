import pygame

class element:
    def __init__(self,pos_x,pos_y,texture=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
        self.texture = pygame.image.load("ressources/" + texture)
    
    def render(self,screen):
        screen.blit(self.texture, (self.pos_x, self.pos_y))

    def setPosition(self,pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def setTexture(self,texture):
        self.texture = texture
    
