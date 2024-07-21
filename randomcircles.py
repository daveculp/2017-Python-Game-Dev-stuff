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
    
for pixel in range (0, 10000):
    x = random.randrange(0,SCREEN_WIDTH)
    y = random.randrange(0, SCREEN_HEIGHT)
    radius = random.randrange(0,25)

    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    pygame.draw.circle(screen, (r,g,b), (x,y), radius, 0)
    #pygame.display.update()
#clock.tick(30)
    
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
