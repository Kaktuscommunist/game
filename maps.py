from setting import *

text_map = [
    'WWWWWWWWWWWWWW',
    'W............W',
    'W............W',
    'W............W',
    'W..WWWW.WW..WW',
    'W............W',
    'WWWWWWWWWWWWWW'
]
world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
