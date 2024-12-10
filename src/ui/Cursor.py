"""
Ce fichier gère le mouvement du curseur.
Le curseur est le centre de l'écran
"""

from ui import Zoom
from utils.mytyping import utils_myTyping_mut_coord_f

Cursor_val: utils_myTyping_mut_coord_f = [0, 0]
Cursor_cursor_speed = 0.1

def Cursor_reset():
	global Cursor_val
	Cursor_val = [0, 0]

def Cursor_move_right():
	Cursor_val[0] -= Cursor_cursor_speed * Zoom.Zoom_val

def Cursor_move_left():
	Cursor_val[0] += Cursor_cursor_speed * Zoom.Zoom_val

def Cursor_move_up():
	Cursor_val[1] -= Cursor_cursor_speed * Zoom.Zoom_val

def Cursor_move_down():
	Cursor_val[1] += Cursor_cursor_speed * Zoom.Zoom_val

