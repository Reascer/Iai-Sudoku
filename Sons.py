import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            'loose': pygame.mixer.Sound('ressources/loose.mp3'),
            'vent': pygame.mixer.Sound('ressources/vent.wav'),
            'hajime': pygame.mixer.Sound('ressources/hajime.wav'),
            'banzai': pygame.mixer.Sound('ressources/banzai.wav'),
            'click': pygame.mixer.Sound('ressources/click.wav')
        }

    def playXTime(self, name):
        self.sounds[name].play(1000).set_volume(0.2)

    def playOneTime(self, name):
        self.sounds[name].play().set_volume(0.3)