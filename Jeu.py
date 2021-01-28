import pygame
import element as elmt
from Sudoku import Sudoku


class Jeu:
    def __init__(self,title,width,height):
        self.title = title
        self.width = width
        self.height = height

        self.sudoku = Sudoku(3)

        self.running = True

        pygame.init() #initalisation
        pygame.display.set_caption(title) # Mettre le titre sur Iai-sudoku <3
        self.screen = pygame.display.set_mode((1080,720)) # Resize la fenêtre
        self.sysfont = pygame.font.get_default_font() # initialisaiton des font (c'est pour le texte)
        self.background = pygame.image.load('ressources/sakuraBackground.jpg')

        self.font = pygame.font.SysFont(self.sysfont, 72)
        self.img = self.font.render('Iai-sudoku', True,(0,0,0))

        self.buttonPlay = elmt.element(100,400,"button.png")

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                self.quit()
                print("end of game")

    def update(self):
        pass

    def render(self):

        
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.img, (100, 100))
        self.buttonPlay.render(self.screen)

        pygame.display.flip()
    
    def quit(self):
        pygame.display.quit()
        pygame.quit()
    
    def init(self):




