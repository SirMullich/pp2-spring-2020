"""
002_display_fps.py

Open a Pygame window and display framerate.
Program terminates by pressing the ESCAPE-Key.

works with python2.7 and python3.4

url: http://thepythongamebook.com/en:part2:pygame:step003
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

ballsurface = pygame.Surface((50, 50))
pygame.draw.circle(ballsurface, (0, 0, 255), (25, 25), 25)  # blue colored cirlce RGB -> (0, 0, 255)

running = True
FPS = 30
clock = pygame.time.Clock()

rect = pygame.Rect(350, 400, 100, 150)

pygame.draw.rect(background, (0, 255, 0), rect)
backgournd = background.convert()
ballsurface = ballsurface.convert()
screen.blit(background, (0, 0))
screen.blit(ballsurface, (50, 50))

while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()

pygame.quit()