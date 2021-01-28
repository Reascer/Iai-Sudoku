import pygame
import element as elmt
import elementManager as elmtManager
from Sudoku import Sudoku


class Jeu:
    def __init__(self,title,width,height):
        self.title = title
        self.width = width
        self.height = height

        self.sudoku = Sudoku(3)

        self.running = True

        pygame.init() #initalisation de pygame

        pygame.display.set_caption(title) # Mettre le titre sur Iai-sudoku <3
        self.screen = pygame.display.set_mode((1080,720)) # Resize la fenêtre

        self.sysfont = pygame.font.get_default_font() # initialisaiton des font (c'est pour le texte)
        self.font = pygame.font.SysFont(self.sysfont, 72)
        
        self.initRender()


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                self.quit()
                print("end of game")

    def update(self):
        pass

    def render(self):
        self.backgroundManager.renderElements(self.screen)
        self.textManager.renderElements(self.screen)
        self.buttonManager.renderElements(self.screen)

        pygame.display.flip()
    
    def quit(self):
        pygame.display.quit()
        pygame.quit()
    
    #Ajouter les elements dans l'initRender
    def initRender(self):
        self.backgroundManager = elmtManager.elementManager()
        self.textManager = elmtManager.elementManager()
        self.buttonManager = elmtManager.elementManager()
        #====================== element a ajouter ===========================
        self.backgroundManager.addElement(0,0,'sakuraBackground.jpg')

        self.Menutitle = elmt.element(100,100)
        self.Menutitle.setTexture(self.font.render('Iai-sudoku', True,(0,0,0))) # pour les parametres: le text , je sais plus mais true du coup , la couleur du text en RGB
        
        self.textManager.elements.append(self.Menutitle)

        self.buttonManager.addElement(100,400,"button.png")

        #=====================================================================



