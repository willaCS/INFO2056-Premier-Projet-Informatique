"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

import random

from model.terrain import Ressource, TerrainTile
from utils.cache import utils_cache_add_cache
from .seed import model_terrain_seed_get_height, model_terrain_seed_get_seed, model_terrain_seed_load_seed, model_terrain_seed_random_lcg_coord
from utils.mytyping import utils_myTyping_coord_i

def model_terrain_terrain_init_random():
	random.seed()

	seed = model_terrain_seed_get_seed()
	print(seed)
	model_terrain_seed_load_seed()

	# for i in range(-500 + 0, 500 + 0, 2):
	# 	for j in range(-500 + 0, 500 + 0, 2):
	# 		# print(i, j)
	# 		get_terrain_tile((i, j))
	# 	print(i)

@utils_cache_add_cache
def model_terrain_terrain_get_terrain_tile(coord: utils_myTyping_coord_i) -> TerrainTile.model_terrain_terrainTile_types:
	height = model_terrain_seed_get_height(coord)
	
	if (height < -5):
		res = TerrainTile.model_terrain_terrainTile_init(TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_DEEPSEA, coord, height)
	elif (height < 0):
		res = TerrainTile.model_terrain_terrainTile_init(TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_SEA, coord, height)
	elif (height < 1):
		res = TerrainTile.model_terrain_terrainTile_init(TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, coord, height)
	elif (height < 15):
		res = TerrainTile.model_terrain_terrainTile_init(TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, coord, height)
	elif (height < 25):
		res = TerrainTile.model_terrain_terrainTile_init(TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, coord, height)
	elif (height < 35):
		res = TerrainTile.model_terrain_terrainTile_init(TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, coord, height)
	elif (height >= 35):
		res = TerrainTile.model_terrain_terrainTile_init(TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_TOP, coord, height)
	else:
		raise ValueError("Terrain tile has height not possible")
	
	ressource = int(model_terrain_seed_random_lcg_coord(TerrainTile.model_terrain_terrainTile_position(res)) * 100)
	richness = int(model_terrain_seed_random_lcg_coord(TerrainTile.model_terrain_terrainTile_position(res)) * 100)
	res["ressource"] = model_terrain_terrain_generate_ressource(res, ressource, richness, height)
	return res	

def model_terrain_terrain_generate_ressource(tile: TerrainTile.model_terrain_terrainTile_types, ressource: int, richness: int, height: int) -> Ressource.model_terrain_ressource_types | None:
	match(TerrainTile.model_terrain_terrainTile_type(tile)):
		case TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_DEEPSEA:
			match ressource:
				case 90:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_FISH, richness, height)
				case 95 | 96 | 97:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_FISH, richness, height)
				case _:
					pass
		case TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_SEA:
			match ressource:
				case 90 | 91 | 92 | 93 | 94:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_FISH, richness, height)
				case _:
					pass
		case TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH:
			match ressource:
				case 1:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_SALT, richness, height)
				case 0:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_OIL, richness, height)
				case _:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_SAND, 1, height)
		case TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN:
			if height == 9 or height == 10:
				return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_FERTILE_LAND, richness, height)
		case TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST:
			return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_WOOD, richness % 5, height)
		case TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE:
			match ressource:
				case 0:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_COAL, richness, height)
				case 1:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_IRON, richness, height)
				case 2:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_COPPER, richness, height)
				case _:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_STONE, richness % 5, height)
		case TerrainTile. model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_TOP:
			match ressource:
				case 0:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_IRON, richness, height)
				case 1:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_PRECIOUS_METALS, richness, height)
				case 2:
					return Ressource.model_terrain_ressource_init(Ressource.model_terrain_ressource_RESSOURCE_RARE_METALS, richness, height)
				case _:
					pass
		case _:
			pass
	return None