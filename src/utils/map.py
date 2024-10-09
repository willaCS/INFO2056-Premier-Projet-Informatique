from typing import Tuple

import globals.cursor
import globals.zoom
import window

def coord_to_px(coord: Tuple[float, float]) -> Tuple[int, int]:
	return (
		window.half_resolution[0] + int(globals.cursor.val[0] * globals.zoom.tile_size) + (coord[0]) * globals.zoom.tile_size,
		window.half_resolution[1] - int(globals.cursor.val[1] * globals.zoom.tile_size) - (coord[1]) * globals.zoom.tile_size,
	)

def px_to_coord(coord: Tuple[int, int]) -> Tuple[float, float]:
	return (
		(coord[0] - window.half_resolution[0]) / globals.zoom.tile_size - globals.cursor.val[0],
		-((coord[1] - window.half_resolution[1]) / globals.zoom.tile_size + globals.cursor.val[1]),
	)