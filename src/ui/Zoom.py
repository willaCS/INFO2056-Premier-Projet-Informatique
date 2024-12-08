"""
Ce fichier gère le zoom sur la carte et calcule les valeurs sur la carte
modifié par le zoom.
Exemple: le nombre de pixel que fait une case.
"""

import math


val = 100
__zoom_speed = 1.05
__zoom_min = 1
__zoom_max = 1000
tile_size = 0
line_width = 0
outline_width = 0
opti_factor = 2

def __update():
	global tile_size, line_width, outline_width,opti_factor
	tile_size = 200 // val
	line_width = 25 // val
	outline_width = 15 // val
	opti_factor = max(2 ** int(math.log2(val / 10)), 1)

def increment():
	global val
	if val < __zoom_max:
		val *= __zoom_speed
		__update()

def decrement():
	global val
	if val > __zoom_min:
		val /= __zoom_speed
		__update()

__update()