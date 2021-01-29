import pygame
import element as elmt
import elementManager as elmtManager
from Sudoku import Sudoku


class Jeu:
    def __init__(self,title,width,height):
        pygame.init() #initalisation de pygame
        self.title = title
        self.width = width
        self.height = height
        self.layoutEnCours = "titleScreen"
        self.sudoku = Sudoku(3)
        self.sudoku.load('grille.txt')
        self.sudoku.afficher()
        #self.sudoku.save('grille.txt')  --> Faudrait demander un nom au user, puis le reafficher dans une liste ensuite

        self.running = True

        pygame.display.set_caption(title) # Mettre le titre sur Iai-sudoku <3
        self.screen = pygame.display.set_mode((1080,720)) # Resize la fenêtre

        self.font = pygame.font.SysFont("comicsansms", 72) # initialisaiton des font (c'est pour le texte)
        
        self.initRender()


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            action = self.buttonManager.EventElements(event)
            if action == 'quitter':
                self.quit()
                

    def update(self):
        pass

    def render(self):
        self.backgroundManager.renderElements(self.screen)
        self.textManager.renderElements(self.screen)
        self.buttonManager.renderElements(self.screen)
        self.sudoku.render(self.screen)

        pygame.display.flip()
    
    def quit(self):
        self.running = False
        pygame.quit()
        print("end of game")
    
    #Ajouter les elements dans l'initRender
    def initRender(self):
        self.backgroundManager = elmtManager.elementManager()
        self.textManager = elmtManager.elementManager()
        self.buttonManager = elmtManager.elementManager()

        #====================== element a ajouter ===========================
        titleBackground = elmt.element(0,0,"sakuraBackground.jpg")
        titleBackground.texture = pygame.transform.scale(titleBackground.texture,(1080,720))
        self.backgroundManager.addElement(titleBackground)

        Menutitle = elmt.element(100,100)
        Menutitle.setTexture(self.font.render('Iai-sudoku', True,(0,0,0))) # pour les parametres: le text , je sais plus mais true du coup , la couleur du text en RGB
        self.textManager.elements.append(Menutitle)

        buttonPlay = elmt.element(100,400,"button.png")
        buttonPlay.setText(self.font.render('Play', True,(0,0,0)))
        buttonPlay.clickable = True
        buttonPlay.action = "Menu"
        self.buttonManager.addElement(buttonPlay)

        buttonQuitter = elmt.element(500,400,"button.png")
        buttonQuitter.setText(self.font.render('Quitter', True,(0,0,0)))
        buttonQuitter.clickable = True
        buttonQuitter.action = "quitter"
        self.buttonManager.addElement(buttonQuitter)

        #=====================================================================



