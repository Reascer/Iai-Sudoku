from Jeu import *


jeu = Jeu("Iai-sudoku",0.75,0.75)

while jeu.running:
    jeu.render()
    jeu.update()
    jeu.event()


