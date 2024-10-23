"""
Ce fichier permet d'afficher la carte.
"""

import pygame

import Window
from globals import Cursor, SelectedTile, Zoom
from globals.all import COLOR_WHITE
from .get_color import get_color
from utils.map import coord_to_px
from map import Map

def __drawTile(color, coord, ignore_opti = False):
	tile_size = Zoom.tile_size * Zoom.opti_factor if not ignore_opti else Zoom.tile_size
	new_coord = coord_to_px(coord)
	pygame.draw.rect(Window.inst, color, (
		(new_coord[0], new_coord[1] - int(Zoom.tile_size)),
   		(int(tile_size) + 1, int(tile_size) + 1)
	))

def __drawTileOutline(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(Window.inst, color,
		((new_coord[0], int(new_coord[1] - Zoom.tile_size)), (int(Zoom.tile_size), int(Zoom.tile_size))),
		int(Zoom.outline_width),
	)

def drawMap():
	x_min = int(-Window.half_resolution[0] / Zoom.tile_size - Cursor.val[0]) // Zoom.opti_factor - 2
	x_max = int( Window.half_resolution[0] / Zoom.tile_size - Cursor.val[0]) // Zoom.opti_factor + 2
	y_min = int(-Window.half_resolution[1] / Zoom.tile_size - Cursor.val[1]) // Zoom.opti_factor - 2
	y_max = int( Window.half_resolution[1] / Zoom.tile_size - Cursor.val[1]) // Zoom.opti_factor + 2
	
	# Draw Terrain
	for i in range(x_min, x_max):
		for j in range(y_min, y_max):
			coord = (i * Zoom.opti_factor, j * Zoom.opti_factor)
			__drawTile(get_color(coord), coord)
	
	# Draw Buildings even if zoomed out
	if Zoom.opti_factor > 1:
		for tile_coord in Map.map.keys():
			if x_min * Zoom.opti_factor > tile_coord[0] or tile_coord[0] > x_max  * Zoom.opti_factor\
				or y_min * Zoom.opti_factor > tile_coord[1] or tile_coord[1] > y_max  * Zoom.opti_factor:
				continue
			__drawTile(get_color(tile_coord, True), tile_coord, True)
	
	# Draw Selected Tile
	if SelectedTile.val:
		__drawTileOutline(COLOR_WHITE, SelectedTile.val)



	