import pygame
import element as elmt
import elementManager as elmtManager
from Sons import SoundManager
from Sudoku import Sudoku
import Layout as Lyt
from random import randint

#====================== Classe principale du programme ===========================#

class Jeu:
    def __init__(self,title,width,height):
        pygame.init() #initalisation de pygame
        self.title = title
        self.width = width
        self.height = height
        self.layoutEnCours = "titleScreen"        
        self.heure = 0
        self.minute = 0
        self.seconde = 0
        self.running = True
        self.timer = False
        self.Pause = True
        self.sudoku = Sudoku()
        self.sakuraDelay = 0
        self.sound_manager = SoundManager()

        pygame.display.set_caption(title) # Mettre le titre sur Iai-sudoku <3
        self.screen = pygame.display.set_mode((width,height)) # Resize la fenêtre
        self.font = pygame.font.SysFont("comicsansms", 30) # initialisaTIon des font (pour le texte)

        self.initRender()

#====================== Liste des events pris en charge par l'application ===========================#

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
                    self.sound_manager.playOneTime('click')
                    self.layoutEnCours = "SubMenu"
            elif self.layoutEnCours == "SubMenu":
                action = self.subMenu.event(event)
                if action == 'Jouer':
                    self.sound_manager.playOneTime('click')
                    self.layoutEnCours = "ChoixGrille"
                if action == 'Charger':
                    self.sound_manager.playOneTime('click')
                    self.loading.render(self.screen)
                    pygame.display.flip()
                    ok = self.sudoku.loadMenu()
                    if ok == True:
                        vie = ''
                        for i in range(self.sudoku.trys):
                            vie = vie + 'O'
                            if i != self.sudoku.trys-1:
                                vie = vie + ' '
                        self.jeuLayout.listElmtManager[0].elements[1].setText(self.font.render(vie, True,(0,190,0)))
                        self.sound_manager.playXTime('vent')
                        self.heure = int(self.sudoku.stringCompteur[0:2])
                        self.minute = int(self.sudoku.stringCompteur[3:5])
                        self.seconde = int(self.sudoku.stringCompteur[6:8])
                        self.jeuLayout.listElmtManager[0].elements[0].setText(self.font.render(self.sudoku.stringCompteur, True,(0,0,0)))
                        if self.sudoku.base == 4:
                            x = 10
                            y = 200
                            i = 0
                            for button in self.jeuLayout.listElmtManager[1].elements:
                                i = i + 1
                                button.setPosition(x,y)
                                y = y + 150
                                if i == 3:
                                    break
                            self.jeuLayout.listElmtManager[0].elements[1].setPosition(70,130)
                            self.jeuLayout.listElmtManager[0].elements[0].setPosition(50,40)
                        else:
                            self.jeuLayout.listElmtManager[0].elements[0].setPosition(450,5)
                            self.jeuLayout.listElmtManager[0].elements[1].setPosition(470,95)
                            self.jeuLayout.listElmtManager[1].elements[0].setPosition(420,620)
                            self.jeuLayout.listElmtManager[1].elements[1].setPosition(100,620)
                            self.jeuLayout.listElmtManager[1].elements[2].setPosition(740,620)
                        self.layoutEnCours = "Jeu"
                if action == 'Back':
                    self.sound_manager.playOneTime('click')
                    self.layoutEnCours = 'titleScreen'
            elif self.layoutEnCours == 'ChoixGrille':
                action = self.choixGrille.event(event)
                if action == 'Neuf':
                    self.sound_manager.playOneTime('click')
                    self.loading.render(self.screen)
                    pygame.display.flip()
                    self.launchSudoku(3)
                    self.layoutEnCours = "Jeu"
                    self.sound_manager.playXTime('vent')
                    self.jeuLayout.listElmtManager[0].elements[0].setPosition(450,5)
                    self.jeuLayout.listElmtManager[0].elements[1].setPosition(470,95)
                    self.jeuLayout.listElmtManager[1].elements[0].setPosition(420,620)
                    self.jeuLayout.listElmtManager[1].elements[1].setPosition(100,620)
                    self.jeuLayout.listElmtManager[1].elements[2].setPosition(740,620)
                if action == 'Seize':
                    self.sound_manager.playOneTime('click')
                    self.loading.render(self.screen)
                    pygame.display.flip()
                    self.launchSudoku(4)
                    self.layoutEnCours = "Jeu"
                    self.sound_manager.playXTime('vent')
                    x = 10
                    y = 210
                    i = 0
                    for button in self.jeuLayout.listElmtManager[1].elements:
                        i = i + 1
                        button.setPosition(x,y)
                        y= y + 130
                        if i == 4:
                            break
                    self.jeuLayout.listElmtManager[0].elements[0].setPosition(50,45)
                    self.jeuLayout.listElmtManager[0].elements[1].setPosition(70,135)

                if action == 'Back':
                    self.sound_manager.playOneTime('click')
                    self.layoutEnCours = 'titleScreen'
            elif self.layoutEnCours == "Jeu":
                if not self.timer:
                    self.jeuLayout.listElmtManager[1].elements[4].hoverable = False
                    pygame.time.set_timer( pygame.USEREVENT + 1,1000)
                    self.timer = True
                action = self.jeuLayout.event(event)
                if action == 'Ready':
                    self.Pause = False
                    self.sound_manager.playOneTime('hajime')
                    self.jeuLayout.listElmtManager[1].elements.pop()
                    for button in self.jeuLayout.listElmtManager[1].elements:
                        button.clickable = True
                        button.hoverable = True

                if action == 'howToPlay':
                    self.Pause = True
                    for button in self.jeuLayout.listElmtManager[1].elements:
                        button.clickable = False
                        button.hoverable = False
                    screenTuto = elmt.element(0,0,"tuto.png")
                    screenTuto.clickable = True
                    screenTuto.action = "Tuto"
                    self.jeuLayout.listElmtManager[1].addElement(screenTuto)

                if action == 'Tuto':
                    self.Pause = False
                    self.jeuLayout.listElmtManager[1].elements.pop()
                    for button in self.jeuLayout.listElmtManager[1].elements:
                        button.clickable = True
                        button.hoverable = True

                if action == 'Sauvegarder':
                    self.sound_manager.playOneTime('click')
                    self.sudoku.save()

                if action == 'Verif':
                    if self.sudoku.isFinish():
                        self.sound_manager.playOneTime('banzai')
                        self.Pause = True
                        Banzai = elmt.element(0,0,"Banzai.png")
                        Banzai.clickable = True
                        Banzai.action = "titleScreen"
                        self.jeuLayout.listElmtManager[0].addElement(Banzai)
                        print("tu win bro")
                    else:
                        self.sudoku.trys = self.sudoku.trys - 1
                        vie = ''
                        for i in range(self.sudoku.trys):
                            vie = vie + 'O'
                            if i != self.sudoku.trys-1:
                                vie = vie + ' '
                        self.jeuLayout.listElmtManager[0].elements[1].setText(self.font.render(vie, True,(0,190,0)))   
                        if self.sudoku.trys == 0:
                            self.layoutEnCours = "titleScreen"
                            self.jeuLayout.listElmtManager[0].elements[1].render(self.screen)
                            self.Seppuku.render(self.screen)
                            pygame.display.flip()
                            self.sound_manager.playOneTime('seppuku')
                            pygame.time.wait(1000)
                            self.sound_manager.playOneTime('loose')
                            pygame.time.wait(2000)
                        else:
                            self.sound_manager.playOneTime('loose')
                
                if action == 'Pause':
                    self.sound_manager.playOneTime('click')
                    if self.Pause == False:
                        self.Pause = True
                    else:
                        self.Pause = False

                if action == 'Back':
                    self.sound_manager.playOneTime('click')
                    self.layoutEnCours = 'titleScreen'
                    self.subMenu.listElmtManager[0].elements[2].setPosition(820,-10)
               
                if not self.Pause:
                    self.sudoku.event(event)
                
                if action == "titleScreen":
                    self.layoutEnCours = "titleScreen"
                
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
                        self.jeuLayout.listElmtManager[0].elements[0].setText(self.font.render(stringCompteur, True,(0,0,0)))

