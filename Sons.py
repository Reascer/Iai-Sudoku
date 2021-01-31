import pygame

#====================== Classe gérant les sons de l'application ===========================#

class SoundManager:
    def __init__(self):
        self.sounds = {
            'loose': pygame.mixer.Sound('ressources/loose.mp3'),
            'vent': pygame.mixer.Sound('ressources/vent.wav'),
            'hajime': pygame.mixer.Sound('ressources/hajime.wav'),
            'banzai': pygame.mixer.Sound('ressources/banzai.wav'),
            'seppuku': pygame.mixer.Sound('ressources/seppuku.wav'),
            'click': pygame.mixer.Sound('ressources/click.wav')
        }

#====================== Methode jouant un son 1000 fois (musique de fond pendant la partie) ===========================#

    def playXTime(self, name):
        self.sounds[name].play(1000).set_volume(0.2)

#====================== Methode jouant un son une fois ===========================#

    def playOneTime(self, name):
        self.sounds[name].play().set_volume(0.3)