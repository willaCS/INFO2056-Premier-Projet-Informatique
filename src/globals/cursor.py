"""
Ce fichier gère le mouvement du curseur.
Le curseur est le centre de l'écran
"""

import globals.zoom

val = [0, 0]
cursor_speed = 0.1

def reset():
	global val
	val = [0, 0]

def move_right():
	val[0] -= cursor_speed * globals.zoom.val

def move_left():
	val[0] += cursor_speed * globals.zoom.val

def move_up():
	val[1] -= cursor_speed * globals.zoom.val

def move_down():
	val[1] += cursor_speed * globals.zoom.val

