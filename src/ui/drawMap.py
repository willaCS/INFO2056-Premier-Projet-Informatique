from typing import Tuple
import pygame

import window
import globals.all
import globals.selectedTile
import globals.cursor
import globals.zoom
from globals.all import COLOR_WHITE, COLOR_BLACK
from map.tile import tile_render
from map.map import map_get
from utils.map import coord_to_px

def getColor(x, y):
	test_map = map_get((x, y))
	if test_map != None:
		return tile_render(test_map)
	match globals.all.screen_mode:
		case globals.all.SCREENMODE_MAIN:
			return (255 - ((x + y) % 32) * 2, 0, 0)
		case globals.all.SCREENMODE_ECONOMY_DEMAND:
			return (0, 255 - ((x + y) % 32) * 2, 0)
		case globals.all.SCREENMODE_ECONOMY_SUPPLY:
			return (0, 0, 255 - ((x + y) % 32) * 2)
		case globals.all.SCREENMODE_TRANSPORT:
			return (255 - ((x + y) % 32) * 2, 255 - ((x + y) % 32) * 2, 0)
		case _:
			return (0, 0, 0)

def __drawTile(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(window.inst, color, ((new_coord[0], new_coord[1] - globals.zoom.tile_size), (globals.zoom.tile_size, globals.zoom.tile_size)))

def __drawTileOutline(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(window.inst, color,
		((new_coord[0], new_coord[1] - globals.zoom.tile_size), (globals.zoom.tile_size, globals.zoom.tile_size)),
		globals.zoom.outline_width,
	)

def drawMap():
	x_min = int(-window.half_resolution[0] / globals.zoom.tile_size - globals.cursor.val[0] - 2)
	x_max = int( window.half_resolution[0] / globals.zoom.tile_size - globals.cursor.val[0] + 2)
	y_min = int(-window.half_resolution[1] / globals.zoom.tile_size - globals.cursor.val[1] - 2)
	y_max = int( window.half_resolution[1] / globals.zoom.tile_size - globals.cursor.val[1] + 2)
	for i in range(x_min, x_max):
		for j in range(y_min, y_max):
			__drawTile(getColor(i, j), (i, j))
	
	pygame.draw.line(window.inst, COLOR_BLACK, coord_to_px((0, -20)), coord_to_px((0, 20)), globals.zoom.line_width)
	pygame.draw.line(window.inst, COLOR_BLACK, coord_to_px((-20, 0)), coord_to_px((20, 0)), globals.zoom.line_width)

	if globals.selectedTile.val:
		__drawTileOutline(COLOR_WHITE, globals.selectedTile.val)



	