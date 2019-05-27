# define some colors
import pygame as PG
from pygame import *
from pygame.locals import *
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# GAME settings
WIDTH = 1024 # divisible by 16, 32, and 64
HEIGHT = 768  # divisible by 16, 32 and 64
FPS = 60
TITLE = "TileMap"
BGCOLOR = LIGHTGREY
TILESIZE = 24
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


# player settings
PLAYER_SPEED = TILESIZE * 10
JUMP_SPEED = PLAYER_SPEED * 4
GRAVITY = PLAYER_SPEED / 10 + 13

PLAYER_IMG = 'player1.png'
WALL_IMG = 'wall.png'
LAVA_IMG = 'lava.png'
