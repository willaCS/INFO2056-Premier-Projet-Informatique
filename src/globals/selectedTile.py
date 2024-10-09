"""
Ce fichier gère la case selectionnée sur la carte.
"""

from typing import Tuple

from utils.map import px_to_coord

val = None

def select(screen_coord: Tuple[int, int]):
	global val

	coord = px_to_coord(screen_coord)
	val = (
		int(coord[0]) if coord[0] > 0 else int(coord[0]) - 1,
		int(coord[1]) if coord[1] > 0 else int(coord[1]) - 1
	)

def clear():
	global val
	val = None