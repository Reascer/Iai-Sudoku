from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from Jeu import *

#====================== Classe main du programme ===========================#

jeu = Jeu("Iai-sudoku",1200,800)

while jeu.running:
    jeu.event()
    if not jeu.running:
        break
    jeu.update()
    jeu.render()
