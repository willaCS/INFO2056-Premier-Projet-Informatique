import math
import random
from typing import List
from utils.mytyping import utils_myTyping_coord_i

model_terrain_seed_ITER = 100
model_terrain_seed_random_list: List[List[int | float]] = []
model_terrain_seed_prev_random_val = 0

def model_terrain_seed_get_seed():
	global model_terrain_seed_prev_random_val
	model_terrain_seed_prev_random_val = random.randint(0, 0x7fffffff)
	return model_terrain_seed_prev_random_val

def model_terrain_seed_load_seed():
	global model_terrain_seed_random_list

	model_terrain_seed_random_list = []
	for i in range(0, model_terrain_seed_ITER): # type: ignore
		model_terrain_seed_random_list.append([
			int(model_terrain_seed_random_lcg() * 7 + 1), # height
			1/int(model_terrain_seed_random_lcg() * 200 + 500), # width_x
			1/int(model_terrain_seed_random_lcg() * 200 + 500), # width_y
			int(model_terrain_seed_random_lcg() * 2 + 1), # height_around
			1/int(model_terrain_seed_random_lcg() * 20000 + 10000), # width_x_around
			1/int(model_terrain_seed_random_lcg() * 20000 + 10000), # width_y_around
			int(model_terrain_seed_random_lcg() * 400 - 200), # offset_x
			int(model_terrain_seed_random_lcg() * 400 - 200), # offset_y
		])

def model_terrain_seed__gausse(height: int, width_x: float, width_y: float, offset_x: int, offset_y: int, coordinates: utils_myTyping_coord_i):
	return height * math.pow(2, width_x * -math.pow(coordinates[0] + offset_x, 2) - width_y * math.pow(coordinates[1] + offset_y, 2))

def model_terrain_seed__gausse2d(coordinates: utils_myTyping_coord_i, random: List[int | float]):
	return model_terrain_seed__gausse(random[0], random[1], random[2], random[6], random[7], coordinates)\
		+ model_terrain_seed__gausse(random[3], random[4], random[5], random[6], random[7], coordinates)


def model_terrain_seed_get_height(coord: utils_myTyping_coord_i):
	global model_terrain_seed_random_list

	if coord[0] > 500 or coord[1] > 500 or coord[0] < -500 or coord[1] < -500:
		return -31

	res = 0
	for ran in model_terrain_seed_random_list:
		res += model_terrain_seed__gausse2d(coord, ran)
	res -= 32
	return int(res)


# Park & Miller constants for random number generator
model_terrain_seed_M = 0x7fffffff
model_terrain_seed_A = 48271

model_terrain_seed_NB_ITERATIONS = 10


# Type of linear congruential generator presented by D. H. lehmer
def model_terrain_seed_random_lcg():
	global model_terrain_seed_prev_random_val
	n = model_terrain_seed_prev_random_val % (model_terrain_seed_M - 1) + 1

	# Iteration with only x
	iteration = model_terrain_seed_NB_ITERATIONS
	while (iteration > 0):
		n = n * model_terrain_seed_A % model_terrain_seed_M
		iteration -= 1

	model_terrain_seed_prev_random_val = n
	return n / model_terrain_seed_M	


# Type of linear congruential generator presented by D. H. lehmer
# We use the x as the seed (x_0) for the first batch of
# iterations. After that, we use that result in combination with a XOR of it
# and y to be the seed of our second set of iterations.
# Thanks to Prof. Boigelot for the suggestion
def model_terrain_seed_random_lcg_coord(coord: utils_myTyping_coord_i):
    # Send all number to the interval ]0, M[
	x_val = coord[0] % (model_terrain_seed_M - 1) + 1
	
	# Iteration with only x
	iteration = model_terrain_seed_NB_ITERATIONS
	while (iteration > 0):
		x_val = x_val * model_terrain_seed_A % model_terrain_seed_M
		iteration -= 1
	
	y_val = x_val ^ coord[1]

	# Iteration with y
	iteration = model_terrain_seed_NB_ITERATIONS
	while (iteration > 0):
		y_val = y_val * model_terrain_seed_A % model_terrain_seed_M
		iteration -= 1

	# Return value between 0 and 1
	return y_val / model_terrain_seed_M


