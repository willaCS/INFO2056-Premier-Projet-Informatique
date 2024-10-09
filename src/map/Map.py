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

from map import Tile

def init() -> Dict[Tuple[int, int], Dict[str, int | Tuple[int, int]]]:
	return {}

def get(coord: Tuple[int, int]) -> Dict[str, int | Tuple[int, int]]:
	global map
	return map.get(coord)

def add(tile: Dict[str, int | Tuple[int, int]]):
	global map
	if get(Tile.get_position(tile)):
		raise ValueError('Cannot add two tile on the same space')
	map[Tile.get_position(tile)] = tile

def remove(coord: Tuple[int, int]):
	global map
	map.pop(coord)

def iter():
	global map
	for tile in map.values():
		yield tile

def print() -> str:
	global map
	res = 'Map :\n'
	for t in map:
		res += f'- {str(Tile.print(t))}\n'
	return res

def tile_is_empty(coord: Tuple[int, int]):
	tile = get(coord)
	if not tile:
		return True
	return Tile.get_type(tile) == Tile.TILETYPE_EMPTY

map = init()
add(Tile.init(Tile.TILETYPE_CITY, (2, 3)))
add(Tile.init(Tile.TILETYPE_CITY, (3, 2)))
add(Tile.init(Tile.TILETYPE_CITY, (2, 2)))
add(Tile.init(Tile.TILETYPE_CITYCENTER, (3, 3)))
add(Tile.init(Tile.TILETYPE_INDUSTRY, (0, -1)))
add(Tile.init(Tile.TILETYPE_TRANSPORTHUB, (0, 0)))
add(Tile.init(Tile.TILETYPE_TRANSPORT, (0, 1)))
add(Tile.init(Tile.TILETYPE_TRANSPORT, (0, 2)))
add(Tile.init(Tile.TILETYPE_TRANSPORT, (1, 2)))
add(Tile.init(Tile.TILETYPE_TRANSPORTHUB, (1, 3)))
