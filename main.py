import pygame
import random
from bullet import Bullet
from enemy import Enemy

pygame.init()
screenWidth = 900
screenHeight = 700
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)
background = pygame.image.load("images/background.jpg")

# Player
playerImg = pygame.image.load("images/player.png")
playerX = 417
playerY = 600
playerChangeX = 0



def player(x, y):
    screen.blit(playerImg, (x, y))




# Enemy
enemyImg = pygame.image.load("images/ufo.png")
enemyX = random.randint(30, 800)
enemyY = random.randint(30, 200)
enemySpeed = 0.3

enemy=Enemy(enemyX, enemyY, enemySpeed, enemyImg)


#def enemy(x, y):
   #screen.blit(enemyImg, (x, y))


# Bullets
bullets=[]


# Collision Rects

enemy_rect = enemyImg.get_rect()
enemy_rect.topleft = (enemyX, enemyY)


# Game loop
running = True
while running:
    screen.fill((50, 100, 200))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard Input
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                playerChangeX -= 1
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                playerChangeX += 1
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet(playerX, playerY))

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d):
                playerChangeX = 0

    if screenWidth - 64 > playerX + playerChangeX > 0:
        playerX += playerChangeX

    # if enemyX + enemySpeed > 0:
    #     enemyX += enemySpeed
    # else:
    #     enemySpeed *= -1
    #     enemyY += 10

    # if enemyX + enemySpeed < screenWidth - 64:
    #     enemyX += enemySpeed
    # else:
    #     enemySpeed *= -1
    #     enemyY += 10

    # enemy_rect.topleft = (enemyX, enemyY)
   
    for b in bullets:
        b.move()
        b.draw(screen)
        if b.check_collision(enemy.rect):
            print("Bullet hit the enemy!")
            bullets.remove(b)
    

    
        
    bullets = [b for b in bullets if b.y > 0]

    player(playerX, playerY)
    enemy.draw(screen)
    enemy.move(screenWidth)
    pygame.display.update()
