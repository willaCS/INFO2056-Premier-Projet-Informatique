from globals import Screenmode, Zoom
from map import TerrainTile
from map import Map
from ui import render
from map.generation.map import random_terrain_landscape
from utils.cache import add_cache

def get_color(coord, refresh = True):
	colors = get_color_all(coord, refresh)
	match Screenmode.val:
		case Screenmode.SCREENMODE_MAIN:
			return colors[0 if Zoom.opti_factor == 1 else 1]
		case Screenmode.SCREENMODE_ECONOMY_DEMAND:
			return colors[2]
		case Screenmode.SCREENMODE_ECONOMY_SUPPLY:
			return colors[3]
		case Screenmode.SCREENMODE_TRANSPORT:
			return colors[4]
		case _:
			return (0, 0, 0)

@add_cache
def get_color_all(coord):
	tile = random_terrain_landscape(coord)
	return (
		get_color_close(coord, tile),
		get_color_far(tile),
		getColorEconomyDemand(tile),
		getColorEconomySupply(tile),
		getColorTansport(tile),
	)

def get_color_close(coord, tile):
	test_map = Map.get(coord)
	if test_map:
		return render.tile(test_map)
	
	if TerrainTile.ressource(tile) != None:
		return render.ressource(TerrainTile.ressource(tile))
	return render.terrainTile(tile)

def get_color_far(tile):
	return render.terrainTile(tile)

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