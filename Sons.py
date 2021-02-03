import pygame

#====================== Classe gérant les sons de l'application ===========================#
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class SoundManager:
    def __init__(self):
        self.sounds = {
            'loose': pygame.mixer.Sound(resource_path('ressources/loose.mp3')),
            'vent': pygame.mixer.Sound(resource_path('ressources/vent.wav')),
            'hajime': pygame.mixer.Sound(resource_path('ressources/hajime.wav')),
            'banzai': pygame.mixer.Sound(resource_path('ressources/banzai.wav')),
            'seppuku': pygame.mixer.Sound(resource_path('ressources/seppuku.wav')),
            'click': pygame.mixer.Sound(resource_path('ressources/click.wav'))
        }

#====================== Methode jouant un son 1000 fois (musique de fond pendant la partie) ===========================#

    def playXTime(self, name):
        self.sounds[name].play(1000).set_volume(0.2)

#====================== Methode jouant un son une fois ===========================#

    def playOneTime(self, name):
        self.sounds[name].play().set_volume(0.3)