import math
import re
import random
from typing import List, Tuple

ITER = 100
random_list = []

def get_seed():
	seed = '|'
	for i in range(0, ITER):
		test = [
			random.randint(1, 8), # height
			random.randint(500, 2000), # width_x
			random.randint(500, 2000), # width_y
			random.randint(1, 2), # height_around
			random.randint(10000, 200000), # width_x_around
			random.randint(10000, 200000), # width_y_around
			random.randint(0, 1000), # offset_x
			random.randint(0, 1000), # offset_y
		]
		seed += ':'.join(f'{x:0>5X}' for x in test)
		seed += '|'
	
	return seed

def load_seed(seed: str):
	global random_list

	random_list = []
	matches = re.findall(r'|[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+|', seed)
	for matche in matches:
		if not matche:
			continue
		params = re.findall(r'[0-9A-F]+', matche)
		random_list.append([
			int(params[0], 16), # height
			1/int(params[1], 16), # width_x
			1/int(params[2], 16), # width_y
			int(params[3], 16), # height_around
			1/int(params[4], 16), # width_x_around
			1/int(params[5], 16), # width_y_around
			int(params[6], 16) - 500, # offset_x
			int(params[7], 16) - 500, # offset_y
			int(params[1], 16), # Value for cos
			int(params[2], 16), # Value for cos
			int(params[4], 16), # Value for cos2
			int(params[5], 16), # Value for cos2
		])
	
def _gausse2d(height, width_x, width_y, offset_x, offset_y, coordinates):
	return height * math.pow(2, width_x * -math.pow(coordinates[0] + offset_x, 2) - width_y * math.pow(coordinates[1] + offset_y, 2))

def get_height(coord: Tuple[int, int]):
	global random_list

	res = 0
	for ran in random_list:
		res += _gausse2d(ran[0], ran[1], ran[2], ran[6], ran[7], coord)
		res += _gausse2d(ran[3], ran[4], ran[5], ran[6], ran[7], coord)
	res -= 32
	return int(res)

def random_cos(coord: Tuple[int, int]):
	res = 0
	for elem in random_list:
		res += math.cos((coord[0] + elem[6]) * elem[10]) \
			+ math.cos((coord[1] + elem[7]) * elem[11])
	return int(res * 3) % 100

def random_cos2(coord: Tuple[int, int]):
	res = 0
	for elem in random_list:
		res += math.cos((coord[0] - elem[6]) * elem[8]) \
			+ math.cos((coord[1] - elem[7]) * elem[9])
	return int(res * 3) % 100