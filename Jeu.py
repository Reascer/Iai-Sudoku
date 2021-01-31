import pygame
import element as elmt
import elementManager as elmtManager
from Sudoku import Sudoku
import Layout as Lyt
from random import randint

class Jeu:
    def __init__(self,title,width,height):
        pygame.init() #initalisation de pygame
        self.title = title
        self.width = width
        self.height = height
        self.layoutEnCours = "titleScreen"
        self.sudoku = Sudoku(3)
        self.sudoku.afficher()
        self.heure = 0
        self.minute = 0
        self.seconde = 0
        self.running = True
        self.timer = False
        self.Pause = False
        
        self.sakuraDelay = 0

        pygame.display.set_caption(title) # Mettre le titre sur Iai-sudoku <3
        self.screen = pygame.display.set_mode((1080,720)) # Resize la fenêtre

        self.font = pygame.font.SysFont("comicsansms", 30) # initialisaiton des font (c'est pour le texte)
        
        self.initRender()


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                return True
            if self.layoutEnCours == "titleScreen":
                action = self.titleScreen.event(event)
                if action == 'Quitter':
                    self.quit()
                    return True
                if action == 'SubMenu':                    
                    self.layoutEnCours = "SubMenu"
            if self.layoutEnCours == "SubMenu":
                action = self.subMenu.event(event)                
                if action == 'Jouer':
                    self.layoutEnCours = "Jeu"
                if action == 'Charger':
                    ok = self.sudoku.loadMenu()
                    if ok == True:
                        self.heure = int(self.sudoku.stringCompteur[0:2])
                        self.minute = int(self.sudoku.stringCompteur[3:5])
                        self.seconde = int(self.sudoku.stringCompteur[6:8])
                        self.jeuLayout.listElmtManager[1].elements[0].setText(self.font.render(self.sudoku.stringCompteur, True,(0,0,0)))
                        self.layoutEnCours = "Jeu"
            if self.layoutEnCours == "Jeu":
                if not self.timer:
                    pygame.time.set_timer( pygame.USEREVENT + 1,1000)
                    self.timer = True
                action = self.jeuLayout.event(event)
                if action == 'Sauvegarder':
                    self.sudoku.save()
                if action == 'Verif':
                    self.sudoku.isFinish()
                if action == 'Pause':
                    if self.Pause == False:
                        self.Pause = True
                    else:
                        self.Pause = False
                self.sudoku.event(event)
                if event.type ==  pygame.USEREVENT + 1:
                    if not self.Pause:
                        self.seconde = self.seconde + 1
                        if self.seconde == 60:
                            self.seconde = 0
                            self.minute = self.minute + 1
                            if self.minute == 60:
                                self.minute = 0
                                self.heure = self.heure + 1
                        if self.seconde < 10:
                            stringCompteur = '0'+str(self.seconde)
                        else:
                            stringCompteur = str(self.seconde)

                        if self.minute < 10:
                            stringCompteur = '0'+ str(self.minute)+':'+ stringCompteur
                        else:
                            stringCompteur = str(self.minute)+':'+ stringCompteur

                        if self.heure < 10:
                            stringCompteur = '0'+str(self.heure)+':'+ stringCompteur
                        else:
                            stringCompteur = str(self.heure)+':'+ stringCompteur
                        self.sudoku.stringCompteur = stringCompteur
                        self.jeuLayout.listElmtManager[1].elements[0].setText(self.font.render(stringCompteur, True,(0,0,0)))

            
    def update(self):
        
        for petal in self.sakuraPetalManager.elements:
            if self.sakuraDelay < petal.action[2]:
                pass
            else:
                petal.texture_rect.x = petal.texture_rect.x + petal.action[0]
                petal.texture_rect.y = petal.texture_rect.y + petal.action[1]
                if petal.texture_rect.y > 720:
                    petal.texture_rect.y = -50
                    petal.texture_rect.x = randint(-500,1000)
        if self.sakuraDelay <= 600:
            self.sakuraDelay = self.sakuraDelay + 1
            

    def render(self):
        if self.layoutEnCours == 'Jeu':
            self.backgroundManager.renderElements(self.screen,1)
            self.sakuraPetalManager.renderElements(self.screen)
            self.jeuLayout.render(self.screen)
            self.sudoku.render(self.screen)


        if self.layoutEnCours == "titleScreen":
            self.backgroundManager.renderElements(self.screen,0)
            self.sakuraPetalManager.renderElements(self.screen)
            self.titleScreen.render(self.screen)

        if self.layoutEnCours == "SubMenu":
            self.backgroundManager.renderElements(self.screen,0)
            self.sakuraPetalManager.renderElements(self.screen)
            self.subMenu.render(self.screen)


        pygame.display.flip()
    
    def quit(self):
        self.running = False
        pygame.quit()
        print("end of game")
    
    #Ajouter les elements dans l'initRender
    
    def initRender(self):
        self.backgroundManager = elmtManager.elementManager()
        self.sakuraPetalManager = elmtManager.elementManager()
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
        
        for i in range(50):
            petal = elmt.element(randint(-500,1000),-50,"sakuraPetal.png")
            petal.texture = pygame.transform.scale(petal.texture,(40,40))
            petal.action = (randint(0,4),randint(0,2),randint(0,600))
            self.sakuraPetalManager.addElement(petal)

        Menutitle = elmt.element(300,200,"title.png")
        petal.texture = pygame.transform.scale(petal.texture,(40,40))
        textManager.elements.append(Menutitle)
        
        #====================== Bouttons Home Screen ===========================
        
        buttonPlay = elmt.element(5,300,"button.png")
        buttonPlay.setText(pygame.font.SysFont("comicsansms", 48).render('Play', True,(0,0,0)))
        buttonPlay.clickable = True
        buttonPlay.action = "SubMenu"
        buttonPlay.hoverable = True
        buttonManager.addElement(buttonPlay)

        buttonQuitter = elmt.element(450,300,"button.png")
        buttonQuitter.setText(self.font.render('Quitter', True,(0,0,0)))
        buttonQuitter.clickable = True
        buttonQuitter.action = "Quitter"
        buttonQuitter.hoverable = True
        buttonManager.addElement(buttonQuitter)
        
        #====================== Bouttons Sous Menu ===========================
        
        buttonNew = elmt.element(50,100,"button.png")
        buttonNew.setText(self.font.render('Nouveau', True,(0,0,0)))
        buttonNew.clickable = True
        buttonNew.action = "Jouer"
        buttonNew.hoverable = True
        buttonManagerSub.addElement(buttonNew)

        buttonLoad = elmt.element(450,100,"button.png")
        buttonLoad.setText(self.font.render('Charger', True,(0,0,0)))
        buttonLoad.clickable = True
        buttonLoad.action = "Charger"
        buttonLoad.hoverable = True
        buttonManagerSub.addElement(buttonLoad)

        #====================== Bouttons Jeu ===========================
        otherElmManagerJeu = elmtManager.elementManager()

        compteur = elmt.element(380,25,"compteur.png")
        compteur.setText(self.font.render("00:00:00", True,(0,0,0)))
        otherElmManagerJeu.addElement(compteur)

        buttonVerif = elmt.element(440,600,"buttonRect.png")
        buttonVerif.setTexture(pygame.transform.scale(buttonVerif.texture,(200,80)))
        buttonVerif.setText(pygame.transform.scale(self.font.render('Verifier', True,(0,0,0)),(150,70)))
        buttonVerif.clickable = True
        buttonVerif.action = "Verif"
        buttonManagerJeu.addElement(buttonVerif)

        buttonSauvegarder = elmt.element(200,600,"buttonRect.png")
        buttonSauvegarder.setTexture(pygame.transform.scale(buttonSauvegarder.texture,(200,80)))
        buttonSauvegarder.setText(pygame.transform.scale(self.font.render('Sauvegarder', True,(0,0,0)),(150,50)))
        buttonSauvegarder.clickable = True
        buttonSauvegarder.action = "Sauvegarder"
        buttonManagerJeu.addElement(buttonSauvegarder)

        buttonPause = elmt.element(680,600,"buttonRect.png")
        buttonPause.setTexture(pygame.transform.scale(buttonPause.texture,(200,80)))
        buttonPause.setText(pygame.transform.scale(self.font.render('Pause', True,(0,0,0)),(150,70)))
        buttonPause.clickable = True
        buttonPause.action = "Pause"
        buttonManagerJeu.addElement(buttonPause)

        #====================== Initialisation des Layouts ===========================

        self.titleScreen = Lyt.Layout()
        self.titleScreen.addElmtManager(buttonManager)
        self.titleScreen.addElmtManager(textManager)

        self.subMenu = Lyt.Layout()
        self.subMenu.addElmtManager(buttonManagerSub)

        self.jeuLayout = Lyt.Layout()
        self.jeuLayout.addElmtManager(buttonManagerJeu)
        self.jeuLayout.addElmtManager(otherElmManagerJeu)


        
        
