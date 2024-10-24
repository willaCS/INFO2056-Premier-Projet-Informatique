"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

coord = Tuple[int, int]
types = Dict[str, int | coord]

TILETYPE_EMPTY			= 0
TILETYPE_TRANSPORT		= 1
TILETYPE_TRANSPORTHUB	= 2
TILETYPE_INDUSTRY		= 3
TILETYPE_CITY			= 4
TILETYPE_CITYCENTER		= 5

def init(type: int, subtype: int, position: coord) -> types:
	return {
		"type": type,
		"subtype": subtype,
		"position": position,
	}

def type(tile: types) -> int:
	return tile["type"] # type: ignore

def subtype(tile: types) -> int:
	return tile["subtype"] # type: ignore

def position(tile: types) -> coord:
	return tile["position"] # type: ignore
