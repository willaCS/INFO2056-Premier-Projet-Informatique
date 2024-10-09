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

from map import tile

def init() -> Dict[Tuple[int, int], Dict[str, int | Tuple[int, int]]]:
	return {}

def get(coord: Tuple[int, int]) -> Dict[str, int | Tuple[int, int]]:
	global map
	return map.get(coord)

def add(new_tile: Dict[str, int | Tuple[int, int]]):
	global map
	if get(tile.get_position(new_tile)):
		raise ValueError('Cannot add two tile on the same space')
	map[tile.get_position(new_tile)] = new_tile

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
		res += f'- {str(tile.print(t))}\n'
	return res

def tile_is_empty(coord: Tuple[int, int]):
	checked_tile = get(coord)
	if not checked_tile:
		return True
	return tile.get_type(checked_tile) == tile.TILETYPE_EMPTY

map = init()
add(tile.init(tile.TILETYPE_CITY, (2, 3)))
add(tile.init(tile.TILETYPE_CITY, (3, 2)))
add(tile.init(tile.TILETYPE_CITY, (2, 2)))
add(tile.init(tile.TILETYPE_CITYCENTER, (3, 3)))
add(tile.init(tile.TILETYPE_INDUSTRY, (0, -1)))
add(tile.init(tile.TILETYPE_TRANSPORTHUB, (0, 0)))
add(tile.init(tile.TILETYPE_TRANSPORT, (0, 1)))
add(tile.init(tile.TILETYPE_TRANSPORT, (0, 2)))
add(tile.init(tile.TILETYPE_TRANSPORT, (1, 2)))
add(tile.init(tile.TILETYPE_TRANSPORTHUB, (1, 3)))
