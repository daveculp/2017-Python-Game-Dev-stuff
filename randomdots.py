#!/usr/bin/env python

import random, pygame, sys

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200

pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

screen.fill( (0,0,0) )
    
for pixel in range (0, 1000000):
    x = random.randrange(0,SCREEN_WIDTH)
    y = random.randrange(0, SCREEN_HEIGHT)
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    screen.set_at( (x,y), (r,g,b) )
    #pygame.display.update()
#clock.tick(30)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
	pygame.display.update()
