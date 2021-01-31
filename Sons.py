import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            'loose': pygame.mixer.Sound('ressources/loose.mp3'),
            'vent': pygame.mixer.Sound('ressources/vent.wav')
        }

    def playXTime(self, name):
        self.sounds[name].play(1000)

    def playOneTime(self, name):
        self.sounds[name].play()