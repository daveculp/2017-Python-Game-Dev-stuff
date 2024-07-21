#!/usr/bin/env python

import random, pygame, sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

screen.fill( (0,0,0) )
    
for pixel in range (0, 100000):
    start_x = random.randrange(0,SCREEN_WIDTH)
    start_y = random.randrange(0, SCREEN_HEIGHT)

    end_x = random.randrange(0,SCREEN_WIDTH)
    end_y = random.randrange(0, SCREEN_HEIGHT)


    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    pygame.draw.line(screen, (r,g,b), (start_x,start_y), (end_x,end_y), 5)
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
