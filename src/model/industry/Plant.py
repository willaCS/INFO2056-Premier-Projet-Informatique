"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

coord = Tuple[int, int]
types = Dict[str, int | coord]

def init(type: int, position: coord) -> types:
	return {
		"type": type,
		"position": position,
		"xp": 0,
		"generated": 0
	}

def type(tile: types) -> int:
	return tile["type"]

def position(tile: types) -> coord:
	return tile["position"]

def xp(tile: types) -> int:
	return tile["xp"]

def generated(tile: types) -> int:
	return tile["generated"]