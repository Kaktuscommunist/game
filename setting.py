# W w
import math

WIDTH = 1200
HEIGHT = 700
HALF_WIDTH = WIDTH // 5
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100  # масштаб
FPS_POS = (WIDTH - 65, 5)

# min maps
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

# ray casting_setting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 200
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player setting
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2  # скорость движения шарика

# color
WHITE = (255, 255, 255)
BLACK = (0, 10, 0)  # фон
GREEN = (80, 0, 100)  # шарик
DARKGRAY = (40, 50, 40)  # кубики
RED = (200, 0, 0)
BLUE = (0, 0, 220)
PYRPLE = (120, 0, 120)
SKYBLUE = (50, 200, 255)
YELLOW = (120, 120, 0)
