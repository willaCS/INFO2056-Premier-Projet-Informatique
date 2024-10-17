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
	return Tile.type(tile) == Tile.TILETYPE_EMPTY

map = init()
