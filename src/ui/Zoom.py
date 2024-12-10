"""
Ce fichier gère le zoom sur la carte et calcule les valeurs sur la carte
modifié par le zoom.
Exemple: le nombre de pixel que fait une case.
"""

import math


Zoom_val = 100
Zoom__zoom_speed = 1.05
Zoom__zoom_min = 1
Zoom__zoom_max = 1000
Zoom_tile_size = 0
Zoom_line_width = 0
Zoom_outline_width = 0
Zoom_opti_factor = 2

def Zoom__update():
	global Zoom_tile_size, Zoom_line_width, Zoom_outline_width,Zoom_opti_factor
	Zoom_tile_size = 200 / Zoom_val
	Zoom_line_width = 25 / Zoom_val
	Zoom_outline_width = 15 / Zoom_val
	Zoom_opti_factor = max(2 ** int(math.log2(Zoom_val / 10)), 1)

def Zoom_increment():
	global Zoom_val
	if Zoom_val < Zoom__zoom_max:
		Zoom_val *= Zoom__zoom_speed
		Zoom__update()

def Zoom_decrement():
	global Zoom_val
	if Zoom_val > Zoom__zoom_min:
		Zoom_val /= Zoom__zoom_speed
		Zoom__update()

Zoom__update()