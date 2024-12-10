"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

model_Plant_coord = Tuple[int, int]
model_Plant_types = Dict[str, int | model_Plant_coord]

def model_Plant_init(type: int, position: model_Plant_coord) -> model_Plant_types:
	return {
		"type": type,
		"position": position,
		"xp": 0,
		"generated": 0
	}

def model_Plant_type(tile: model_Plant_types) -> int:
	return tile["type"]

def model_Plant_position(tile: model_Plant_types) -> model_Plant_coord:
	return tile["position"]

def model_Plant_xp(tile: model_Plant_types) -> int:
	return tile["xp"]

def model_Plant_generated(tile: model_Plant_types) -> int:
	return tile["generated"]