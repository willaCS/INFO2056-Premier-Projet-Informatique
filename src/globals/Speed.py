"""
Ce fichier gère la vitesse de simulation du jeu.
"""

__prev_val = 3
val = 3

def increment():
	global val
	if val < 5:
		val += 1

def decrement():
	global val
	if val > 1:
		val -= 1

def set(new_speed):
	global val
	val = new_speed

def pause():
	global val, __prev_val
	if (val != 0):
		__prev_val = val
		val = 0
	else:
		val = __prev_val