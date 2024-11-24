"""
Ce fichier gère la vitesse de simulation du jeu.
"""

from math import inf


__prev_val = 3
val = 3
tick_index = 0
_delta_tick_simation = 10

# action by the player to increase the speed of the simulation
def increment():
	global val
	if val < 5:
		val += 1
		_update_tick_simulation()

# action by the player to decrease the speed of the simulation
def decrement():
	global val
	if val > 1:
		val -= 1
		_update_tick_simulation()

# action by the player to set the speed of the simulation
def set(new_speed: int):
	global val
	val = new_speed
	_update_tick_simulation()

# action by the player to pause the simulation
def pause():
	global val, __prev_val
	if (val != 0):
		__prev_val = val
		val = 0
	else:
		val = __prev_val
	_update_tick_simulation()

def can_execute_simulation():
	global tick_index
	tick_index += 1
	if (tick_index > _delta_tick_simation):
		tick_index = 0
		return True
	return False

def _update_tick_simulation():
	global _delta_tick_simation
	match val:
		case 0:
			_delta_tick_simation = inf
		case 1:
			_delta_tick_simation = 32
		case 2:
			_delta_tick_simation = 16
		case 3:
			_delta_tick_simation = 4
		case 4:
			_delta_tick_simation = 2
		case 5:
			_delta_tick_simation = 1
		case _:
			pass
