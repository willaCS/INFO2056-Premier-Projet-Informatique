"""
Ce fichier permet d'afficher la carte.
"""

import pygame

import Window
from globals import Cursor, Screenmode, SelectedTile, Zoom
from globals.all import COLOR_WHITE, COLOR_BLACK
from map import TerrainTile
from map import Tile
from map.Map import get
from utils.map import coord_to_px, random_terrain_ressource, random_terrain_landscape

def getColor(coord):
	test_map = get(coord)
	if test_map:
		return Tile.render(test_map)
	
	tile = random_terrain_landscape(coord)
	match Screenmode.val:
		case Screenmode.SCREENMODE_MAIN:
			return TerrainTile.render(tile)
		case Screenmode.SCREENMODE_ECONOMY_DEMAND:
			return getColorEconomyDemand(tile)
		case Screenmode.SCREENMODE_ECONOMY_SUPPLY:
			return getColorEconomySupply(tile)
		case Screenmode.SCREENMODE_TRANSPORT:
			return getColorTansport(tile)
		case _:
			return (0, 0, 0)

def getColorEconomyDemand(tile):
	height = TerrainTile.height(tile) % 4 * 16
	test = height % 4 * 16
	if (height < 0):
		return (0, 25, 150 - test)
	else:
		return (0, 255 - test, 0)

def getColorEconomySupply(tile):
	height = TerrainTile.height(tile) % 4 * 16
	test = height % 4 * 16
	if (height < 0):
		return (0, 25, 150 - test)
	else:
		return (0, 0, 255 - test)

def getColorTansport(tile):
	height = TerrainTile.height(tile) % 4 * 16
	test = height % 4 * 16
	if (height < 0):
		return (0, 25, 150 - test)
	else:
		return (255 - test, 255 - test, 0)

def __drawTile(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(Window.inst, color, ((new_coord[0], new_coord[1] - Zoom.tile_size), (Zoom.tile_size, Zoom.tile_size)))

def __drawTileOutline(color, coord):
	new_coord = coord_to_px(coord)
	pygame.draw.rect(Window.inst, color,
		((new_coord[0], new_coord[1] - Zoom.tile_size), (Zoom.tile_size, Zoom.tile_size)),
		Zoom.outline_width,
	)

def drawMap():
	x_min = int(-Window.half_resolution[0] / Zoom.tile_size - Cursor.val[0] - 2)
	x_max = int( Window.half_resolution[0] / Zoom.tile_size - Cursor.val[0] + 2)
	y_min = int(-Window.half_resolution[1] / Zoom.tile_size - Cursor.val[1] - 2)
	y_max = int( Window.half_resolution[1] / Zoom.tile_size - Cursor.val[1] + 2)
	for i in range(x_min, x_max):
		for j in range(y_min, y_max):
			coord = (i, j)
			__drawTile(getColor(coord), coord)
	
	pygame.draw.line(Window.inst, COLOR_BLACK, coord_to_px((0, -20)), coord_to_px((0, 20)), Zoom.line_width)
	pygame.draw.line(Window.inst, COLOR_BLACK, coord_to_px((-20, 0)), coord_to_px((20, 0)), Zoom.line_width)

	if SelectedTile.val:
		__drawTileOutline(COLOR_WHITE, SelectedTile.val)



	