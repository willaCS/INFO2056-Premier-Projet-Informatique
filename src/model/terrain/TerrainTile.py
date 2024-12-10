"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

from model.terrain import Ressource

model_terrain_terrainTile_TERRAINTILETYPE_DEEPSEA			= 1
model_terrain_terrainTile_TERRAINTILETYPE_SEA				= 2
model_terrain_terrainTile_TERRAINTILETYPE_BEACH			= 3
model_terrain_terrainTile_TERRAINTILETYPE_PLAIN			= 4
model_terrain_terrainTile_TERRAINTILETYPE_FOREST			= 5
model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE	= 6
model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_TOP	= 7

model_terrain_terrainTile_coord = Tuple[int, int]
model_terrain_terrainTile_types = Dict[str, int | model_terrain_terrainTile_coord | Ressource.model_terrain_ressource_types | None]

def model_terrain_terrainTile_init(type: int, position: model_terrain_terrainTile_coord, height: int) -> model_terrain_terrainTile_types:
	return {
		"type": type,
		"position": position,
		"height": height,
		"ressource": None,
	}

def model_terrain_terrainTile_type(tile: model_terrain_terrainTile_types) -> int:
	return tile["type"]

def model_terrain_terrainTile_position(tile: model_terrain_terrainTile_types) -> model_terrain_terrainTile_coord:
	return tile["position"]

def model_terrain_terrainTile_height(tile: model_terrain_terrainTile_types) -> int:
	return tile["height"]

def model_terrain_terrainTile_ressource(tile: model_terrain_terrainTile_types) -> Ressource.model_terrain_ressource_types | None:
	return tile["ressource"]
