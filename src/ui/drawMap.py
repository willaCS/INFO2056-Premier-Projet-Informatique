"""
Ce fichier permet d'afficher la carte.
"""

import math
from typing import List
import pygame

import Window
from globals import Cursor, Screenmode, SelectedTile, Zoom
from globals.all import COLOR_WHITE, COLOR_BLACK
from map import TerrainTile
from map import Map
from ui import render
from map.generation.map import random_terrain_landscape
from utils.map import coord_to_px

# Colors approx : sqrt(sum(color_i^2)/i)

def getColor(coord):
	test_map = Map.get(coord)
	if test_map:
		return render.tile(test_map)
	
	tile = random_terrain_landscape(coord)
	match Screenmode.val:
		case Screenmode.SCREENMODE_MAIN:
			if TerrainTile.ressource(tile) != None:
				return render.ressource(TerrainTile.ressource(tile))
			return render.terrainTile(tile)
		
		case Screenmode.SCREENMODE_ECONOMY_DEMAND:
			return getColorEconomyDemand(tile)
		
		case Screenmode.SCREENMODE_ECONOMY_SUPPLY:
			return getColorEconomySupply(tile)
		
		case Screenmode.SCREENMODE_TRANSPORT:
			return getColorTansport(tile)
		
		case _:
			return (0, 0, 0)

def getColorEconomyDemand(tile):
	height = TerrainTile.height(tile)
	test = height % 4 * 16
	if (height < 0):
		return (0, 0, 180 + height * 4)
	else:
		return (80 - test, 80 - test, 80 - test)

def getColorEconomySupply(tile):
	height = TerrainTile.height(tile)
	test = height % 4 * 16
	if (height < 0):
		return (0, 0, 180 + height * 4)
	else:
		return (0, 0, 255 - test)

def getColorTansport(tile):
	height = TerrainTile.height(tile)
	test = height % 4 * 16
	if (height < 0):
		return (0, 0, 180 + height * 4)
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

def averageColor(colors: List[int]):
	red = 0
	green = 0
	blue = 0
	for color in colors:
		red += color[0] ** 2
		green += color[1] ** 2
		blue += color[2] ** 2
	return (
		math.sqrt(red) // len(colors),
		math.sqrt(green) // len(colors),
		math.sqrt(blue) // len(colors)
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



	