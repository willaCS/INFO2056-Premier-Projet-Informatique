from typing import Dict

RESSOURCE_FISH				= 1
RESSOURCE_SALT				= 2
RESSOURCE_FERTILE_LAND		= 3
RESSOURCE_HUNTING_GROUNDS	= 4
RESSOURCE_WOOD				= 5
RESSOURCE_OIL				= 6
RESSOURCE_COAL				= 7
RESSOURCE_IRON				= 8
RESSOURCE_COPPER			= 9
RESSOURCE_PRECIOUS_METALS	= 10
RESSOURCE_RARE_METALS		= 11
RESSOURCE_SAND				= 12
RESSOURCE_STONE				= 13

types = Dict[str, int | str]

def init(type: int, richness: int, height: int) -> types:
	return {
		"type": type,
		"richness": richness,
		"height": height,
	}

def type(tile: types) -> int:
	return tile["type"] # type: ignore

def richness(tile: types) -> int:
	return tile["richness"] # type: ignore

def height(tile: types) -> int:
	return tile["height"] # type: ignore

def print_ressource(type):
	if type == RESSOURCE_FISH:
		return 'fish'
	elif type == RESSOURCE_SALT:
		return 'salt'
	elif type == RESSOURCE_FERTILE_LAND:
		return 'fertile land'
	elif type == RESSOURCE_HUNTING_GROUNDS:
		return 'fur'
	elif type == RESSOURCE_WOOD:
		return 'wood'
	elif type == RESSOURCE_OIL:
		return 'oil'
	elif type == RESSOURCE_COAL:
		return 'coal'
	elif type == RESSOURCE_IRON:
		return 'iron'
	elif type == RESSOURCE_COPPER:
		return 'copper'
	elif type == RESSOURCE_PRECIOUS_METALS:
		return 'precious metals'
	elif type == RESSOURCE_RARE_METALS:
		return 'rare metals'
	elif type == RESSOURCE_SAND:
		return 'sand'
	elif type == RESSOURCE_STONE:
		return 'stone'
	else:
		return 'unknown'
