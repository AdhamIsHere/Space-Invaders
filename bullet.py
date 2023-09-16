import pygame

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.image.load("images/bullet.png")
        self.rect = self.image.get_rect()

    def move(self):
        self.y -= self.speed
        self.rect.topleft = (self.x + 16, self.y - 10)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def check_collision(self, enemy_rect):
        return self.rect.colliderect(enemy_rect)
