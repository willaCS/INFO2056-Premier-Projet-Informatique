from typing import Dict, Tuple

from map.tile import TILETYPE_CITY, TILETYPE_CITYCENTER, TILETYPE_EMPTY, TILETYPE_INDUSTRY, TILETYPE_TRANSPORT, TILETYPE_TRANSPORTHUB, tile_get_position, tile_get_type, tile_init, tile_print

def map_init() -> Dict[Tuple[int, int], Dict[str, int | Tuple[int, int]]]:
	return {}

def map_get(coord: Tuple[int, int]) -> Dict[str, int | Tuple[int, int]]:
	global map
	return map.get(coord)

def map_add(tile: Dict[str, int | Tuple[int, int]]):
	global map
	if map_get(tile_get_position(tile)):
		raise ValueError('Cannot add two tile on the same space')
	map[tile_get_position(tile)] = tile

def map_remove(coord: Tuple[int, int]):
	global map
	map.pop(coord)

def map_iter():
	global map
	for tile in map.values():
		yield tile

def map_print() -> str:
	global map
	res = 'Map :\n'
	for tile in map:
		res += f'- {str(tile_print(tile))}\n'
	return res

def tile_is_empty(coord: Tuple[int, int]):
	tile = map_get(coord)
	if not tile:
		return True
	return tile_get_type(tile) == TILETYPE_EMPTY

map = map_init()
map_add(tile_init(TILETYPE_CITY, (2, 3)))
map_add(tile_init(TILETYPE_CITY, (3, 2)))
map_add(tile_init(TILETYPE_CITY, (2, 2)))
map_add(tile_init(TILETYPE_CITYCENTER, (3, 3)))
map_add(tile_init(TILETYPE_INDUSTRY, (0, -1)))
map_add(tile_init(TILETYPE_TRANSPORTHUB, (0, 0)))
map_add(tile_init(TILETYPE_TRANSPORT, (0, 1)))
map_add(tile_init(TILETYPE_TRANSPORT, (0, 2)))
map_add(tile_init(TILETYPE_TRANSPORT, (1, 2)))
map_add(tile_init(TILETYPE_TRANSPORTHUB, (1, 3)))
