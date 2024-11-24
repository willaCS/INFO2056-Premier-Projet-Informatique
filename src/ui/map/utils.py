"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

import Window
from utils.mytyping import coord_f, coord_i
from globals import Cursor, Zoom

def coord_to_px(coord: coord_f) -> coord_i:
	return (
		int(Window.half_resolution[0] + int(Cursor.val[0] * Zoom.tile_size) + (coord[0]) * Zoom.tile_size),
		int(Window.half_resolution[1] - int(Cursor.val[1] * Zoom.tile_size) - (coord[1]) * Zoom.tile_size),
	)

def px_to_coord(coord: coord_i) -> coord_f:
	return (
		(coord[0] - Window.half_resolution[0]) / Zoom.tile_size - Cursor.val[0],
		-((coord[1] - Window.half_resolution[1]) / Zoom.tile_size + Cursor.val[1]),
	)
