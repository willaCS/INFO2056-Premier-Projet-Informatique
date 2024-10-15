"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

TERRAINTILETYPE_DEEPSEA			= 1
TERRAINTILETYPE_SEA				= 2
TERRAINTILETYPE_BEACH			= 3
TERRAINTILETYPE_PLAIN			= 4
TERRAINTILETYPE_FOREST			= 5
TERRAINTILETYPE_MOUNTAIN_SIDE	= 6
TERRAINTILETYPE_MOUNTAIN_TOP	= 7

coord = Tuple[int, int]
type = Dict[str, int | coord]
ressource_type = None

def init(type: int, position: coord, height: int) -> type:
	return {
		"type": type,
		"position": position,
		"height": height,
		"ressource": None,
	}

def init_deepsea(position: coord, height: float):
	res = init(TERRAINTILETYPE_DEEPSEA, position, height)

def type(tile: type) -> int:
	return tile["type"]

def position(tile: type) -> coord:
	return tile["position"]

def height(tile: type) -> int:
	return tile["height"]

def ressource(tile: type) -> int:
	return tile["ressource"]

def render(tile: Dict[str, int | coord]):
	h = height(tile) % 4 * 16
	match type(tile):
		case 1: #TERRAINTILETYPE_DEEPSEA
			return (0, 0, 255 + height(tile) * 4)
		case 2: #TERRAINTILETYPE_SEA
			return (0, 0, 255 + height(tile) * 4)
		case 3: #TERRAINTILETYPE_BEACH
			return (255 - h, 255 - h, 0)
		case 4: #TERRAINTILETYPE_PLAIN
			return (0, 255 - h, 0)
		case 5: #TERRAINTILETYPE_FOREST
			return (64 - h, 128 - h, 0)
		case 6: #TERRAINTILETYPE_MOUNTAIN_SIDE
			return (150 - h, 150 - h, 150 - h)
		case 7: # TERRAINTILETYPE_MOUNTAIN_TOP
			return (255 - h, 255 - h, 255 - h)
		case _:
			return (0, 0, 0)
		
