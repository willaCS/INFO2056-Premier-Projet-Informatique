from globals import Screenmode, Zoom
from map import TerrainTile
from map import Map
from ui import render
from map.generation.map import random_terrain_landscape
from utils.cache import add_cache
from utils.mytyping import coord_i

def get_color(coord: coord_i, ignore_opti: bool = False):
	colors = get_color_all(coord)
	match Screenmode.val:
		case Screenmode.SCREENMODE_MAIN:
			return colors[0 if Zoom.opti_factor == 1 or ignore_opti else 1]
		case Screenmode.SCREENMODE_ECONOMY_DEMAND:
			return colors[2]
		case Screenmode.SCREENMODE_ECONOMY_SUPPLY:
			return colors[3]
		case Screenmode.SCREENMODE_TRANSPORT:
			return colors[4]
		case _:
			return (0, 0, 0)

def refresh_color(coord: coord_i):
	get_color_all(coord, True) # type: ignore

@add_cache
def get_color_all(coord: coord_i):
	tile: TerrainTile.types = random_terrain_landscape(coord)
	return (
		get_color_close(coord, tile),
		get_color_far(tile),
		getColorEconomyDemand(coord, tile),
		getColorEconomySupply(tile),
		getColorTansport(tile),
	)

def get_color_close(coord: coord_i, tile: TerrainTile.types):
	test_map = Map.get(coord)
	if test_map:
		return render.tile(test_map)
	
	if TerrainTile.ressource(tile) != None:
		return render.ressource(TerrainTile.ressource(tile)) # type: ignore
	return render.terrainTile(tile)

def get_color_far(tile: TerrainTile.types):
	return render.terrainTile(tile)

def getColorEconomyDemand(coord: coord_i, tile: TerrainTile.types):
	test_map = Map.get(coord)
	if test_map:
		return render.tile(test_map)
	height = TerrainTile.height(tile)
	test = height % 4 * 16
	if (height < 0):
		return (0, 0, 180 + height * 4)
	else:
		return (80 - test, 80 - test, 80 - test)

def getColorEconomySupply(tile: TerrainTile.types):
	height = TerrainTile.height(tile)
	test = height % 4 * 16
	if (height < 0):
		return (0, 0, 180 + height * 4)
	else:
		return (0, 0, 255 - test)

def getColorTansport(tile: TerrainTile.types):
	height = TerrainTile.height(tile)
	test = height % 4 * 16
	if (height < 0):
		return (0, 0, 180 + height * 4)
	else:
		return (255 - test, 255 - test, 0)