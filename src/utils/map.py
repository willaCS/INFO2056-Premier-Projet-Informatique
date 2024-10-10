"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

import math
from sqlite3 import InternalError
from typing import Callable, Dict, Tuple
import random

from globals import Cursor, Zoom
from map import Map, TerrainTile, Tile
import Window

def coord_to_px(coord: Tuple[float, float]) -> Tuple[int, int]:
	return (
		Window.half_resolution[0] + int(Cursor.val[0] * Zoom.tile_size) + (coord[0]) * Zoom.tile_size,
		Window.half_resolution[1] - int(Cursor.val[1] * Zoom.tile_size) - (coord[1]) * Zoom.tile_size,
	)

def px_to_coord(coord: Tuple[int, int]) -> Tuple[float, float]:
	return (
		(coord[0] - Window.half_resolution[0]) / Zoom.tile_size - Cursor.val[0],
		-((coord[1] - Window.half_resolution[1]) / Zoom.tile_size + Cursor.val[1]),
	)

random_list = []
ITER = 128

test_point_list = []
SEA_CIRCLE = 2

def init_random():
	global random_list

	random.seed()
	random_list = []
	for i in range(1, ITER + 1):
		random_list.append([
			random.randint(i*4, i*4 + 10), random.randint(i*4, i*4 + 10), random.randint(i*4, i*4 + 10),
			random.randint(i*4, i*4 + 10), random.randint(i*4, i*4 + 10), random.randint(i*4, i*4 + 10),
			random.randint(i*2, i*2 + 10)
		])

	for i in range(-SEA_CIRCLE, SEA_CIRCLE + 1):
		for j in range(-SEA_CIRCLE, SEA_CIRCLE + 1):
			if math.pow(i, 2) + math.pow(j, 2) <= math.pow(SEA_CIRCLE, 2) - 0.5:
				test_point_list.append((i, j))
	print(test_point_list)

def create_caching_function(arg_func: Callable[[Tuple[int, int]], int]) -> Callable[[Tuple[int, int]], int]:
	cache: Dict[Tuple[int, int], int] = {}
	
	def test(coord: Tuple[int, int]):
		if not cache.get(coord):
			res = arg_func(coord)
			cache[coord] = res
		return cache.get(coord)

	return test


@create_caching_function
def random_terrain_landscape(coord: Tuple[int, int]) -> Dict[str, int | Tuple[int, int]]:
	height = 0
	for elem in random_list:
		height += (elem[0] * math.cos(coord[0] / elem[1] + elem[2])\
			- elem[3] * math.cos(coord[1] / elem[4] + elem[5])) / elem[6]
	
	if (height < -5):
		return TerrainTile.init(TerrainTile.TERRAINTILETYPE_DEEPSEA, coord, height)
	elif (height < 0):
		return TerrainTile.init(TerrainTile.TERRAINTILETYPE_SEA, coord, height)
	elif (height < 2):
		if 1.7 < random_terrain_ressource(coord) % 2 and random_terrain_ressource(coord) % 2 < 1.705:
			Map.add(Tile.init(Tile.TILETYPE_CITYCENTER, coord))
		return TerrainTile.init(TerrainTile.TERRAINTILETYPE_BEACH, coord, height)
	elif (height < 15):
		if 1.7 < random_terrain_ressource(coord) % 2 and random_terrain_ressource(coord) % 2 < 1.705:
			Map.add(Tile.init(Tile.TILETYPE_CITYCENTER, coord))
		return TerrainTile.init(TerrainTile.TERRAINTILETYPE_PLAIN, coord, height)
	elif (height < 25):
		return TerrainTile.init(TerrainTile.TERRAINTILETYPE_FOREST, coord, height)
	elif (height < 35):
		return TerrainTile.init(TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, coord, height)
	elif (height >= 35):
		return TerrainTile.init(TerrainTile.TERRAINTILETYPE_MOUNTAIN_TOP, coord, height)
	raise InternalError("Terrain tile has height not possible")

@create_caching_function
def random_terrain_ressource(coord: Tuple[int, int]) -> int:
	res = 0
	for elem in random_list:
		res += (elem[0] * math.cos(coord[0] * elem[1] + elem[2])\
			- elem[3] * math.cos(coord[1] * elem[4] + elem[5]))
	return res

@create_caching_function
def random_test(coord: Tuple[int, int]) -> int:
	test = random_terrain_ressource(coord)
	for test in test_point_list:
		test = random_terrain_ressource((coord[0] + test[0], coord[1] + test[1]))
		if (1.7 < test % 2 and test % 2 < 1.71):
			return True
	return False

