from Jeu import *


jeu = Jeu("Iai-sudoku",1080,720)

while jeu.running:
    jeu.event()
    jeu.update()
    if jeu.running == False:
        break
    jeu.render()


