from typing import Dict, Tuple

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

coord = Tuple[int, int]
type = Dict[str, int | str]

def init(type: int, richness: int) -> type:
	return {
		"type": type,
		"richness": richness,
	}