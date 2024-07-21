#!/usr/bin/env python
import random, pygame, sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
#init screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#clock to keep track of framerate
clock = pygame.time.Clock()

#constants for square
x = 400
y = 300
wl = 20
color = (255,0,0) #the squares color
background = (0,0,0) #our black background color
delta = 5 #How far to move square

screen.fill( background )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= delta
    if keys[pygame.K_DOWN]:
        y += delta
    if keys[pygame.K_LEFT]:
        x -= delta
    if keys[pygame.K_RIGHT]:
        x += delta

    screen.fill(background)
    pygame.draw.rect( screen, color, (x,y,wl,wl), 0)
    pygame.display.update()
    clock.tick(30)
