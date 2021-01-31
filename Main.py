from Jeu import *

jeu = Jeu("Iai-sudoku",1200,800)

while jeu.running:
    jeu.event()
    jeu.update()
    if not jeu.running:
        break
    jeu.render()
