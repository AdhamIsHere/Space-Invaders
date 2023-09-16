class Player:

    def __init__(self,x,y,img,speed):
        self.x = x
        self.y = y
        self.img = img
        self.speed = speed

    def draw(self,screen):
        screen.blit(self.img, (self.x, self.y))

    def moveX(self,x):
        self.x += x*self.speed
    
    def moveY(self,y):
        self.y += y*self.speed