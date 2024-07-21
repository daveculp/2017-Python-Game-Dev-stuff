#!/usr/bin/env python

import random, pygame, sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    screen.fill( (0,0,0) )
    screen.set_at( (400,300), (255,255,255) )
    pygame.display.update()
    clock.tick(30)
