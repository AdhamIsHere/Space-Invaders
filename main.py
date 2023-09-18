import pygame
import random
from bullet import Bullet
from enemy import Enemy
from pygame import mixer
from sound_effects import SoundEffects

# pygame
pygame.init()
screenWidth = 900
screenHeight = 700
screen = pygame.display.set_mode((screenWidth, screenHeight))
paused = False

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
score=0

# Sounds
sounds=SoundEffects()
sounds.loopMusic()

font = pygame.font.Font("freesansbold.ttf",24)
def showScore():
    txt = font.render("Score: "+str(score),True,(255,255,255))
    screen.blit(txt,(10,10))
   



def player(x, y):
    screen.blit(playerImg, (x, y))




# Enemy
enemyImg = pygame.image.load("images/ufo.png")
enemyX = 834
enemyY = 100
enemySpeed = -0.3
#enemy=Enemy(enemyX, enemyY, enemySpeed, enemyImg)

enemies=[]

def generate_enemy_position():
    while True:
        x = random.randint(40, 800)
        if all(abs(x - e.x) > 64 for e in enemies):  # Check if new enemy position doesn't overlap with existing enemies
            return x

for i in range(10):
    enemies.append(Enemy(i*100, enemyY, enemySpeed, enemyImg))
def bounce():
    global playerY, is_bouncing
    playerY =620
    is_bouncing = True
    pygame.time.set_timer(pygame.USEREVENT, 50)

# Bullets
bullets=[]




# Game loop
# ... (previous code)

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))
    # key=pygame.key.get_pressed()
    # if key == pygame.K_x:
    #     paused=not paused
    
  
    # Handle events
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_ESCAPE:
                paused=not paused
        if not paused:
            # Keyboard Input
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    playerChangeX += 1
                elif event.key == pygame.K_SPACE:
                    print("Space pressed")
                    bullets.append(Bullet(playerX, playerY))
                    sounds.playBullet()
                    bounce()
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    playerChangeX -= 1

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d):
                    playerChangeX = 0

            elif event.type == pygame.USEREVENT and is_bouncing:
                playerY = 600
                is_bouncing = False
    if not paused:
        if screenWidth - 64 > playerX + playerChangeX > 0:
            playerX += playerChangeX

        for b in bullets:
            b.move()
            b.draw(screen)

        for e in enemies:
            for b in bullets:
                if b.check_collision(e.rect):
                    bullets.remove(b)
                    enemies.remove(e)
                    score += 1
                    enemies.append(Enemy(enemyX, enemyY, enemySpeed, enemyImg))
                    enemies.append(Enemy(enemyX - 80, enemyY, enemySpeed, enemyImg))

        bullets = [b for b in bullets if b.y > 0]
        showScore()
        player(playerX, playerY)
        for e in enemies:
            e.draw(screen)
            e.move(screenWidth)
                

    if paused:
        # Display pause screen or menu
        font = pygame.font.Font(None, 36)
        text = font.render("PAUSED", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screenWidth // 2, screenHeight // 2))
        screen.blit(text, text_rect)
    pygame.display.update()    