from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32

_ = False
matrix_map = [

    [6,6,6,6,6,6,2,6,6,6,6,6,6,6,6],
    [5,_,_,_,_,_,_,6,_,_,_,_,_,_,1],
    [6,_,_,_,_,_,_,_,_,_,_,_,_,_,6],
    [6,_,_,6,6,6,_,_,_,6,_,_,_,_,6],
    [6,_,_,_,_,7,6,_,6,6,_,_,_,_,6],
    [6,_,_,6,_,6,_,_,6,_,_,_,_,_,4],
    [6,_,_,6,_,_,_,6,10,6,_,_,_,_,6],
    [8,_,_,_,_,_,_,_,_,_,_,_,_,_,6],
    [6,_,_,_,_,_,_,_,_,_,_,_,_,_,6],
    [6,_,_,_,_,6,_,_,_,_,_,_,_,_,6],
    [6,6,6,3,6,6,6,6,6,9,6,6,6,6,6]]



WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
mini_map = set()
collision_walls = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4
            elif char == 5:
                world_map[(i * TILE, j * TILE)] = 5
            elif char == 6:
                world_map[(i * TILE, j * TILE)] = 6
            elif char == 7:
                world_map[(i * TILE, j * TILE)] = 7
            elif char == 8:
                world_map[(i * TILE, j * TILE)] = 8
            elif char == 9:
                world_map[(i * TILE, j * TILE)] = 9
            elif char == 10:
                world_map[(i * TILE, j * TILE)] = 10
