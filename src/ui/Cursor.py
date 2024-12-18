"""
Ce fichier gère le mouvement du curseur.
Le curseur est le centre de l'écran
"""

from ui import Zoom
from utils.mytyping import mut_coord_f

val: mut_coord_f = [0, 0]
cursor_speed = 0.1

def reset():
	global val
	val = [0, 0]

def move_right():
	val[0] -= cursor_speed * Zoom.val

def move_left():
	val[0] += cursor_speed * Zoom.val

def move_up():
	val[1] -= cursor_speed * Zoom.val

def move_down():
	val[1] += cursor_speed * Zoom.val

