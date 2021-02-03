import pygame

#====================== Class Element - Conteneur d'élément type de l'application ===========================#
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
class element:
    def __init__(self,pos_x,pos_y,textureName=None):
        self.alphaClickable = True
        self.clickable = False
        self.text = None
        self.action = None
        self.clickState = False
        self.clickStateToggle = False
        self.hoverable = False
        self.hovered = False
        self.click = False
        self.texture_rect = pygame.Rect(pos_x,pos_y,0,0)
        self.texture = None
        self.centerText = True
        if textureName is not None:
            self.texture = pygame.image.load(resource_path("ressources/" + textureName))
            self.texture_rect = self.texture.get_rect()
            self.texture_rect.x = pos_x
            self.texture_rect.y = pos_y
    
#====================== Liste des event possibles sur les éléments constituant une Layout ===========================#

    def event(self,event):
        if self.clickable:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
            if self.click == True:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.texture_rect.collidepoint(event.pos):
                            mouse_pos = (event.pos[0] - self.texture_rect.x , event.pos[1] - self.texture_rect.y)
                            if not self.texture.get_at(mouse_pos)[3] == 0 or not self.alphaClickable:
                                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                                if self.clickStateToggle:
                                    if not self.clickState:
                                        self.clickState = True
                                    else:
                                        self.clickState = False
                                else:
                                    self.clickState = True
                                self.click = False
                                return self.action
        if self.hoverable:
            if self.texture_rect.collidepoint(pygame.mouse.get_pos()):
                mouse_pos = (pygame.mouse.get_pos()[0] - self.texture_rect.x , pygame.mouse.get_pos()[1] - self.texture_rect.y)
                if self.alphaClickable:
                    if not self.texture.get_at(mouse_pos)[3] == 0:
                        self.text.fill((255,255,0),rect=None, special_flags=pygame.BLEND_RGB_ADD)
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        self.text.fill((255,255,0),rect=None, special_flags=pygame.BLEND_RGB_SUB)
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                else:
                    if self.texture.get_at(mouse_pos)[3] == 0:
                        self.text.fill((255,255,0),rect=None, special_flags=pygame.BLEND_RGB_ADD)
                    else:
                        self.text.fill((255,255,0),rect=None, special_flags=pygame.BLEND_RGB_SUB)
            else:
                self.text.fill((255,255,0),rect=None, special_flags=pygame.BLEND_RGB_SUB)

            if self.clickStateToggle:
                if self.clickState:
                    self.text.fill((255,255,0),rect=None, special_flags=pygame.BLEND_RGB_ADD)
                
#====================== Affichage d'un element ===========================#

    def render(self,screen):
        if self.texture is not None:
            screen.blit(self.texture, (self.texture_rect.x, self.texture_rect.y))
        if self.text is not None:
            if self.centerText:
                self.renderTextCenter(screen)
            else:
                screen.blit(self.text, (self.texture_rect.x, self.texture_rect.y))
            
#====================== Positionement d'un élément dans son Layout ===========================#

    def setPosition(self,pos_x,pos_y):
        self.texture_rect.x = pos_x
        self.texture_rect.y = pos_y
    
#====================== Définition de la texture d'un élément ===========================#

    def setTexture(self,texture):
        self.texture = texture
        self.texture_rect.w = self.texture.get_rect().w
        self.texture_rect.h = self.texture.get_rect().h
    
#====================== Définition du texte contenu dans un élément ===========================#

    def setText(self,text):
        self.text = text

#====================== Centrage du texte dans son élément ===========================#

    def renderTextCenter(self,screen):
        screen.blit(self.text, (self.texture_rect.x + self.texture_rect.w/2 - self.text.get_width()/2, self.texture_rect.y + self.texture_rect.h/2 - self.text.get_height()/2))
        