from pygame import mixer

class SoundEffects:
    def __init__(self):
        mixer.music.load("sounds/background-music.wav")
        self.bullet= mixer.Sound("sounds/laser.wav")
        self.explode= mixer.Sound("sounds/explosion.wav")

    def loopMusic(self):
        mixer.music.play(-1)
    
    def playBullet(self):
        self.bullet.play()
    def playExplode(self):
        self.explode.play()