#====================== Lancement du Layout "Ready", lançant la grille de Sudoku ===========================#

    def launchSudoku(self, base):
        self.heure = 0
        self.minute = 0
        self.seconde = 0
        self.Pause = True
        screenReady = elmt.element(0,0,"Ready.png")
        screenReady.clickable = True
        screenReady.action = "Ready"
        self.jeuLayout.listElmtManager[1].addElement(screenReady)
        self.sudoku = Sudoku(base)
        self.jeuLayout.listElmtManager[0].elements[0].setText(self.font.render(self.sudoku.stringCompteur, True,(0,0,0)))
        vie = ''
        for i in range(self.sudoku.trys):
            vie = vie + 'O'
            if i != self.sudoku.trys-1:
                vie = vie + ' '
        self.jeuLayout.listElmtManager[0].elements[1].setText(self.font.render(vie, True,(0,190,0)))        
        self.sudoku.afficher()

#====================== Lancement du Layout "Ready", lançant la grille de Sudoku ===========================#

    def update(self):
        for petal in self.sakuraPetalManager.elements:
            if self.sakuraDelay < petal.action[2]:
                pass
            else:
                petal.texture_rect.x = petal.texture_rect.x + petal.action[0]
                petal.texture_rect.y = petal.texture_rect.y + petal.action[1]
                if petal.texture_rect.y > self.screen.get_height():
                    petal.texture_rect.y = -50
                    petal.texture_rect.x = randint(-500,1000)
        if self.sakuraDelay <= 600:
            self.sakuraDelay = self.sakuraDelay + 1

