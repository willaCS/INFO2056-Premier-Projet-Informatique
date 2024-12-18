import math
import random
from typing import List
from utils.mytyping import coord_i

ITER = 100
random_list: List[List[int | float]] = []
prev_random_val = 0

def get_seed():
	global prev_random_val
	prev_random_val = random.randint(0, 0x7fffffff)
	return prev_random_val

def load_seed():
	global random_list

	random_list = []
	for i in range(0, ITER): # type: ignore
		random_list.append([
			int(random_lcg() * 7 + 1), # height
			1/int(random_lcg() * 200 + 500), # width_x
			1/int(random_lcg() * 200 + 500), # width_y
			int(random_lcg() * 2 + 1), # height_around
			1/int(random_lcg() * 20000 + 10000), # width_x_around
			1/int(random_lcg() * 20000 + 10000), # width_y_around
			int(random_lcg() * 400 - 200), # offset_x
			int(random_lcg() * 400 - 200), # offset_y
		])

def _gausse(height: int, width_x: float, width_y: float, offset_x: int, offset_y: int, coordinates: coord_i):
	return height * math.pow(2, width_x * -math.pow(coordinates[0] + offset_x, 2) - width_y * math.pow(coordinates[1] + offset_y, 2))

def _gausse2d(coordinates: coord_i, random: List[int | float]):
	return _gausse(random[0], random[1], random[2], random[6], random[7], coordinates)\
		+ _gausse(random[3], random[4], random[5], random[6], random[7], coordinates)


def get_height(coord: coord_i):
	global random_list

	if coord[0] > 500 or coord[1] > 500 or coord[0] < -500 or coord[1] < -500:
		return -31

	res = 0
	for ran in random_list:
		res += _gausse2d(coord, ran)
	res -= 32
	return int(res)


# Park & Miller constants for random number generator
M = 0x7fffffff
A = 48271

NB_ITERATIONS = 10


# Type of linear congruential generator presented by D. H. lehmer
def random_lcg():
	global prev_random_val
	n = prev_random_val % (M - 1) + 1

	# Iteration with only x
	iteration = NB_ITERATIONS
	while (iteration > 0):
		n = n * A % M
		iteration -= 1

	prev_random_val = n
	return n / M	


# Type of linear congruential generator presented by D. H. lehmer
# We use the x as the seed (x_0) for the first batch of
# iterations. After that, we use that result in combination with a XOR of it
# and y to be the seed of our second set of iterations.
# Thanks to Prof. Boigelot for the suggestion
def random_lcg_coord(coord: coord_i):
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


