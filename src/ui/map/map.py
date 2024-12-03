import Window
from ui import Cursor
from model.industry import plants
from model.terrain.terrain import get_terrain_tile
from ui import SelectedTile, Zoom
from ui.framework import drawRect
from ui.map import draw_industry, draw_terrain_tile
from utils.cache import add_cache
from ui.map.utils import coord_to_px
from utils.mytyping import Color, coord_i
from ui import visual_config as vc

@add_cache
def _drawTerrain(coord: coord_i):
	terrainTile = get_terrain_tile(coord)
	return draw_terrain_tile(terrainTile)

@add_cache
def drawTile(tile_coord: coord_i):
	tile = plants.get(tile_coord)
	if not tile: return None

	print(tile)

	return draw_industry(tile)

def _drawTileOutline(color: Color, coord: coord_i):
	new_coord = coord_to_px(coord)
	drawRect((
			(new_coord[0], int(new_coord[1] - Zoom.tile_size)),
			(int(Zoom.tile_size), int(Zoom.tile_size))
		),
		color,
		outline=int(Zoom.outline_width),
	)

def drawMap(rect):
	x_min = int(-Window.half_resolution[0] / Zoom.tile_size - Cursor.val[0]) // Zoom.opti_factor - 2
	x_max = int( Window.half_resolution[0] / Zoom.tile_size - Cursor.val[0]) // Zoom.opti_factor + 2
	y_min = int(-Window.half_resolution[1] / Zoom.tile_size - Cursor.val[1]) // Zoom.opti_factor - 2
	y_max = int( Window.half_resolution[1] / Zoom.tile_size - Cursor.val[1]) // Zoom.opti_factor + 2
	
	# Draw Terrain
	for i in range(x_min, x_max):
		for j in range(y_min, y_max):
			coord = (i * Zoom.opti_factor, j * Zoom.opti_factor)
			screen_coord = coord_to_px(coord)
			tile_size = int(Zoom.tile_size * Zoom.opti_factor)
			rect = (
				(screen_coord[0], screen_coord[1] - int(Zoom.tile_size)),
				(int(tile_size) + 1, int(tile_size) + 1)
			)
			_drawTerrain(coord)(rect)
	
	# Draw Buildings
	for tile_coord in plants.map.keys():
		if x_min * Zoom.opti_factor > tile_coord[0] or tile_coord[0] > x_max * Zoom.opti_factor\
			or y_min * Zoom.opti_factor > tile_coord[1] or tile_coord[1] > y_max * Zoom.opti_factor:
			continue
		screen_coord = coord_to_px(tile_coord)
		rect = (
			(screen_coord[0], screen_coord[1] - int(Zoom.tile_size)),
			(int(Zoom.tile_size) + 1, int(Zoom.tile_size) + 1)
		)
		drawTile(tile_coord)(rect)
	
	# Draw Selected Tile
	if SelectedTile.val:
		_drawTileOutline((255, 255, 255), SelectedTile.val)
