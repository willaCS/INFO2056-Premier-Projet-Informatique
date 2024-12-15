"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

coord = Tuple[int, int]
types = Dict[str, int | coord]

class Plant:
	def __init__(self, type: int, position: coord) -> types:
		self.type = type
		self.position = position
		self.xp = 0
		self.generated = 0
