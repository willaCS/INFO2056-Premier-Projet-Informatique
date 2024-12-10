"""
Ce fichier gère la case selectionnée sur la carte.
"""

from ui.map.utils import ui_map_utils_px_to_coord
from utils.mytyping import utils_myTyping_coord_i

SelectedTile_val: utils_myTyping_coord_i | None = None

def SelectedTile_select(screen_coord: utils_myTyping_coord_i):
	global SelectedTile_val

	coord = ui_map_utils_px_to_coord(screen_coord)
	SelectedTile_val = (
		int(coord[0]) if coord[0] > 0 else int(coord[0]) - 1,
		int(coord[1]) if coord[1] > 0 else int(coord[1]) - 1
	)

def SelectedTile_clear():
	global SelectedTile_val
	SelectedTile_val = None