class Enemy:

    def __init__(self,x,y,speed,img):
        self.x = x
        self.y = y
        self.speed = speed
        self.img = img
        self.rect = self.img.get_rect()   
        self.rect.topleft=(self.x,self.y)


   
        

    def draw(self,screen):
        screen.blit(self.img, (self.x, self.y))
        
    def move(self,width):
        if self.x+self.speed > 0:
            self.x += self.speed
        else:
            self.speed *= -1
            self.y +=70

        if self.x+self.speed < width-64:
            self.x += self.speed
        else:
            self.speed *= -1
            self.y +=70
        self.rect.topleft=(self.x,self.y)