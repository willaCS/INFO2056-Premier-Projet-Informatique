"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

import math
import random
from typing import Callable, Dict, Tuple

import Window
from globals import Cursor, Zoom
from map import Map, Ressource, TerrainTile, Tile
from utils.seed import get_height, get_seed, load_seed, random_cos, random_cos2

def coord_to_px(coord: Tuple[float, float]) -> Tuple[int, int]:
	return (
		Window.half_resolution[0] + int(Cursor.val[0] * Zoom.tile_size) + (coord[0]) * Zoom.tile_size,
		Window.half_resolution[1] - int(Cursor.val[1] * Zoom.tile_size) - (coord[1]) * Zoom.tile_size,
	)

def px_to_coord(coord: Tuple[int, int]) -> Tuple[float, float]:
	return (
		(coord[0] - Window.half_resolution[0]) / Zoom.tile_size - Cursor.val[0],
		-((coord[1] - Window.half_resolution[1]) / Zoom.tile_size + Cursor.val[1]),
	)

def init_random():
	random.seed()

	seed = get_seed()
	load_seed(seed)

def create_caching_function(arg_func: Callable[[Tuple[int, int]], int]) -> Callable[[Tuple[int, int]], int]:
	cache: Dict[Tuple[int, int], int] = {}
	
	def test(coord: Tuple[int, int]):
		if cache.get(coord) == None:
			res = arg_func(coord)
			cache[coord] = res
		return cache.get(coord)

	return test

@create_caching_function
def random_terrain_landscape(coord: Tuple[int, int]) -> Dict[str, int | Tuple[int, int]]:
	height = get_height(coord)
	
	if (height < -5):
		res = TerrainTile.init(TerrainTile.TERRAINTILETYPE_DEEPSEA, coord, height)
	elif (height < 0):
		res = TerrainTile.init(TerrainTile.TERRAINTILETYPE_SEA, coord, height)
	elif (height < 1):
		res = TerrainTile.init(TerrainTile.TERRAINTILETYPE_BEACH, coord, height)
	elif (height < 15):
		res = TerrainTile.init(TerrainTile.TERRAINTILETYPE_PLAIN, coord, height)
	elif (height < 25):
		res = TerrainTile.init(TerrainTile.TERRAINTILETYPE_FOREST, coord, height)
	elif (height < 35):
		res = TerrainTile.init(TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, coord, height)
	elif (height >= 35):
		res = TerrainTile.init(TerrainTile.TERRAINTILETYPE_MOUNTAIN_TOP, coord, height)
	else:
		raise ValueError("Terrain tile has height not possible")
	
	generate_ressource(res)
	return res

def generate_ressource(tile: TerrainTile.typing):
	ressource = random_cos(TerrainTile.position(tile))
	richness = random_cos2(TerrainTile.position(tile))
	print(ressource, richness, TerrainTile.type(tile))
	match(TerrainTile.type(tile)):
		case TerrainTile.TERRAINTILETYPE_DEEPSEA:
			match ressource:
				case 90 | 91 | 92 | 93 | 94:
					tile["ressource"] = Ressource.init(Ressource.RESSOURCE_FISH, richness)
		case TerrainTile.TERRAINTILETYPE_SEA:
			pass
		case TerrainTile.TERRAINTILETYPE_BEACH:
			pass
		case TerrainTile.TERRAINTILETYPE_PLAIN:
			print('here')
			match ressource:
				case 90 | 91 | 92 | 93 | 94:
					tile["ressource"] = Ressource.init(Ressource.RESSOURCE_HUNTING_GROUNDS, richness)
					print("xd")
		case TerrainTile.TERRAINTILETYPE_FOREST:
			pass
		case TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE:
			pass
		case TerrainTile. TERRAINTILETYPE_MOUNTAIN_TOP:
			pass
		case _:
			pass
	return tile