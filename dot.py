#!/usr/bin/env python

import random, pygame, sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
#init screen
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
#clock to keep track of framerate
clock = pygame.time.Clock()

screen.fill( (255,128,64) )
screen.set_at( (400,300), (255,255,255) )
pygame.display.update()
