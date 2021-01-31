from random import shuffle,sample
import pygame
import element as elmt
from tkinter import filedialog, Tk
import case as cse
from os import getcwd
from datetime import datetime

class Sudoku:
    def __init__(self, base):
        self.base = base
        self.taille = base * base
        self.grille = [[0 for colone in range(0,self.taille)] for ligne in range(0,self.taille)]
        self.grilleDeJeu = [[0 for colone in range(0,self.taille)] for ligne in range(0,self.taille)]
        self.number9 = ['1','2','3','4','5','6','7','8','9']
        self.number16 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G']
        self.remplissage(self.base)
        self.vidage(3,5)
        self.stringCompteur = ""

        self.backgroundGrille = elmt.element(0,0,"case.png")
        if self.base == 3:
            self.backgroundGrille.setTexture(pygame.transform.scale(self.backgroundGrille.texture,(440,440)))
            self.backgroundGrille.setPosition(610 - self.backgroundGrille.texture_rect.centerx,400 - self.backgroundGrille.texture_rect.centery)
        elif self.base == 4:
            self.backgroundGrille.setTexture(pygame.transform.scale(self.backgroundGrille.texture,(783,783)))
            self.backgroundGrille.setPosition(610 - self.backgroundGrille.texture_rect.centerx,743 - self.backgroundGrille.texture_rect.centery)
        self.initRender()
    
    def initRender(self):
        self.cases = []
        # if self.base==3:
        x = self.backgroundGrille.texture_rect.x+40
        y = self.backgroundGrille.texture_rect.y+40
        # elif self.base==4:
        #     x = self.backgroundGrille.texture_rect.x+40
        #     y = self.backgroundGrille.texture_rect.y+40
        for i in range(0,self.taille * self.taille ):
            if x > 0:
                x = x - 1
            if i % self.base == 0:
                x = x + 2
            case = cse.case((i//self.taille,i%self.taille),self.grilleDeJeu[i//self.taille][i%self.taille],x,y)
            self.font = pygame.font.SysFont("comicsansms", 20)
            # if self.base==3:
            case.setTexture(pygame.Surface((40,40),pygame.SRCALPHA))
            # if self.base==4:
            #     case.setTexture(pygame.Surface((54,54),pygame.SRCALPHA))
            case.setText(self.font.render(self.grilleDeJeu[i//self.taille][i%self.taille], True,(255,255,255))) # TO CHECK POUR 16x16
            pygame.draw.rect(case.texture,(150,150,255,255),(0,0,40,40),width=1)
            case.clickable = True
            case.alphaClickable = False
            case.clickStateToggle = True

            self.cases.append(case)

            z = 40
            x = x + z
            if i % self.taille == self.taille-1:
                y = y + z
                if y > 0:
                    y = y - 1
                if i // self.taille % self.base == self.base-1:
                    y = y + 2
                x = self.backgroundGrille.texture_rect.x + z

    def vidage(self,nomin,denomin):
        empties = (self.taille * self.taille) * nomin//denomin
        for p in sample(range((self.taille * self.taille) ),empties):
           self.grilleDeJeu[p//self.taille][p%self.taille] = ' '

    def checkgrille(self):
        for row in range(0,self.taille):
            for col in range(0,self.taille):
                if self.grille[row][col]==0:
                    return False
        return True 

    def remplissage(self, base):
        size = self.taille*self.taille
        for i in range(0,size):
            row=i//self.taille
            col=i%self.taille
            if self.grille[row][col]==0:
                shuffle(self.number9)      
                for value in self.number9:
                    if not(value in self.grille[row]):
                        
                        # if base == 3:
                        #     caseList = self.grille[0][col],self.grille[1][col],self.grille[2][col],self.grille[3][col],self.grille[4][col],self.grille[5][col],self.grille[6][col],self.grille[7][col],self.grille[8][col]                
                        # elif base == 4:
                        #     caseList = self.grille[0][col],self.grille[1][col],self.grille[2][col],self.grille[3][col],self.grille[4][col],self.grille[5][col],self.grille[6][col],self.grille[7][col],self.grille[8][col],self.grille[9][col],self.grille[10][col],self.grille[11][col],self.grille[12][col],self.grille[13][col],self.grille[14][col],self.grille[15][col]
                        # if not value in (caseList):
                        if not value in [self.grille[i][col] for i in range (0, self.taille-1)]:
                            square=[]
                            if row<base:
                                if col<base:
                                    square=[self.grille[i][0:base] for i in range(0,base)]
                                elif col<base*2:
                                    square=[self.grille[i][base:base*2] for i in range(0,base)]
                                elif col<base*3:  
                                    square=[self.grille[i][base*2:base*3] for i in range(0,base)]
                                elif col<base*4:  
                                    square=[self.grille[i][base*3:self.taille] for i in range(0,base)]
                            elif row<base*2:
                                if col<base:
                                    square=[self.grille[i][0:base] for i in range(base,base*2)]
                                elif col<base*2:
                                    square=[self.grille[i][base:base*2] for i in range(base,base*2)]
                                elif col<base*3:  
                                    square=[self.grille[i][base*2:base*3] for i in range(base,base*2)]
                                elif col<base*4:  
                                    square=[self.grille[i][base*3:self.taille] for i in range(base,base*2)]
                            elif row<base*3:
                                if col<base:
                                    square=[self.grille[i][0:base] for i in range(base*2,base*3)]
                                elif col<base*2:
                                    square=[self.grille[i][base:base*2] for i in range(base*2,base*3)]
                                elif col<base*3:  
                                    square=[self.grille[i][base*2:base*3] for i in range(base*2,base*3)]
                                elif col<base*4:  
                                    square=[self.grille[i][base*3:self.taille] for i in range(base*2,base*3)]
                            elif row<base*4:
                                if col<base:
                                    square=[self.grille[i][0:base] for i in range(base*3,self.taille)]
                                elif col<base*2:
                                    square=[self.grille[i][base:base*2] for i in range(base*3,self.taille)]
                                elif col<base*3:  
                                    square=[self.grille[i][base*2:base*3] for i in range(base*3,self.taille)]
                                elif col<base*4:  
                                    square=[self.grille[i][base*3:self.taille] for i in range(base*3,self.taille)]
                            if base == 3:
                                if not value in (square[0] + square[1] + square[2]):
                                    self.grille[row][col]=value
                                    self.grilleDeJeu[row][col]=value
                                    if self.checkgrille():
                                        return True
                                    else:
                                        if self.remplissage(self.base):
                                            return True
                            if base == 4:
                                if not value in (square[0] + square[1] + square[2] + square[3]):
                                    self.grille[row][col]=value
                                    self.grilleDeJeu[row][col]=value
                                    if self.checkgrille():
                                        return True
                                    else:
                                        if self.remplissage(self.base):
                                            return True
                break
        self.grille[row][col]=0

    def isValide(self):
        etat = True
        for l in range(len(self.grille)):
            for c in range(len(self.grille[l])):
                target = self.grille[l][c]
                if self.grille[l].count(target) > 1:
                    etat = False
                checkColonne = []
                for iLigne in range(len(self.grille)):
                    checkColonne.append(self.grille[iLigne][c])
                if checkColonne.count(target) > 1:
                    etat = False
                square = []
                line = len(self.grille) // self.base
                entier = len(self.grille)
                if l < line:
                    if c < line:
                        square = [self.grille[i][0:line] for i in range(0, line)]
                    elif c < line*line:
                        square = [self.grille[i][line:line*line] for i in range(0, line)]
                    elif c < line**line:
                        square = [self.grille[i][line*line:line**line] for i in range(0, line)]
                    elif c < entier & self.base == 4:
                        square = [self.grille[i][line**line:entier] for i in range(0, line)]
                elif l < line*line:
                    if c < line:
                        square = [self.grille[i][0:line] for i in range(line, line*line)]
                    elif c < line*line:
                        square = [self.grille[i][line:line*line] for i in range(line, line*line)]
                    elif c < line**line:
                        square = [self.grille[i][line*line:line**line] for i in range(line, line*line)]
                    elif c < entier & self.base == 4:
                        square = [self.grille[i][line**line:entier] for i in range(line, line*line)]
                elif l < line**line:
                    if c < line:
                        square = [self.grille[i][0:line] for i in range(line*line, line**line)]
                    elif c < line*line:
                        square = [self.grille[i][line:line*line] for i in range(line*line, line**line)]
                    elif c < line**line:
                        square = [self.grille[i][line*line:line**line] for i in range(line*line, line**line)]
                    elif c < entier & self.base == 4:
                        square = [self.grille[i][line**line:entier] for i in range(line*line, line**line)]
                elif l < line*4 & self.base == 4:
                    if c < line:
                        square = [self.grille[i][0:line] for i in range(line**line, entier)]
                    elif c < line*line:
                        square = [self.grille[i][line:line*line] for i in range(line**line, entier)]
                    elif c < line**line:
                        square = [self.grille[i][line*line:line**line] for i in range(line**line, entier)]
                    else:
                        square = [self.grille[i][line**line:entier] for i in range(line**line, entier)]
                
                
                
                # if self.base == 3:        
                    # bloc = (square[0] + square[1] + square[2])                    
                bloc = list([square[i] for i in range (0, self.base-1)])
                if target in bloc:
                    bloc.remove(target)
                    if target in bloc:
                        etat = False
                # if self.base == 4:        
                #     bloc = (square[0] + square[1] + square[2] + square[3])
                    # if target in bloc:
                    #     bloc.remove(target)
                    #     if target in bloc:
                    #         etat = False
        return etat

    def afficher(self):
        def interligne(taille):
            for i in range(0,taille):
                if i % self.base == 0:
                    print("+-", end='')
                print("--",end='')
            print("+")

        for ligne in range(0,len(self.grille)):
            if ligne % self.base == 0:
                interligne(len(self.grille[ligne]))

            for colonne in range(0,len(self.grille[ligne])):
                if colonne % self.base == 0:
                    print("|", end=' ')
                if self.grille[ligne][colonne] == 0:
                    print(0, end=' ')
                else:
                    print(self.grille[ligne][colonne], end=' ')

                if colonne == len(self.grille[ligne])-1:
                    print("|")

            if ligne == self.taille-1:
                interligne(len(self.grille[colonne]))

    def render(self,screen):
        self.backgroundGrille.render(screen)
        for case in self.cases :
            case.render(screen)
    
    def event(self,event):
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == "escape":
                for case in self.cases :
                    case.clickState = False
                    case.rightClickState = False
        for case in self.cases:
            case.event(event)
            if case.grilleValeur == ' ':
                if case.rightClickState:
                    for case2 in self.cases :
                        case2.clickState = False
                if case.clickState:
                    for case2 in self.cases :
                        case2.rightClickState = False
                    pygame.draw.rect(case.texture,(255,120,120,255),(1,1,38,38),width=1)
                    if event.type == pygame.KEYDOWN:
                        if self.base == 3:
                            buttonList = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","backspace"]
                        elif self.base == 4:
                            buttonList = ("[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","A","[b]","[c]","[d]","[e]","[f]","[g]","backspace")    
                        if pygame.key.name(event.key) in buttonList:
                            if pygame.key.name(event.key) == "backspace":
                                case.indices = []
                                self.grilleDeJeu[case.grillePos[0]][case.grillePos[1]] = ' '
                                case.setText(self.font.render(' ', True,(120,120,120)))
                                case.clickState = False
                            else:    
                                self.grilleDeJeu[case.grillePos[0]][case.grillePos[1]] = pygame.key.name(event.key)[1]
                                case.setText(self.font.render(pygame.key.name(event.key)[1], True,(120,120,120)))
                                case.clickState = False
                else:
                    if not case.rightClickState:
                        pygame.draw.rect(case.texture,(0,0,0,0),(1,1,38,38),width=1)
                if case.texture_rect.collidepoint(pygame.mouse.get_pos()):
                    if not case.clickState and not case.rightClickState:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        pygame.draw.rect(case.texture,(120,255,120,255),(1,1,38,38),width=1)
                else:
                    if not case.clickState and not case.rightClickState:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        pygame.draw.rect(case.texture,(0,0,0,0),(1,1,38,38),width=1)
            
    def loadMenu(self):
        root = Tk()
        root.withdraw()
        return self.load(filedialog.askopenfilename(initialdir = "./", filetypes=(("Fichier Grille", ".sudoku"), ('Tout Fichier', "*.*"))))
        
    def load(self, path):
        try:
            with open(path, mode="r") as fichier:
                # Les etapes en lecture sur le fichier
                content = fichier.readline()
                if content == "":
                    print("Il n'y a rien a charger.")
                else:
                    for i in range(self.taille*self.taille):
                        self.grilleDeJeu[i//self.taille][i%self.taille] = content[i]
                    content = fichier.readline()
                    for i in range(self.taille*self.taille):
                        self.grille[i//self.taille][i%self.taille] = content[i]
                    self.stringCompteur = fichier.readline()
                self.initRender()
                fichier.close()
                return True
        except FileNotFoundError:
            print("Il n'y a rien a charger.")
            return False

    def save(self):
        dateNow = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        path = str(getcwd()+'\\'+'grille_'+dateNow+'.sudoku')
        with open(path, mode="w") as fichier:
            # Les etapes en ecriture sur le fichier
            grilleActu = ""
            for l in range(len(self.grilleDeJeu)):
                for c in range(len(self.grilleDeJeu)):
                    grilleActu += str(self.grilleDeJeu[l][c])
            grilleFinale = ""
            for l in range(len(self.grille)):
                for c in range(len(self.grille)):
                    grilleFinale += str(self.grille[l][c])
            fichier.write(grilleActu)
            fichier.write('\n')
            fichier.write(grilleFinale)
            fichier.write('\n')
            fichier.write(self.stringCompteur)
            print(path)
            fichier.close()

    def isFinish(self):
        if self.grille == self.grilleDeJeu:
            print("BANZAÏ !!")
        else:
            print("Seppuku...")

    def __del__(self):
        self.grille = []
        self.grilleDeJeu = []   
        self.cases = []
