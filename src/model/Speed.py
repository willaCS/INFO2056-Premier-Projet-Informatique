"""
Ce fichier gère la vitesse de simulation du jeu.
"""

from math import inf

from ui import gestionMenu


__prev_val = 3
val = 3
tick_index = 0
_delta_tick_simation = 10

# action by the player to increase the speed of the simulation
def model_speed_increment():
	global val
	if val < 5:
		val += 1
		model_speed__update_tick_simulation()

# action by the player to decrease the speed of the simulation
def model_speed_decrement():
	global val
	if val > 1:
		val -= 1
		model_speed__update_tick_simulation()

# action by the player to set the speed of the simulation
def model_speed_set(new_speed: int):
	global val
	val = new_speed
	model_speed__update_tick_simulation()

# action by the player to pause the simulation
def model_speed_pause():
	global val, __prev_val
	if (val != 0):
		__prev_val = val
		val = 0
	else:
		val = __prev_val
	model_speed__update_tick_simulation()

def model_speed_can_execute_simulation():
	global tick_index
	tick_index += 1
	if (tick_index > _delta_tick_simation and gestionMenu.menu == gestionMenu.GestionMenu_MENU_JEU):
		tick_index = 0
		return True
	return False

def model_speed__update_tick_simulation():
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
