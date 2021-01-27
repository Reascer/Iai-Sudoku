from random import shuffle

class Sudoku:
    def __init__(self, base):
        self.base = base
        taille = base * base
        self.grille = [[0 for colone in range(0,taille)] for ligne in range(0,taille)]
        self.number = ['1','2','3','4','5','6','7','8','9']
        self.remplissage()

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
    