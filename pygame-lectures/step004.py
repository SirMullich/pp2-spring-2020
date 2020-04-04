"""
004_colorkey.py
dynamic blitting and colorkey
url: http://thepythongamebook.com/en:part2:pygame:step004
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html

Blitting one surface on 2 static positions, once before the
mainloop and once inside the mainloop.
using colorkey to make a part of the surfaces tranparent
blitting lines on the screen to create a colourful pattern
like in a screensaver
"""


import pygame
import random

pygame.init()

screen = pygame.display.set_mode((640, 480))  # 640 / 20 = 32, 480 / 20 = 24
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
background = background.convert()

ballsurface = pygame.Surface((50, 50))
ballsurface.set_colorkey((0, 0, 0)) # black will be transparent

pygame.draw.circle(ballsurface, (0, 0, 255), (25, 25), 25)
ballsurface = ballsurface.convert()

screen.blit(background, (0, 0))
ballx = 20
bally = 240

screen.blit(ballsurface, (ballx, bally))

ballx2 = 400
bally2 = 380

clock = pygame.time.Clock()
running = True

FPS = 30
color1 = 0 # to draw lines later
color2 = 0 # to draw lines later

t = 0 # 0 -> 20

while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # user pressed [X] button
            running = False
        elif event.type == pygame.KEYDOWN: # user pressed some key
            if event.key == pygame.K_ESCAPE:
                running = False

    # blit (draw) lines
    pygame.draw.line(screen, (color1, 255 - color1, color2), (32 * t, 0), (0, 480 - 24 * t))
    pygame.draw.line(screen, (255 - color2, color2, color1), (32 * t, 480), (640, 480 - 24 * t))

    screen.blit(ballsurface, (ballx2, bally2))

    t += 1
    if t > 20: # finished drawing all lines
        t = 0
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)

    pygame.display.flip()

pygame.quit()