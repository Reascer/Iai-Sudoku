import pygame

class element:
    def __init__(self,pos_x,pos_y,textureName=None):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.clickable = False
        self.text = None
        self.action = None

        if textureName is not None:
            self.texture = pygame.image.load("ressources/" + textureName)
            self.texture_rect = self.texture.get_rect()
            self.texture_rect.x = self.pos_x
            self.texture_rect.y = self.pos_y
            #print("w:"+str(self.size_w)+"h:"+str(self.size_h))
    
    def eventElmt(self,event):
        if self.clickable == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0] == True:
                    if self.texture_rect.collidepoint(event.pos):
                        mouse_pos = (event.pos[0] - self.pos_x , event.pos[1] - self.pos_y)
                        if not self.texture.get_at(mouse_pos)[3] == 0:
                            print("click !")
                            return self.action
            

    def render(self,screen):
        screen.blit(self.texture, (self.pos_x, self.pos_y))
        if self.text is not None:
            self.renderTextCenter(screen)
            

    def setPosition(self,pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    def setTexture(self,texture):
        self.texture = texture
        self.texture_rect = self.texture.get_rect()
        self.texture_rect.x = self.pos_x
        self.texture_rect.y = self.pos_y
    
    def setText(self,text):
        self.text = text

    def renderTextCenter(self,screen):
        screen.blit(self.text, (self.pos_x + self.texture_rect.w/2 - self.text.get_width()/2, self.pos_y + self.texture_rect.h/2 - self.text.get_height()/2))