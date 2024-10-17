"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

from globals.all import COLOR_BLACK, COLOR_GREEN, COLOR_ORANGE, COLOR_PURPLE, COLOR_RED, COLOR_YELLOW

coord = Tuple[int, int]
types = Dict[str, int | coord]
ressource_type = None

TILETYPE_EMPTY			= 0
TILETYPE_TRANSPORT		= 1
TILETYPE_TRANSPORTHUB	= 2
TILETYPE_INDUSTRY		= 3
TILETYPE_CITY			= 4
TILETYPE_CITYCENTER		= 5

def type_print(tile_type: int):
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

def init(type: int, position: coord) -> types:
	return {
		"type": type,
		"position": position,
	}

def type(tile: types) -> int:
	return tile["type"]

def position(tile: types) -> coord:
	return tile["position"]

def print(tile: types):
	pos = position(tile)
	x = str(pos[0]).rjust(4)
	y = str(pos[1]).rjust(4)
	return f'( {x}, {y} ) | {type_print(type(tile))}'
