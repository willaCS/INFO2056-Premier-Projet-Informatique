"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

from model.terrain import Ressource

TERRAINTILETYPE_DEEPSEA			= 1
TERRAINTILETYPE_SEA				= 2
TERRAINTILETYPE_BEACH			= 3
TERRAINTILETYPE_PLAIN			= 4
TERRAINTILETYPE_FOREST			= 5
TERRAINTILETYPE_MOUNTAIN_SIDE	= 6
TERRAINTILETYPE_MOUNTAIN_TOP	= 7

coord = Tuple[int, int]
types = Dict[str, int | coord | Ressource.types | None]

def init(type: int, position: coord, height: int) -> types:
	return {
		"type": type,
		"position": position,
		"height": height,
		"ressource": None,
	}

def type(tile: types) -> int:
	return tile["type"]

def position(tile: types) -> coord:
	return tile["position"]

def height(tile: types) -> int:
	return tile["height"]

def ressource(tile: types) -> Ressource.types | None:
	return tile["ressource"]
