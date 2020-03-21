[200~"""
        002_display_fps.py

        Open a Pygame window and display framerate.
        Program terminates by pressing the ESCAPE-Key.
         
         works with python2.7 and python3.4 

         URL    : http://thepythongamebook.com/en:part2:pygame:step002
         Author : horst.jens@spielend-programmieren.at
         License: GPL, see http://www.gnu.org/licenses/gpl.html
         """

         import pygame

         pygame.init()

         # window = screen
         screen = pygame.display.set_mode((640, 480))

         # draw = blit (put a surface on a screen)
         background = pygame.Surface(screen.get_size())

         background.fill((255, 255, 255)) # rgb - white color -> RGB 255, 255, 255
         background = background.convert() # to make blit faster

         screen.blit(background, (0, 0)) # position - 0, 0

         clock = pygame.time.Clock()

         # infinite loop
         running = True
         FPS = 30
         playtime = 0.0 # in seconds
         while running:
             milliseconds = clock.tick(FPS) # in milliseconds
                 playtime = playtime + milliseconds / 1000.0 # convert to seconds

                     # handle user input
                         for event in pygame.event.get():
                                 if event.type == pygame.QUIT:
                                             running = False
                                                     elif event.type == pygame.KEYDOWN: # user pressed a key
                                                                 if event.key == pygame.K_ESCAPE:
                                                                                 running = False

                                                                                     text = "FPS: {0:.1f}, Playtime: {1:.2f}".format(clock.get_fps(), playtime)
                                                                                         pygame.display.set_caption(text)

                                                                                             pygame.display.flip() # refreshes the display

pygame.quit()
