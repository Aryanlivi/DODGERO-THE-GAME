#########______IMPORTS________#################
import pygame
import time
import random
##########_____initialization________################
pygame.init()
pygame.font.init()
##############DISPLAY ROOT:
display_height=600
display_width=600
gameDisplay = pygame.display.set_mode((display_width,display_height))
##########BACKGROUND CLOUDS:
Back=pygame.image.load("Sprites\\clouds.png")
#########CAPTION :
pygame.display.set_caption("DODGERO THE GAME!")
######## for fps:
clock=pygame.time.Clock()
############for aeroplane sprite:
Aero_img=pygame.image.load("Sprites\\aeroplane.png")
Aero_width=128
Aero_height=128
############### GAME SPRITES:
def fireballs(fireballx, firebally, fireballw, fireballh):
    fireball=pygame.image.load("Sprites\\fire.gif")
    gameDisplay.blit(fireball, (fireballx, firebally))
#def fireballs2(fireball2x, fireball2y, fireball2w, fireball2h):
#    fireball2=pygame.image.load("C:\\Users\\Aryan\\Desktop\\fireball2.png")
 #   gameDisplay.blit(fireball2, (fireball2x, fireball2y))
def aeros(x,y):
    gameDisplay.blit(Aero_img, (x, y))
#######################################################:)
def collision(ax, ay, aw, ah, bx, by, bw, bh):
    return ax < bx+bw and ay < by+bh and bx < ax+aw and by < ay+ah

def fireballs_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, (0,0,0))
    gameDisplay.blit(text,(0,0))

#########for msg display :(both text_objects nd message display FUNC):
def text_objects(text,font):
    Textsurf=font.render(text,True,(0,0,0))
    return Textsurf,Textsurf.get_rect()
def message_display(text):
    The_text=pygame.font.Font("freesansbold.ttf",40)
    Textsurf , Textbox=text_objects(text,The_text)
    Textbox.center=((display_width/2),(display_height/2))

    gameDisplay.blit(Textsurf,Textbox)
    pygame.display.update()
    time.sleep(2)
    gameloop()
### crash:
def crash():
    message_display("You Crashed!!")

######## GAME LOOP:
def gameloop():
########## definiing x and y for aeros:
    x=(display_width*0.40)
    y=(display_height*0.6)
############### aero movement value stored in x_change:
    x_change=0
    dodged=0


#######fireball 1 prop:
    fireball_height = 64
    fireball_width = 64
    fireball_startx = random.randrange(0, display_width)
    fireball_starty = -600
    fireball_speed = 4
######fireball 2 prop:
   #fireball2_height =128
   # fireball2_width = 128
   # fireball2_startx = random.randrange(0, display_width)
  #  fireball2_starty = -600
   # fireball2_speed = 7
########################################################################################
################# EVENT HANDLING::: ##################################################
    gameEnd = False
    a=1
    while not gameEnd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key== pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x +=x_change
        ##########"BACKGROUND Blit:
        gameDisplay.blit(Back,(0,0))
        ##########
        ################# ##FIREBALL 1 Movement
        fireballs(fireball_startx, fireball_starty,fireball_width ,fireball_height)
        fireball_starty += fireball_speed
        ############FIREBALL 2 Movement
       # fireballs2(fireball2_startx, fireball2_starty, fireball2_width, fireball2_height)
     #   fireball2_starty += fireball2_speed
        ###"aeros function call:
        aeros(x,y)
        fireballs_dodged(dodged)
        ############################"SIDE BOUNDARIES CRASH:
        if x>display_width-Aero_width or x<0:
            crash()
        #####################"FIREBALL Movement
        if fireball_starty > display_height:
            fireball_starty = 0 - fireball_height
            fireball_startx = random.randrange(0, display_width)
            dodged +=1
            fireball_speed +=0.5
        pygame.display.update()
        if collision(x, y, Aero_width, Aero_height, fireball_startx, fireball_starty, fireball_width,
                     fireball_height):
            crash()
        ##############3###"FIREBALL2 Movement"
      #  if fireball2_starty > display_height:
        #    fireball2_starty = 0 - fireball2_height
         #   fireball2_startx = random.randrange(0, display_width)
      #  pygame.display.update()
        ############################"CRASH TYPE 1"##################################################
        #if y < fireball_starty + fireball_height:
         #   print('y crossover')

          #  if (x > fireball_startx and x < fireball_startx + fireball_width or x + fireball_width > fireball_startx
        #  and x + fireball_width < fireball_startx + fireball_width):
           #     print('x crossover')
            #    crash()

        ##################################################"CRASH TYPE 2"###############################################
        #if y < fireball2_starty + fireball2_height:
          #  print('y crossover1')
        #pygame.display.update()
        #if (x > fireball2_startx and x < fireball2_startx + fireball2_width or x + fireball2_width > fireball2_startx
         #       and x+ fireball2_width < fireball2_startx + fireball2_width):
         #   print('x crossover1')
         #   crash()
        ############################## "FOR GO IN THE BEGGINING"
        while a<2:
            font = pygame.font.Font("freesansbold.ttf", 66)
            text_surface = font.render("GO!", True, (0, 0, 0))
            gameDisplay.blit(text_surface, ((display_width * 0.45), (display_height * 0.4)))
            pygame.display.update()
            time.sleep(1)
            a=a+1
        ################################"clock.tick for fps"
        clock.tick(80)
#########"gameloop"
gameloop()
###################"quit func"
pygame.quit()
quit()
