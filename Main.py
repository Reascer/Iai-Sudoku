from Jeu import *

jeu = Jeu("Iai-sudoku",3,1200,800)

while jeu.running:
    jeu.event()
    if not jeu.running:
        break
    jeu.update()
    jeu.render()
