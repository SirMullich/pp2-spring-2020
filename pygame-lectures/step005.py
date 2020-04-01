#!/usr/bin/env python
"""
005_bouncing_ball_frame_based.py
bouncing ball and pulsating circle
url: http://thepythongamebook.com/en:part2:pygame:step005
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html

works with python3.4 and python2.7

bouncing ball. each frame the complete screen is filled with the background,
making this example simple to code but possible slow on larger resolutions.
Each frame, a random-coloured circle is drawn with randomized radius directly on the screen.
Try to manipulate the display.set_mode values to change the resolution."""


import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

background = background.convert()

screen.blit(background, (0, 0))

ballsurface = pygame.Surface((50, 50))
ballsurface.set_colorkey((0, 0, 0))

ballsurface = ballsurface.convert()

ballrect = ballsurface.get_rect() # rectangle of the ball surface

ballx, bally = 100, 100 # start position
dx = 10 # will be used to change position of X
dy = 0

running = True
FPS = 30
clock = pygame.time.Clock()

while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


    if ballx > 640:
        dx = -dx
    elif ballx < 0:
        dx = -dx # -10 -> 10

    ballx = ballx + dx    # if dx -10    ballx 700 -> ballx 690
    bally = bally + dy

    screen.blit(background, (0, 0))

    pygame.draw.circle(screen, (255, 255, 0), (ballx, bally), 25)

    # screen.blit(ballsurface, ballx, bally)

    pygame.display.flip()







pygame.quit()