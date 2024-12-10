"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

import Window
from ui import Zoom
from utils.mytyping import utils_myTyping_coord_f, utils_myTyping_coord_i
from ui import Cursor

def ui_map_utils_coord_to_px(coord: utils_myTyping_coord_f) -> utils_myTyping_coord_i:
	return (
		int(Window.Window_half_resolution[0] + int(Cursor.Cursor_val[0] * Zoom.Zoom_tile_size) + (coord[0]) * Zoom.Zoom_tile_size),
		int(Window.Window_half_resolution[1] - int(Cursor.Cursor_val[1] * Zoom.Zoom_tile_size) - (coord[1]) * Zoom.Zoom_tile_size),
	)

def ui_map_utils_px_to_coord(coord: utils_myTyping_coord_i) -> utils_myTyping_coord_f:
	return (
		(coord[0] - Window.Window_half_resolution[0]) / Zoom.Zoom_tile_size - Cursor.Cursor_val[0],
		-((coord[1] - Window.Window_half_resolution[1]) / Zoom.Zoom_tile_size + Cursor.Cursor_val[1]),
	)