#====================== Activation des layouts suivant la valeur de la variable "layoutEnCours" ===========================#

    def render(self):
        if self.layoutEnCours == 'Jeu':
            self.backgroundManager.renderElements(self.screen,1)
            self.sakuraPetalManager.renderElements(self.screen)
            self.sudoku.render(self.screen)
            self.jeuLayout.render(self.screen)

        if self.layoutEnCours == "titleScreen":
            self.backgroundManager.renderElements(self.screen,0)
            self.sakuraPetalManager.renderElements(self.screen)
            self.titleScreen.render(self.screen)

        if self.layoutEnCours == "SubMenu":
            self.backgroundManager.renderElements(self.screen,0)
            self.sakuraPetalManager.renderElements(self.screen)
            self.subMenu.render(self.screen)

        if self.layoutEnCours == "ChoixGrille":
            self.backgroundManager.renderElements(self.screen,0)
            self.sakuraPetalManager.renderElements(self.screen)
            self.choixGrille.render(self.screen)

        pygame.display.flip()

    def quit(self):
        self.running = False
        pygame.quit()
        print("end of game")

        #====================== Ajouter les elements dans l'initRender ===========================#

    def initRender(self):
        self.backgroundManager = elmtManager.elementManager()
        self.sakuraPetalManager = elmtManager.elementManager()
        textManager = elmtManager.elementManager()
        buttonManager = elmtManager.elementManager()
        buttonManagerSub = elmtManager.elementManager()
        buttonManagerGrille = elmtManager.elementManager()
        buttonManagerJeu = elmtManager.elementManager()

        #====================== element a ajouter ===========================#

        titleBackground = elmt.element(0,0,"sakuraBackground.jpg")
        titleBackground.texture = pygame.transform.scale(titleBackground.texture,(self.width,self.height))
        self.backgroundManager.addElement(titleBackground)

        jeuBackground = elmt.element(0,0,"sakuraBackground2.jpg")
        jeuBackground.texture = pygame.transform.scale(jeuBackground.texture,(self.width,self.height))
        self.backgroundManager.addElement(jeuBackground)

        for i in range(50):
            petal = elmt.element(randint(-500,1000),-50,"sakuraPetal.png")
            petal.texture = pygame.transform.scale(petal.texture,(40,40))
            petal.action = (randint(1,5),randint(1,3),randint(0,600))
            self.sakuraPetalManager.addElement(petal)

        Menutitle = elmt.element(355,230,"title.png")
        petal.texture = pygame.transform.scale(petal.texture,(40,40))
        textManager.elements.append(Menutitle)

        self.loading = elmt.element(0,0,"loading.png")
        self.Seppuku = elmt.element(0,0,"Seppuku.png")

        #====================== Bouttons Home Screen ===========================#

        buttonPlay = elmt.element(5,330,"button.png")
        buttonPlay.setText(pygame.font.SysFont("comicsansms", 48).render('Play', True,(0,0,0)))
        buttonPlay.clickable = True
        buttonPlay.action = "SubMenu"
        buttonPlay.hoverable = True
        buttonManager.addElement(buttonPlay)

        buttonQuitter = elmt.element(560,330,"button.png")
        buttonQuitter.setText(self.font.render('Quitter', True,(0,0,0)))
        buttonQuitter.clickable = True
        buttonQuitter.action = "Quitter"
        buttonQuitter.hoverable = True
        buttonManager.addElement(buttonQuitter)

        #====================== Bouttons Sous Menu ===========================#

        buttonNew = elmt.element(5,330,"button.png")
        buttonNew.setText(self.font.render('Nouveau', True,(0,0,0)))
        buttonNew.clickable = True
        buttonNew.action = "Jouer"
        buttonNew.hoverable = True
        buttonManagerSub.addElement(buttonNew)

        buttonLoad = elmt.element(560,330,"button.png")
        buttonLoad.setText(self.font.render('Charger', True,(0,0,0)))
        buttonLoad.clickable = True
        buttonLoad.action = "Charger"
        buttonLoad.hoverable = True
        buttonManagerSub.addElement(buttonLoad)

        # ====================== Bouttons Choix Grille ===========================#

        buttonNeuf = elmt.element(5, 330, "button.png")
        buttonNeuf.setText(self.font.render('9x9', True, (0, 0, 0)))
        buttonNeuf.clickable = True
        buttonNeuf.action = "Neuf"
        buttonNeuf.hoverable = True
        buttonManagerGrille.addElement(buttonNeuf)

        buttonSeize = elmt.element(560, 330, "button.png")
        buttonSeize.setText(self.font.render('16x16', True, (0, 0, 0)))
        buttonSeize.clickable = True
        buttonSeize.action = "Seize"
        buttonSeize.hoverable = True
        buttonManagerGrille.addElement(buttonSeize)

        #====================== Bouttons Jeu ===========================#

        otherElmManagerJeu = elmtManager.elementManager()

        compteur = elmt.element(450,5,"compteur.png")
        compteur.setText(self.font.render("00:00:00", True,(0,0,0)))
        otherElmManagerJeu.addElement(compteur)

        vie = elmt.element(470,95,"compteur.png")
        vie.setTexture(pygame.transform.scale(vie.texture,(278,74)))
        vie.setText(self.font.render(vie.action, True,(0,190,0)))
        otherElmManagerJeu.addElement(vie)

        buttonVerif = elmt.element(420,620,"buttonRect.png")
        buttonVerif.setTexture(pygame.transform.scale(buttonVerif.texture,(400,180)))
        buttonVerif.setText(self.font.render('Verifier', True,(0,0,0)))
        buttonVerif.clickable = False
        buttonVerif.hoverable = False
        buttonVerif.action = "Verif"
        buttonManagerJeu.addElement(buttonVerif)

        buttonSauvegarder = elmt.element(100,620,"buttonRect.png")
        buttonSauvegarder.setTexture(pygame.transform.scale(buttonSauvegarder.texture,(400,180)))
        buttonSauvegarder.setText(pygame.transform.scale(self.font.render('Sauvegarder', True,(0,0,0)),(150,50)))
        buttonSauvegarder.clickable = False
        buttonSauvegarder.hoverable = False
        buttonSauvegarder.action = "Sauvegarder"
        buttonManagerJeu.addElement(buttonSauvegarder)

        buttonPause = elmt.element(740,620,"buttonRect.png")
        buttonPause.setTexture(pygame.transform.scale(buttonPause.texture,(400,180)))
        buttonPause.setText(self.font.render('Pause', True,(0,0,0)))
        buttonPause.clickable = False
        buttonPause.hoverable = False
        buttonPause.action = "Pause"
        buttonPause.clickStateToggle = True
        buttonManagerJeu.addElement(buttonPause)

        buttonhtp = elmt.element(120,0)
        buttonhtp.setText(self.font.render('How to play ?', True,(0,0,0)))
        buttonhtp.setTexture(pygame.Surface((buttonhtp.text.get_rect().w,buttonhtp.text.get_rect().h),pygame.SRCALPHA))
        buttonhtp.clickable = False
        buttonhtp.hoverable = False
        buttonhtp.alphaClickable = False
        buttonhtp.action = "howToPlay"

        #====================== Bouttons Back to Home ===========================#

        buttonBack = elmt.element(820,-10,"buttonRect.png")
        buttonBack.setTexture(pygame.transform.scale(buttonBack.texture,(400,180)))
        buttonBack.setText(pygame.font.SysFont("comicsansms", 44).render('Menu', True,(0,0,0)))
        buttonBack.clickable = True
        buttonBack.action = "Back"
        buttonBack.hoverable = True
        buttonManagerSub.addElement(buttonBack)
        buttonManagerGrille.addElement(buttonBack)
        buttonManagerJeu.addElement(buttonBack)
        buttonManagerJeu.addElement(buttonhtp)
        
        #====================== Initialisation des Layouts ===========================#

        self.titleScreen = Lyt.Layout()
        self.titleScreen.addElmtManager(buttonManager)
        self.titleScreen.addElmtManager(textManager)

        self.subMenu = Lyt.Layout()
        self.subMenu.addElmtManager(buttonManagerSub)
        self.subMenu.addElmtManager(textManager)

        self.choixGrille = Lyt.Layout()
        self.choixGrille.addElmtManager(buttonManagerGrille)
        self.choixGrille.addElmtManager(textManager)

        self.jeuLayout = Lyt.Layout()
        self.jeuLayout.addElmtManager(otherElmManagerJeu)
        self.jeuLayout.addElmtManager(buttonManagerJeu)
