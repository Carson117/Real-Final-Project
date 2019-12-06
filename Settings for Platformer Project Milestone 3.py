# game options/settings
TITLE = "Platformer"
WIDTH = 480# window size
HEIGHT = 600 # window size
FPS = 60 # smooth movement
FONT_NAME = "arial"

# player properties
PLAYER_ACC = 0.5 # player acceleration
PLAYER_FRICTION = -0.12 # player friction
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20 # Player jump height

# Starting platfroms
PLATFORM_LISTS = [(0, HEIGHT - 40, WIDTH, 40),
                (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                (125, HEIGHT - 350, 100, 20),
                (350, 200, 100, 20),
                (175, 100, 50, 20)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
TEAL = (0, 255, 0)
BGCOLOR = LIGHTBLUE
