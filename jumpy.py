###########Import #########
import pygame
import time
import random


White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Green=(0,255,0)
Blue=(0,0,255)
Yellow=(255,255,0)
fps=50

GameRun=True
While GameRun:
	clock.tick(fps)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd=False