from random import shuffle,sample
import pygame
import element as elmt

class Sudoku:
    def __init__(self, base):
        self.base = base
        self.taille = base * base
        self.grille = [[0 for colone in range(0,self.taille)] for ligne in range(0,self.taille)]
        self.number = ['1','2','3','4','5','6','7','8','9']
        self.remplissage()
        self.vidage(3//4)


        self.backgroundGrille = elmt.element(0,0,"case.png")
        self.backgroundGrille.setTexture(pygame.transform.scale(self.backgroundGrille.texture,(440,440)))
        self.backgroundGrille.setPosition(540 - self.backgroundGrille.texture_rect.centerx,360 - self.backgroundGrille.texture_rect.centery)
        self.cases = []
        x = self.backgroundGrille.texture_rect.x+40
        y = self.backgroundGrille.texture_rect.y+40
        for i in range(0,self.taille * self.taille ):
            if x > 0:
                x = x - 1
            if i % 3 == 0:
                x = x + 2
            case = elmt.element(x,y)
            self.font = pygame.font.SysFont("comicsansms", 24)
            case.setTexture(pygame.Surface((40,40),pygame.SRCALPHA))
            case.setText(self.font.render(self.grilleDeJeu[i//9][i%9], True,(255,255,255)))
            pygame.draw.rect(case.texture,(120,120,255,255),(0,0,40,40),width=1)
            case.clickable = True
            case.action = "change"
            self.cases.append(case)
            x = x + 40
            if i % 9 == 8:
                y = y + 40
                if y > 0:
                    y = y - 1
                if i // 9 % 3 == 2:
                    y = y + 2
                x = self.backgroundGrille.texture_rect.x + 40

    def vidage(self,fraction):
        self.grilleDeJeu = self.grille
        empties = 81 * 3//4
        for p in sample(range(81),empties):
           self.grilleDeJeu[p//9][p%9] = ' '

    def checkgrille(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.grille[row][col]==0:
                    return False
        return True 

    def remplissage(self):
        for i in range(0,81):
            row=i//9
            col=i%9
            if self.grille[row][col]==0:
                shuffle(self.number)      
                for value in self.number:
                    if not(value in self.grille[row]):
                        if not value in (self.grille[0][col],self.grille[1][col],self.grille[2][col],self.grille[3][col],self.grille[4][col],self.grille[5][col],self.grille[6][col],self.grille[7][col],self.grille[8][col]):
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[self.grille[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[self.grille[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[self.grille[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[self.grille[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[self.grille[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[self.grille[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[self.grille[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[self.grille[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[self.grille[i][6:9] for i in range(6,9)]
                            if not value in (square[0] + square[1] + square[2]):
                                self.grille[row][col]=value
                                if self.checkgrille():
                                    return True
                                else:
                                    if self.remplissage():
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
                tier = len(self.grille) // 3
                tierdouble = (len(self.grille) // 3) * 2
                entier = len(self.grille)
                if l < tier:
                    if c < tier:
                        square = [self.grille[i][0:tier] for i in range(0, tier)]
                    elif c < tierdouble:
                        square = [self.grille[i][tier:tierdouble] for i in range(0, tier)]
                    else:
                        square = [self.grille[i][tierdouble:entier] for i in range(0, tier)]
                elif l < tierdouble:
                    if c < tier:
                        square = [self.grille[i][0:tier] for i in range(tier, tierdouble)]
                    elif c < tierdouble:
                        square = [self.grille[i][tier:tierdouble] for i in range(tier, tierdouble)]
                    else:
                        square = [self.grille[i][tierdouble:entier] for i in range(tier, tierdouble)]
                else:
                    if c < tier:
                        square = [self.grille[i][0:tier] for i in range(tierdouble, entier)]
                    elif c < tierdouble:
                        square = [self.grille[i][tier:tierdouble] for i in range(tierdouble, entier)]
                    else:
                        square = [self.grille[i][tierdouble:entier] for i in range(tierdouble, entier)]
                bloc = (square[0] + square[1] + square[2])
                if target in bloc:
                    bloc.remove(target)
                    if target in bloc:
                        etat = False
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

            for colone in range(0,len(self.grille[ligne])):
                if colone % self.base == 0:
                    print("|", end=' ')
                if self.grille[ligne][colone] == 0:
                    print(0, end=' ')
                else:
                    print(self.grille[ligne][colone], end=' ')

                if colone == len(self.grille[ligne])-1:
                    print("|")

            if ligne == self.base*self.base-1:
                interligne(len(self.grille[colone]))

    def render(self,screen):
        self.backgroundGrille.render(screen)
        for case in self.cases :
            case.render(screen)

    def event(self,event):
        for case in self.cases:
            action = element.eventElmt(event)
            if not action == None:
                return action
    
    def load(self, path):
        with open(path, mode="r") as fichier:
            # Les etapes en lecture sur le fichier
            content = fichier.read()
            if content == "":
                print("Il n'y a rien a charger.")
            else:
                i = 0
                for l in range(len(self.grille)):
                    for c in range(len(self.grille)):
                        if content[i] == "-":
                            self.grille[l][c] = -int(content[i + 1])
                            i += 2
                        else:
                            self.grille[l][c] = int(content[i])
                            i += 1
            fichier.close()

    def save(self, path):
        with open(path, mode="w") as fichier:
            # Les etapes en ecriture sur le fichier
            content = ""
            for l in range(len(self.grille)):
                for c in range(len(self.grille)):
                    content += str(self.grille[l][c])
            fichier.write(content)
            fichier.close()
