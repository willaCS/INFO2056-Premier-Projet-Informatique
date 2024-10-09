"""
Ce fichier permet d'afficher la carte.
"""

import pygame

import window
from globals import selectedTile, cursor, zoom, screenmode
from globals.all import COLOR_WHITE, COLOR_BLACK
from map.tile import render
from map.map import get
from utils.map import coord_to_px

def getColor(x, y):
	test_map = get((x, y))
	if test_map:
		return render(test_map)
	match screenmode.val:
		case screenmode.SCREENMODE_MAIN:
			return (255 - ((x + y) % 32) * 2, 0, 0)
		case screenmode.SCREENMODE_ECONOMY_DEMAND:
			return (0, 255 - ((x + y) % 32) * 2, 0)
		case screenmode.SCREENMODE_ECONOMY_SUPPLY:
			return (0, 0, 255 - ((x + y) % 32) * 2)
		case screenmode.SCREENMODE_TRANSPORT:
			return (255 - ((x + y) % 32) * 2, 255 - ((x + y) % 32) * 2, 0)
		case _:
			return (0, 0, 0)

def __drawTile(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(window.inst, color, ((new_coord[0], new_coord[1] - zoom.tile_size), (zoom.tile_size, zoom.tile_size)))

def __drawTileOutline(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(window.inst, color,
		((new_coord[0], new_coord[1] - zoom.tile_size), (zoom.tile_size, zoom.tile_size)),
		zoom.outline_width,
	)

def drawMap():
	x_min = int(-window.half_resolution[0] / zoom.tile_size - cursor.val[0] - 2)
	x_max = int( window.half_resolution[0] / zoom.tile_size - cursor.val[0] + 2)
	y_min = int(-window.half_resolution[1] / zoom.tile_size - cursor.val[1] - 2)
	y_max = int( window.half_resolution[1] / zoom.tile_size - cursor.val[1] + 2)
	for i in range(x_min, x_max):
		for j in range(y_min, y_max):
			__drawTile(getColor(i, j), (i, j))
	
	pygame.draw.line(window.inst, COLOR_BLACK, coord_to_px((0, -20)), coord_to_px((0, 20)), zoom.line_width)
	pygame.draw.line(window.inst, COLOR_BLACK, coord_to_px((-20, 0)), coord_to_px((20, 0)), zoom.line_width)

	if selectedTile.val:
		__drawTileOutline(COLOR_WHITE, selectedTile.val)



	