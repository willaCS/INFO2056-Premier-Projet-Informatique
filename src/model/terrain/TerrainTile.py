"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from enum import Enum
from typing import Dict, Tuple

from model.terrain.Ressource import Ressource

class TerrainTileType(Enum):
	DEEPSEA			= 1
	SEA				= 2
	BEACH			= 3
	PLAIN			= 4
	FOREST			= 5
	MOUNTAIN_SIDE	= 6
	MOUNTAIN_TOP	= 7

class TerrainTile:
	def __init__(self, _type: TerrainTileType, position, height: int):
		self.type = _type
		self.position = position
		self.height = height
		self.ressource: Ressource = None

