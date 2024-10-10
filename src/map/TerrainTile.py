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

def init(type: int, position: Tuple[int, int], height: float) -> Dict[str, int | Tuple[int, int] | float]:
	return {
		"type": type,
		"position": position,
		"height": height,
	}

def get_type(tile: Dict[str, int | Tuple[int, int] | float]) -> int:
	return tile["type"]

def get_position(tile: Dict[str, int | Tuple[int, int] | float]) -> Tuple[int, int]:
	return tile["position"]

def get_height(tile: Dict[str, int | Tuple[int, int] | float]) -> float:
	return tile["height"]

def render(tile: Dict[str, int | Tuple[int, int]]):
	height = get_height(tile) % 4 * 16
	match get_type(tile):
		case 1: #TERRAINTILETYPE_DEEPSEA
			return (0, 0, 255 - height)
		case 2: #TERRAINTILETYPE_SEA
			return (0, 0, 255 - height)
		case 3: #TERRAINTILETYPE_BEACH
			return (255 - height, 255 - height, 0)
		case 4: #TERRAINTILETYPE_PLAIN
			return (0, 255 - height, 0)
		case 5: #TERRAINTILETYPE_FOREST
			return (64 - height, 128 - height, 0)
		case 6: #TERRAINTILETYPE_MOUNTAIN_SIDE
			return (150 - height, 150 - height, 150 - height)
		case 7: # TERRAINTILETYPE_MOUNTAIN_TOP
			return (255 - height, 255 - height, 255 - height)
		case _:
			return (0, 0, 0)
		
