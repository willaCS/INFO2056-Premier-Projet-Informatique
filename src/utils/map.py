"""
Ce fichier permet de transformer les coordonnée d'un repère à un autre.
On peut faire :
- repère sur la carte => repère sur l'écran
- repère sur l'écran => repère sur la carte
"""

from typing import Tuple

from globals import cursor, zoom
import window

def coord_to_px(coord: Tuple[float, float]) -> Tuple[int, int]:
	return (
		window.half_resolution[0] + int(cursor.val[0] * zoom.tile_size) + (coord[0]) * zoom.tile_size,
		window.half_resolution[1] - int(cursor.val[1] * zoom.tile_size) - (coord[1]) * zoom.tile_size,
	)

def px_to_coord(coord: Tuple[int, int]) -> Tuple[float, float]:
	return (
		(coord[0] - window.half_resolution[0]) / zoom.tile_size - cursor.val[0],
		-((coord[1] - window.half_resolution[1]) / zoom.tile_size + cursor.val[1]),
	)