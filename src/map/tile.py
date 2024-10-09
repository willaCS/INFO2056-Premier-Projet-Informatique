"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

from globals.all import COLOR_BLACK, COLOR_GREEN, COLOR_ORANGE, COLOR_PURPLE, COLOR_RED, COLOR_YELLOW

TILETYPE_EMPTY			= 0
TILETYPE_TRANSPORT		= 1
TILETYPE_TRANSPORTHUB	= 2
TILETYPE_INDUSTRY		= 3
TILETYPE_CITY			= 4
TILETYPE_CITYCENTER		= 5

def tile_type_print(tile_type: int):
	match tile_type:
		case 0: #TILETYPE_EMPTY
			return 'Empty'
		case 1: #TILETYPE_TRANSPORT
			return 'Transport'
		case 2: #TILETYPE_TRANSPORTHUB
			return 'Transport Hub'
		case 3: #TILETYPE_INDUSTRY
			return 'Industry'
		case 4: #TILETYPE_CITY
			return 'City'
		case 5: #TILETYPE_CITYCENTER
			return 'City Center'

def tile_init(type: int, position: Tuple[int, int]):
	return {
		"type": type,
		"position": position,
	}

def tile_get_type(tile: Dict[str, int | Tuple[int, int]]) -> int:
	return tile["type"]

def tile_get_position(tile: Dict[str, int | Tuple[int, int]]) -> Tuple[int, int]:
	return tile["position"]

def tile_print(tile: Dict[str, int | Tuple[int, int]]):
	pos = tile_get_position(tile)
	x = str(pos[0]).rjust(4)
	y = str(pos[1]).rjust(4)
	return f'( {x}, {y} ) | {tile_type_print(tile_get_type(tile))}'

def tile_render(tile: Dict[str, int | Tuple[int, int]]):
	match tile_get_type(tile):
		case 1: #TILETYPE_TRANSPORT
			return COLOR_PURPLE
		case 2: #TILETYPE_TRANSPORTHUB
			return COLOR_RED
		case 3: #TILETYPE_INDUSTRY
			return COLOR_ORANGE
		case 4: #TILETYPE_CITY
			return COLOR_GREEN
		case 5: #TILETYPE_CITYCENTER
			return COLOR_YELLOW
		case _:
			return COLOR_BLACK
		
