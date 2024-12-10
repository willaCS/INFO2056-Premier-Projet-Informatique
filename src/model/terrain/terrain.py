"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

import random

from model.terrain import Ressource, TerrainTile
from utils.cache import add_cache
from .seed import get_height, get_seed, load_seed, random_lcg_coord
from utils.mytyping import coord_i

def init_random():
	random.seed()

	seed = get_seed()
	print(seed)
	load_seed()

	# for i in range(-500 + 0, 500 + 0, 2):
	# 	for j in range(-500 + 0, 500 + 0, 2):
	# 		# print(i, j)
	# 		get_terrain_tile((i, j))
	# 	print(i)

@add_cache
def get_terrain_tile(coord: coord_i) -> TerrainTile.types:
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
	
	ressource = int(random_lcg_coord(TerrainTile.position(res)) * 100)
	richness = int(random_lcg_coord(TerrainTile.position(res)) * 100)
	res["ressource"] = generate_ressource(res, ressource, richness, height)
	return res	

def generate_ressource(tile: TerrainTile.types, ressource: int, richness: int, height: int) -> Ressource.types | None:
	match(TerrainTile.type(tile)):
		case TerrainTile.TERRAINTILETYPE_DEEPSEA:
			match ressource:
				case 90:
					return Ressource.init(Ressource.RESSOURCE_FISH, richness, height)
				case 95 | 96 | 97:
					return Ressource.init(Ressource.RESSOURCE_FISH, richness, height)
				case _:
					pass
		case TerrainTile.TERRAINTILETYPE_SEA:
			match ressource:
				case 90 | 91 | 92 | 93 | 94:
					return Ressource.init(Ressource.RESSOURCE_FISH, richness, height)
				case _:
					pass
		case TerrainTile.TERRAINTILETYPE_BEACH:
			match ressource:
				case 1:
					return Ressource.init(Ressource.RESSOURCE_SALT, richness, height)
				case 0:
					return Ressource.init(Ressource.RESSOURCE_OIL, richness, height)
				case _:
					return Ressource.init(Ressource.RESSOURCE_SAND, 1, height)
		case TerrainTile.TERRAINTILETYPE_PLAIN:
			if height == 9 or height == 10:
				return Ressource.init(Ressource.RESSOURCE_FERTILE_LAND, richness, height)
		case TerrainTile.TERRAINTILETYPE_FOREST:
			return Ressource.init(Ressource.RESSOURCE_WOOD, richness % 5, height)
		case TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE:
			match ressource:
				case 0:
					return Ressource.init(Ressource.RESSOURCE_COAL, richness, height)
				case 1:
					return Ressource.init(Ressource.RESSOURCE_IRON, richness, height)
				case 2:
					return Ressource.init(Ressource.RESSOURCE_COPPER, richness, height)
				case _:
					return Ressource.init(Ressource.RESSOURCE_STONE, richness % 5, height)
		case TerrainTile. TERRAINTILETYPE_MOUNTAIN_TOP:
			match ressource:
				case 0:
					return Ressource.init(Ressource.RESSOURCE_IRON, richness, height)
				case 1:
					return Ressource.init(Ressource.RESSOURCE_PRECIOUS_METALS, richness, height)
				case 2:
					return Ressource.init(Ressource.RESSOURCE_RARE_METALS, richness, height)
				case _:
					pass
		case _:
			pass
	return None