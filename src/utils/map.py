"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

import math
from typing import Tuple
import random

from globals import Cursor, Zoom
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
ITER = 16

test_point_list = []
SEA_CIRCLE = 6

def init_random():
	global random_list

	random.seed()
	random_list = [[random.randint(1, i * 3) for j in range(3)] for i in range(1, ITER + 1)]
	print(random_list)
	for i in range(-SEA_CIRCLE, SEA_CIRCLE + 1):
		for j in range(-SEA_CIRCLE, SEA_CIRCLE + 1):
			if math.pow(i, 2) + math.pow(j, 2) <= math.pow(SEA_CIRCLE, 2):
				test_point_list.append((i, j))
	print(test_point_list)

cache_temp = {}

def random_test2(coord: Tuple[int, int]):
	global cache_temp, random_list
	if not cache_temp.get(coord):
		res = 0
		for elem in random_list:
			res += elem[0] * math.cos(elem[1] * coord[0] + elem[2] * coord[1])
		cache_temp[coord] = res
	return cache_temp.get(coord)

AVERAGE_OUTSIDE = 1

cache_temp2 = {}

def random_test(coord: Tuple[int, int]):
	global cache_temp2, random_list, test_point_list

	if not cache_temp2.get(coord):
		nb_water = 0
		# for test in test_point_list:
		# 	val = random_test2((coord[0] + test[0], coord[1] + test[1]))
		# 	if (val % 2 > 1.99):
		# 		nb_water += 1

		res = random_test2(coord) / 50000000000000
		if (res % 2 > 1.99999999999):
			res = 0
		# else:
		cache_temp2[coord] = res

	return cache_temp2.get(coord)
