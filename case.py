from element import *

class case(element): 
    def __init__(self,grillePos,valeur,pos_x,pos_y,textureName=None):
        super().__init__(pos_x,pos_y,textureName)
        self.indices = []
        self.grillePos = grillePos
        self.grilleValeur = valeur
        self.rightClickState = False
        self.font = pygame.font.SysFont("comicsansms", 10)
    
    def ajouterIndice(self,valeur):
        if len(self.indices) < 8:
            self.indices.append(valeur)

    def render(self,screen):
        super().render(screen)
        x = self.texture_rect.x +3
        y = self.texture_rect.y -1
        i = 0
        for indice in self.indices:
            screen.blit(self.font.render(indice, True,(255,255,255)),(x,y))
            x = x + 13
            if i % 3 == 2:
                x = self.texture_rect.x +3
                y = y + 13
            if i == 3:
                x = x + 13
                i = i + 1
            i = i + 1

    def event(self,event):
        super().event(event)
        if self.clickable:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    if self.grilleValeur == ' ':
                        if self.texture_rect.collidepoint(event.pos):
                            self.clickState = False
                            if not self.rightClickState:
                                self.rightClickState = True
                            else:
                                self.rightClickState = False
                            pygame.draw.rect(self.texture,(255,255,120,255),(1,1,38,38),width=1)
        if self.rightClickState:
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in ("[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","backspace"):
                    if pygame.key.name(event.key) == "backspace":
                        if len(self.indices) > 0:
                            self.indices.pop()
                    else:
                        if pygame.key.name(event.key)[1] not in self.indices:
                            self.ajouterIndice(pygame.key.name(event.key)[1])
