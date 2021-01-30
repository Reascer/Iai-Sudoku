import pygame
import element as elmt
import elementManager as elmtManager
from Sudoku import Sudoku
import Layout as Lyt

class Jeu:
    def __init__(self,title,width,height):
        pygame.init() #initalisation de pygame
        self.title = title
        self.width = width
        self.height = height
        self.layoutEnCours = "titleScreen"
        self.sudoku = Sudoku(3)
        #self.sudoku.load('grille.txt')
        self.sudoku.afficher()
        #self.sudoku.save('grille.txt')  --> Faudrait demander un nom au user, puis le reafficher dans une liste ensuite

        self.running = True

        pygame.display.set_caption(title) # Mettre le titre sur Iai-sudoku <3
        self.screen = pygame.display.set_mode((1080,720)) # Resize la fenêtre

        self.font = pygame.font.SysFont("comicsansms", 48) # initialisaiton des font (c'est pour le texte)
        
        self.initRender()


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if self.layoutEnCours == "titleScreen":
                action = self.titleScreen.event(event)
                if action == 'Quitter':
                    self.quit()
                if action == 'SubMenu':                    
                    self.layoutEnCours = "SubMenu"
            if self.layoutEnCours == "SubMenu":
                action = self.subMenu.event(event)                
                if action == 'Jouer':
                    self.layoutEnCours = "Jeu"
                if action == 'Charger':
                    ok = self.sudoku.loadMenu()
                    if ok == True:
                        self.layoutEnCours = "Jeu"
            if self.layoutEnCours == "Jeu":
                action = self.jeuLayout.event(event)
                if action == 'verif':
                    self.sudoku.isFinish()
                self.sudoku.event(event)
            
    def update(self):
        pass

    def render(self):
        if self.layoutEnCours == 'Jeu':
            self.backgroundManager.renderElements(self.screen,1)
            self.jeuLayout.render(self.screen)
            self.sudoku.render(self.screen)


        if self.layoutEnCours == "titleScreen":
            self.backgroundManager.renderElements(self.screen,0)
            self.titleScreen.render(self.screen)

        if self.layoutEnCours == "SubMenu":
            self.backgroundManager.renderElements(self.screen,0)
            self.subMenu.render(self.screen)


        pygame.display.flip()
    
    def quit(self):
        self.running = False
        pygame.quit()
        print("end of game")
    
    #Ajouter les elements dans l'initRender
    
    def initRender(self):
        self.backgroundManager = elmtManager.elementManager()
        textManager = elmtManager.elementManager()
        buttonManager = elmtManager.elementManager()
        buttonManagerSub = elmtManager.elementManager()
        buttonManagerJeu = elmtManager.elementManager()

        #====================== element a ajouter ===========================
        
        titleBackground = elmt.element(0,0,"sakuraBackground.jpg")
        titleBackground.texture = pygame.transform.scale(titleBackground.texture,(1080,720))
        self.backgroundManager.addElement(titleBackground)

        jeuBackground = elmt.element(0,0,"sakuraBackground2.jpg")
        jeuBackground.texture = pygame.transform.scale(jeuBackground.texture,(1080,720))
        self.backgroundManager.addElement(jeuBackground)

        Menutitle = elmt.element(100,100)
        Menutitle.setTexture(self.font.render('Iai-sudoku', True,(0,0,0))) # pour les parametres: le text , je sais plus mais true du coup , la couleur du text en RGB
        textManager.elements.append(Menutitle)
        
        #====================== Bouttons Home Screen ===========================
        
        buttonPlay = elmt.element(255,400,"button.png")
        buttonPlay.setText(self.font.render('Play', True,(0,0,0)))
        buttonPlay.clickable = True
        buttonPlay.action = "SubMenu"
        buttonManager.addElement(buttonPlay)

        buttonQuitter = elmt.element(600,400,"button.png")
        buttonQuitter.setText(self.font.render('Quitter', True,(0,0,0)))
        buttonQuitter.clickable = True
        buttonQuitter.action = "Quitter"
        buttonManager.addElement(buttonQuitter)
        
        #====================== Bouttons Sous Menu ===========================
        
        buttonNew = elmt.element(250,200,"button.png")
        buttonNew.setText(self.font.render('Nouveau', True,(0,0,0)))
        buttonNew.clickable = True
        buttonNew.action = "Jouer"
        buttonManagerSub.addElement(buttonNew)

        buttonLoad = elmt.element(650,200,"button.png")
        buttonLoad.setText(self.font.render('Charger', True,(0,0,0)))
        buttonLoad.clickable = True
        buttonLoad.action = "Charger"
        buttonManagerSub.addElement(buttonLoad)

        #====================== Bouttons Jeu ===========================

        buttonVerif = elmt.element(250,200,"buttonRect.png")
        buttonVerif.setText(self.font.render('verfier', True,(0,0,0)))
        buttonVerif.clickable = True
        buttonVerif.action = "verif"
        buttonManagerJeu.addElement(buttonVerif)

        #====================== Initialisation des Layouts ===========================

        self.titleScreen = Lyt.Layout()
        self.titleScreen.addElmtManager(buttonManager)
        self.titleScreen.addElmtManager(textManager)

        self.subMenu = Lyt.Layout()
        self.subMenu.addElmtManager(buttonManagerSub)

        self.jeuLayout = Lyt.Layout()
        self.jeuLayout.addElmtManager(buttonManagerJeu)

        
        
