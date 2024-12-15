from enum import Enum
from typing import Dict

class RessourceType(Enum):
	FISH			= 1
	SALT			= 2
	FERTILE_LAND	= 3
	HUNTING_GROUNDS	= 4
	WOOD			= 5
	OIL				= 6
	COAL			= 7
	IRON			= 8
	COPPER			= 9
	PRECIOUS_METALS	= 10
	RARE_METALS		= 11
	SAND			= 12
	STONE			= 13

types = Dict[str, int | str]

class Ressource:
	def __init__(self, type: RessourceType, richness: int, height: int):
		self.type		= type
		self.richness	= 0
		self.height		= height

