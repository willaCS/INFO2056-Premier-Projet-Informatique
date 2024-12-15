"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

import random

from model.terrain.Ressource import RessourceType, Ressource
from model.terrain.TerrainTile import TerrainTile, TerrainTileType
from utils.cache import add_cache
from .seed import get_height, get_seed, load_seed, random_lcg_coord
from utils.mytyping import coord_i

def init_random():
	random.seed()

	seed = get_seed()
	print(seed)
	load_seed()

@add_cache
def get_terrain_tile(coord: coord_i) -> TerrainTile:
	height = get_height(coord)
	
	if (height < -5):
		res = TerrainTile(TerrainTileType.DEEPSEA, coord, height)
	elif (height < 0):
		res = TerrainTile(TerrainTileType.SEA, coord, height)
	elif (height < 1):
		res = TerrainTile(TerrainTileType.BEACH, coord, height)
	elif (height < 15):
		res = TerrainTile(TerrainTileType.PLAIN, coord, height)
	elif (height < 25):
		res = TerrainTile(TerrainTileType.FOREST, coord, height)
	elif (height < 35):
		res = TerrainTile(TerrainTileType.MOUNTAIN_SIDE, coord, height)
	elif (height >= 35):
		res = TerrainTile(TerrainTileType.MOUNTAIN_TOP, coord, height)
	else:
		raise ValueError("Terrain tile has height not possible")
	
	ressource = int(random_lcg_coord(res.position) * 100)
	richness = int(random_lcg_coord(res.position) * 100)
	res.ressource = generate_ressource(res, ressource, richness, height)
	return res	

def generate_ressource(tile: TerrainTile, ressource: int, richness: int, height: int) -> Ressource | None:
	match (tile.type):
		case TerrainTileType.DEEPSEA:
			match ressource:
				case 90:
					return Ressource(RessourceType.FISH, richness, height)
				case 95 | 96 | 97:
					return Ressource(RessourceType.FISH, richness, height)
				case _:
					pass
		case TerrainTileType.SEA:
			match ressource:
				case 90 | 91 | 92 | 93 | 94:
					return Ressource(RessourceType.FISH, richness, height)
				case _:
					pass
		case TerrainTileType.BEACH:
			match ressource:
				case 1:
					return Ressource(RessourceType.SALT, richness, height)
				case 0:
					return Ressource(RessourceType.OIL, richness, height)
				case _:
					return Ressource(RessourceType.SAND, 1, height)
		case TerrainTileType.PLAIN:
			if height == 9 or height == 10:
				return Ressource(RessourceType.FERTILE_LAND, richness, height)
		case TerrainTileType.FOREST:
			return Ressource(RessourceType.WOOD, richness % 5, height)
		case TerrainTileType.MOUNTAIN_SIDE:
			match ressource:
				case 0:
					return Ressource(RessourceType.COAL, richness, height)
				case 1:
					return Ressource(RessourceType.IRON, richness, height)
				case 2:
					return Ressource(RessourceType.COPPER, richness, height)
				case _:
					return Ressource(RessourceType.STONE, richness % 5, height)
		case TerrainTileType.MOUNTAIN_TOP:
			match ressource:
				case 0:
					return Ressource(RessourceType.IRON, richness, height)
				case 1:
					return Ressource(RessourceType.PRECIOUS_METALS, richness, height)
				case 2:
					return Ressource(RessourceType.RARE_METALS, richness, height)
				case _:
					pass
		case _:
			pass
	return None