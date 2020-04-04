"""
006_time_baed_movement.py
url: http://thepythongamebook.com/en:part2:pygame:step006
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html

works with python3.4 and pyhton2.7

bouncing ball. Movement is now time based.
Because at coding, you never know exactly how many milliseconds
will have been passed between two frames, this example use pygame's
clock function to calculate the passed time and move the ballsurface at
constantly the same speed.
If you toggle the wild circle painting by pressing SPACE, the computer
has more to paint, framerate will drop, more time will pass between
2 frames and movement of the ball surface will be choppy (less smooth).
However, the movent speed remain unchanged because of the time-based movement.
"""

import pygame
import random

def wildPainting():
    pygame.draw.circle(background, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                       (random.randint(0, screenrect.width), random.randint(0, screenrect.height)),
                       random.randint(50, 500))

pygame.init()
screen = pygame.display.set_mode((640, 480))
screenrect = screen.get_rect()
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255)) # white
background = background.convert() # background surface is ready to be blit
background2 = background.copy() # always WHITE and used for blitting white background

ballsurface = pygame.Surface((50, 50))
ballrect = ballsurface.get_rect() # to use rectrangle's height&width
ballsurface.set_colorkey((0, 0, 0))

pygame.draw.circle(ballsurface, (0, 0, 255), (25, 25), 25)
ballsurface = ballsurface.convert_alpha() # ballsurface is ready to be blit

ballx, bally = 550, 240 # position of ballsurface on the screen
dx, dy = 60, 50

screen.blit(background, (0, 0))
screen.blit(ballsurface, (ballx, bally))

clock = pygame.time.Clock()
running = True
FPS = 30
playtime = 0 # used in text in caption
paint_big_circles = False
cleanup = True # blit background in main loop

while running:
    milliseconds = clock.tick(FPS)
    seconds = milliseconds / 1000.0
    playtime = playtime + seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_1:
                FPS = 2
            elif event.key == pygame.K_2:
                FPS = 20
            elif event.key == pygame.K_3:
                FPS = 30
            elif event.key == pygame.K_4:
                FPS = 40
            elif event.key == pygame.K_5:
                FPS = 50
            elif event.key == pygame.K_6:
                FPS = 60
            elif event.key == pygame.K_7:
                FPS = 70
            elif event.key == pygame.K_8:
                FPS = 80
            elif event.key == pygame.K_9:
                FPS = 90
            elif event.key == pygame.K_0:
                FPS = 100
            elif event.key == pygame.K_x:
                paint_big_circles = not paint_big_circles
            elif event.key == pygame.K_y:
                cleanup = not cleanup # True -> False; False -> True
            elif event.key == pygame.K_w:
                background.blit(background2, (0, 0))

    pygame.display.set_caption("x: paint({}) y: cleanup ({}) ,"
                               " w: white, 0-9: limit FPS to {}"
                               " (now: {:.2f}".format(paint_big_circles, cleanup, FPS, clock.get_fps()))

    if cleanup:
        screen.blit(background, (0, 0))
    if paint_big_circles:
        wildPainting()

    ballx = ballx + dx * seconds
    bally = bally + dy * seconds

    # check if the ball is outside of the screen
    if ballx < 0:
        ballx = 0
        dx = dx * -1
    elif ballx + ballrect.width > screenrect.width:
        ballx = screenrect.width - ballrect.width
        dx = dx * -1

    if bally < 0:
        bally = 0
        dy = dy * -1
    elif bally + ballrect.height > screenrect.height:
        bally = screenrect.height - ballrect.height
        dy = dy * -1

    screen.blit(ballsurface, (round(ballx, 0), round(bally, 0)))
    pygame.display.flip() # refresh the screen


pygame.quit()