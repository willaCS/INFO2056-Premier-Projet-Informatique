import math
import re
import random
from typing import List, Tuple

ITER = 100
random_list = []

def get_seed():
	return random.randint(0, 0x7fffffff)

def load_seed(seed: int):
	global random_list

	random_list = []
	for i in range(0, ITER):
		random_list.append([
			  int(random_lcg(i * 8 + seed + 0) * 8 + 1), # height
			1/int(random_lcg(i * 8 + seed + 1) * 2000 + 500), # width_x
			1/int(random_lcg(i * 8 + seed + 2) * 2000 + 500), # width_y
			  int(random_lcg(i * 8 + seed + 3) * 2 + 1), # height_around
			1/int(random_lcg(i * 8 + seed + 4) * 200000 + 10000), # width_x_around
			1/int(random_lcg(i * 8 + seed + 5) * 200000 + 10000), # width_y_around
			  int(random_lcg(i * 8 + seed + 6) * 1000 - 500), # offset_x
			  int(random_lcg(i * 8 + seed + 7) * 1000 - 500), # offset_y
		])
	# print(random_list)``
	for i in random_list:
		print(i[0])

	# random_list = []
	# matches = re.findall(r'|[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+|', seed)
	# for matche in matches:
	# 	if not matche:
	# 		continue
	# 	params = re.findall(r'[0-9A-F]+', matche)
	# 	random_list.append([
	# 		int(params[0], 16), # height
	# 		1/int(params[1], 16), # width_x
	# 		1/int(params[2], 16), # width_y
	# 		int(params[3], 16), # height_around
	# 		1/int(params[4], 16), # width_x_around
	# 		1/int(params[5], 16), # width_y_around
	# 		int(params[6], 16) - 500, # offset_x
	# 		int(params[7], 16) - 500, # offset_y
	# 		int(params[1], 16), # Value for cos
	# 		int(params[2], 16), # Value for cos
	# 		int(params[4], 16), # Value for cos2
	# 		int(params[5], 16), # Value for cos2
	# 	])
	
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

# Park & Miller constants for random number generator
M = 0x7fffffff
A = 48271

NB_ITERATIONS = 10


# Type of linear congruential generator presented by D. H. lehmer
def random_lcg(n: int):
	n = n % (M - 1) + 1

	# Iteration with only x
	iteration = NB_ITERATIONS
	while (iteration > 0):
		n = n * A % M
		iteration -= 1
	return n / M

def random_lcg2(n: int):
	# Iteration with only x
	iteration = NB_ITERATIONS
	while (iteration > 0):
		n = n * A % M
		iteration -= 1
	return n


# Type of linear congruential generator presented by D. H. lehmer
# We use the x as the seed (x_0) for the first batch of
# iterations. After that, we use that result in combination with a XOR of it
# and y to be the seed of our second set of iterations.
# Thanks to Prof. Boigelot for the suggestion
def random_lcg_coord(coord: Tuple[int, int]):
    # Send all number to the interval ]0, M[
	x_val = coord[0] % (M - 1) + 1
	
	# Iteration with only x
	iteration = NB_ITERATIONS
	while (iteration > 0):
		x_val = x_val * A % M
		iteration -= 1
	
	y_val = x_val ^ coord[1]
	# Iteration with y
	iteration = NB_ITERATIONS
	while (iteration > 0):
		y_val = y_val * A % M
		iteration -= 1

	# Return value between 0 and 1
	return y_val / M


