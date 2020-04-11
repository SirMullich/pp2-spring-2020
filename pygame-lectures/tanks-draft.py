import pygame

class Tank:
    # speed instead of dx, dy
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = 1 # 1 - up, 2 - down, 3 - left, 4 - right

    def update_location(self, seconds):
        if self.direction == 1:
            self.y -= self.speed * seconds
        elif self.direction == 2:
            self.y += self.speed * seconds
        elif self.direction == 3:
            self.x -= self.speed * seconds
        elif self.direction == 4:
            self.x += self.speed * seconds

    def change_direction(self, direction):
        self.direction = direction

    def get_rect(self):
        return (self.x, self.y, self.width, self.height)


class SceneBase:
    def __init__(self):
        self.next = self

    def process_input(self, events):
        print("uh-oh, you didn't override this in the child class")

    def update(self, seconds):
        print("uh-oh, you didn't override this in the child class")

    def render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def switch_to_scene(self, next_scene):
        self.next = next_scene

# TitleScene is a subclass of SceneBase
# SceneBase is a parent of TitleScene
# TitleScene inherits from SceneBase
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(GameScene()) # create a new object GameScene

    def update(self, seconds):
        pass

    def render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.tank = Tank(100, 100, 50, 50, 80)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.tank.change_direction(1)
                elif event.key == pygame.K_DOWN:
                    self.tank.change_direction(2)
                elif event.key == pygame.K_LEFT:
                    self.tank.change_direction(3)
                elif event.key == pygame.K_RIGHT:
                    self.tank.change_direction(4)

    def update(self, seconds):
        self.tank.update_location(seconds)

    def render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))
        #draw tank (rect)
        pygame.draw.rect(screen, (0, 255, 0), self.tank.get_rect())


def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        milliseconds = clock.tick(fps)
        seconds = milliseconds / 1000.0

        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys) # handle input
        active_scene.update(seconds) # move tank
        active_scene.render(screen) # (re)draw the tank

        active_scene = active_scene.next # when RETURN is pressed in TitleScene, active_scene: TitleScene -> GameScene

        pygame.display.flip()


run_game(800, 600, 30, TitleScene())