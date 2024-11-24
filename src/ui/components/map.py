import Window
from globals import Cursor, SelectedTile, Zoom
from globals.all import COLOR_WHITE
from map import Map, TerrainTile, Tile
from map.generation.map import random_terrain_landscape
from ui.components.topbar import TOP_BAR_HEIGHT
from ui.utils import draw
from ui.utils.ui_array import button_new, composant_new, composant_show
from utils.cache import add_cache
from utils.map import coord_to_px
from utils.mytyping import Color, coord_i

def _drawTileOutline(color: Color, coord: coord_i):
	new_coord = coord_to_px(coord)
	draw.drawRect((
			(new_coord[0], int(new_coord[1] - Zoom.tile_size)),
			(int(Zoom.tile_size), int(Zoom.tile_size))
		),
		color,
		outline=int(Zoom.outline_width),
	)

@add_cache
def _drawTerrain(coord: coord_i):
	terrainTile = random_terrain_landscape(coord)
	return TerrainTile.draw(terrainTile)

@add_cache
def drawTile(tile_coord: coord_i):
	tile = Map.get(tile_coord)
	if not tile: return None

	return Tile.draw(tile)

def _drawMap(rect):
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
	for tile_coord in Map.map.keys():
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
		_drawTileOutline(COLOR_WHITE, SelectedTile.val)

map_component = composant_new(0, [
	# Map
	button_new(
		1,
		lambda: (
			(
				0,
				TOP_BAR_HEIGHT,
			),
			(
				Window.resolution[0],
				Window.resolution[1] - TOP_BAR_HEIGHT
			),
		),
		_drawMap,
		lambda pos: SelectedTile.select(pos),
	),
])

def drawMap():
	composant_show(map_component)
