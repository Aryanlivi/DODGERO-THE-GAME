#########______IMPORTS________#################
import pygame
import time
import random

White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Green=(0,255,0)
Blue=(0,0,255)
Yellow=(255,255,0)

Bkgd=pygame.image.load("Sprites\\The_road.png")  
fps=60

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        # this line is required to properly create the spritehe she s
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.image.load("Sprites\\car.png")
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        self.radius=int(self.rect.width*.90/3.0)
       # pygame.draw.circle(self.image,Red,self.rect.center,self.radius)
        # center the sprite on the screen
        self.rect.center = (display_width* 0.45, display_height *0.8)
        self.speedx=0
        self.speedy=0


    def update(self):
        # any code here will happen every time the game loop updates
        self.speedx=0
        self.speedy=0

        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -9
        if  keystate[pygame.K_RIGHT]:
            self.speedx=9
        if keystate[pygame.K_UP]:
            self.speedy = -2.5
        if  keystate[pygame.K_DOWN]:
            self.speedy=4

        if self.rect.right>display_width:
            self.rect.right=display_width
        if self.rect.left<0:
            self.rect.left=0

        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>display_height:
            self.rect.bottom=display_height
        self.rect.x+=self.speedx 
        self.rect.y+=self.speedy


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.car_dodged=0
        self.image=pygame.image.load("Sprites\\enemy_car.png")
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width*0.90/2.9)
       # pygame.draw.circle(self.image,Red,self.rect.center,self.radius)
        self.rect.x=random.randrange(0,display_width-self.rect.width)
        self.rect.y=random.randrange((-(display_height+55)),(-(display_height+50)))
        self.speedy=16
    def update(self):
        if self.rect.top>display_height+10:
            self.rect.x=random.randrange(0,display_width-self.rect.width)
            self.rect.y=random.randrange((-(display_height+55)),(-(display_height+50)))
            self.speedy+=3
            self.car_dodged+=1
            print(self.car_dodged)
        self.rect.y+=self.speedy




   

############################################################33      
#initialization
pygame.init()
pygame.font.init()
pygame.mixer.init()

##############DISPLAY ROOT:
display_height=600
display_width=570
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("DODGERO THE GAME!")

clock=pygame.time.Clock()
# all the class object :
User_Car=Player()
#E_fire=Enemy()
#alll sprites in this;
sprites=pygame.sprite.Group()
sprites.add(User_Car)
enemy_sprites=pygame.sprite.Group()
for i in range(3):
    fireball=Enemy()
    sprites.add(fireball)
    enemy_sprites.add(fireball)

#####

Back_y=0
gameEnd = True
Go_loop=1
pygame.mixer.music.load("Music\\Marimba Boy.wav")
pygame.mixer.music.play(-1)
while gameEnd: 
     ################################"clock.tick for fps"
    clock.tick(fps)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd=False
    

    crash=pygame.sprite.spritecollide(User_Car,enemy_sprites,False,pygame.sprite.collide_circle)
    if crash:
        
        gameEnd=False



    ##########"Bkgd Blit(scrool):
    rel_Back_y=Back_y%Bkgd.get_rect().height
    sprites.update()
    gameDisplay.blit(Bkgd,(0,((rel_Back_y-Bkgd.get_rect().height))))
    if rel_Back_y<display_height:
        gameDisplay.blit(Bkgd,(0,rel_Back_y))
    Back_y+=8

    sprites.draw(gameDisplay)
    while Go_loop<2:
        font = pygame.font.Font("freesansbold.ttf", 66)  
        text_surface = font.render("GO!", True, (0, 0, 0))
        gameDisplay.blit(text_surface, ((display_width * 0.45), (display_height * 0.4)))
        pygame.display.update()
        time.sleep(1)
        Go_loop=Go_loop+1
    pygame.display.flip()


pygame.quit()
