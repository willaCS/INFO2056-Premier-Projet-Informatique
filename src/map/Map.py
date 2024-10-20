"""
Ce fichier gère la carte du jeu.
La carte est faite du dictionaire de coordonnées par la structure case (Tile).
Ce fichier permet de faire :
- obtenir un case avec ses coordonnées
- ajouter une nouvelle case
- supprimer une case
- checker si la case est vide
"""

from typing import Dict, Tuple

from map import Industry, Ressource, TerrainTile, Tile
from map.generation.map import random_terrain_landscape

def init() -> Dict[Tuple[int, int], Dict[str, int | Tuple[int, int]]]:
	return {}

def get(coord: Tuple[int, int]) -> Dict[str, int | Tuple[int, int]]:
	global map
	return map.get(coord)

def add(tile: Dict[str, int | Tuple[int, int]]):
	global map
	if get(Tile.position(tile)):
		raise ValueError('Cannot add two tile on the same space')
	map[Tile.position(tile)] = tile

def remove(coord: Tuple[int, int]):
	global map
	map.pop(coord)

def iter():
	global map
	for tile in map.values():
		yield tile

def tile_is_empty(coord: Tuple[int, int]):
	tile = get(coord)
	if not tile:
		return True
	return Tile.type(tile) == Tile.TILETYPE_EMPTY

def place(tile: Dict[str, int | Tuple[int, int]]) -> bool:
	if get(Tile.position(tile)) != None:
		return False
	match Tile.type(tile):
		case Tile.TILETYPE_INDUSTRY:
			terrain = random_terrain_landscape(Tile.position(tile))
			tileProtect = Industry.get_data(Tile.subtype(tile))
			for can_place in tileProtect['place_on']:
				match can_place['type']:
					case Industry.PLACE_ON_TERRAIN:
						if TerrainTile.type(terrain) == can_place['id']:
							add(tile)
							return True
					case Industry.PLACE_ON_RESSOURCE:
						if not TerrainTile.ressource(terrain):
							continue
						if Ressource.type(TerrainTile.ressource(terrain)) == can_place['id']:
							add(tile)
							return True
		case Tile.TILETYPE_TRANSPORT:
			terrain = random_terrain_landscape(Tile.position(tile))
			if terrain != TerrainTile.TERRAINTILETYPE_DEEPSEA and terrain != TerrainTile.TERRAINTILETYPE_SEA:
				add(tile)
				return True
		case Tile.TILETYPE_TRANSPORTHUB:
			match Tile.subtype(tile):
				case Industry.TRANSPORT_HUB_HARBOR:
					terrain = random_terrain_landscape(Tile.position(tile))
					print(terrain, TerrainTile.type(terrain) != TerrainTile.TERRAINTILETYPE_SEA)
					if TerrainTile.type(terrain) != TerrainTile.TERRAINTILETYPE_SEA:
						return False
					has_adjacent_land = False
					for el in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
						terrain = random_terrain_landscape((
							Tile.position(tile)[0] + el[0],
							Tile.position(tile)[1] + el[1],
						))
						print(terrain)
						if TerrainTile.type(terrain) == TerrainTile.TERRAINTILETYPE_BEACH:
							has_adjacent_land == True
					if not has_adjacent_land:
						return False
					add(tile)
					return True
				case _:
					terrain = random_terrain_landscape(Tile.position(tile))
					if TerrainTile.type(terrain) != TerrainTile.TERRAINTILETYPE_DEEPSEA \
						and TerrainTile.type(terrain) != TerrainTile.TERRAINTILETYPE_SEA:
						add(tile)
						return True
	return False

map = init()
