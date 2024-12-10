from typing import Dict

model_terrain_ressource_RESSOURCE_FISH				= 1
model_terrain_ressource_RESSOURCE_SALT				= 2
model_terrain_ressource_RESSOURCE_FERTILE_LAND		= 3
model_terrain_ressource_RESSOURCE_HUNTING_GROUNDS	= 4
model_terrain_ressource_RESSOURCE_WOOD				= 5
model_terrain_ressource_RESSOURCE_OIL				= 6
model_terrain_ressource_RESSOURCE_COAL				= 7
model_terrain_ressource_RESSOURCE_IRON				= 8
model_terrain_ressource_RESSOURCE_COPPER			= 9
model_terrain_ressource_RESSOURCE_PRECIOUS_METALS	= 10
model_terrain_ressource_RESSOURCE_RARE_METALS		= 11
model_terrain_ressource_RESSOURCE_SAND				= 12
model_terrain_ressource_RESSOURCE_STONE				= 13

model_terrain_ressource_types = Dict[str, int | str]

def model_terrain_ressource_init(type: int, richness: int, height: int) -> model_terrain_ressource_types:
	return {
		"type": type,
		"richness": 0,
		"height": height,
	}

def model_terrain_ressource_type(tile: model_terrain_ressource_types) -> int:
	return tile["type"] # type: ignore

def model_terrain_ressource_richness(tile: model_terrain_ressource_types) -> int:
	return tile["richness"] # type: ignore

def model_terrain_ressource_height(tile: model_terrain_ressource_types) -> int:
	return tile["height"] # type: ignore

