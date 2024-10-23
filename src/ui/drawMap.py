"""
Ce fichier permet d'afficher la carte.
"""

import pygame

import Window
from globals import Cursor, SelectedTile, Zoom
from globals.all import COLOR_WHITE, COLOR_BLACK
from .get_color import get_color
from utils.map import coord_to_px

def __drawTile(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(Window.inst, color, ((new_coord[0], new_coord[1] - Zoom.tile_size), (Zoom.tile_size * Zoom.opti_factor + 1, Zoom.tile_size * Zoom.opti_factor + 1)))

def __drawTileOutline(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(Window.inst, color,
		((new_coord[0], int(new_coord[1] - Zoom.tile_size)), (int(Zoom.tile_size), int(Zoom.tile_size))),
		Zoom.outline_width,
	)

def drawMap():
	x_min = int(-Window.half_resolution[0] / Zoom.tile_size - Cursor.val[0]) // Zoom.opti_factor - 2
	x_max = int( Window.half_resolution[0] / Zoom.tile_size - Cursor.val[0]) // Zoom.opti_factor + 2
	y_min = int(-Window.half_resolution[1] / Zoom.tile_size - Cursor.val[1]) // Zoom.opti_factor - 2
	y_max = int( Window.half_resolution[1] / Zoom.tile_size - Cursor.val[1]) // Zoom.opti_factor + 2
	for i in range(x_min, x_max):
		for j in range(y_min, y_max):
			coord = (i * Zoom.opti_factor, j * Zoom.opti_factor)
			__drawTile(get_color(coord), coord)
	
	# pygame.draw.line(Window.inst, COLOR_BLACK, coord_to_px((0, -20)), coord_to_px((0, 20)), Zoom.line_width)
	# pygame.draw.line(Window.inst, COLOR_BLACK, coord_to_px((-20, 0)), coord_to_px((20, 0)), Zoom.line_width)

	if SelectedTile.val:
		__drawTileOutline(COLOR_WHITE, SelectedTile.val)



	