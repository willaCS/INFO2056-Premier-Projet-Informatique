import Window
from ui import Cursor
from model.industry import plants
from model.terrain.terrain import model_terrain_terrain_get_terrain_tile
from ui import SelectedTile, Zoom
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.image import ui_framework_image_drawImage
from ui.map.industry import ui_map_industry_draw_industry_map
from ui.map.terrainTile import ui_map_terrainTile_draw_terrain_tile
from utils.cache import utils_cache_add_cache
from ui.map.utils import ui_map_utils_coord_to_px
from utils.mytyping import utils_myTyping_Color, utils_myTyping_coord_i
from ui import visual_config as vc

@utils_cache_add_cache
def ui_map_map__drawTerrain(coord: utils_myTyping_coord_i):
	terrainTile = model_terrain_terrain_get_terrain_tile(coord)
	return ui_map_terrainTile_draw_terrain_tile(terrainTile)

@utils_cache_add_cache
def ui_map_map_drawTile(tile_coord: utils_myTyping_coord_i):
	tile = plants.model_plants_get(tile_coord)
	if not tile: return None

	print(tile)

	return ui_map_industry_draw_industry_map(tile)

def ui_map_map__drawTileOutline(color: utils_myTyping_Color, coord: utils_myTyping_coord_i):
	new_coord = ui_map_utils_coord_to_px(coord)
	ui_framework_draw_drawRect((
			(new_coord[0], int(new_coord[1] - Zoom.Zoom_tile_size)),
			(int(Zoom.Zoom_tile_size), int(Zoom.Zoom_tile_size))
		),
		color,
		outline=int(Zoom.Zoom_outline_width),
	)

def ui_map_map_drawMap(rect):
	x_min = int(-Window.Window_half_resolution[0] / Zoom.Zoom_tile_size - Cursor.Cursor_val[0]) // Zoom.Zoom_opti_factor - 2
	x_max = int( Window.Window_half_resolution[0] / Zoom.Zoom_tile_size - Cursor.Cursor_val[0]) // Zoom.Zoom_opti_factor + 2
	y_min = int(-Window.Window_half_resolution[1] / Zoom.Zoom_tile_size - Cursor.Cursor_val[1]) // Zoom.Zoom_opti_factor - 2
	y_max = int( Window.Window_half_resolution[1] / Zoom.Zoom_tile_size - Cursor.Cursor_val[1]) // Zoom.Zoom_opti_factor + 2
	
	# Draw Terrain
	for i in range(x_min, x_max):
		for j in range(y_min, y_max):
			coord = (i * Zoom.Zoom_opti_factor, j * Zoom.Zoom_opti_factor)
			screen_coord = ui_map_utils_coord_to_px(coord)
			tile_size = int(Zoom.Zoom_tile_size * Zoom.Zoom_opti_factor)
			rect = (
				(screen_coord[0], screen_coord[1] - int(Zoom.Zoom_tile_size)),
				(int(tile_size) + 1, int(tile_size) + 1)
			)
			ui_map_map__drawTerrain(coord)(rect)
	
	# Draw Buildings
	for tile_coord in plants.model_plants_map.keys():
		if x_min * Zoom.Zoom_opti_factor > tile_coord[0] or tile_coord[0] > x_max * Zoom.Zoom_opti_factor\
			or y_min * Zoom.Zoom_opti_factor > tile_coord[1] or tile_coord[1] > y_max * Zoom.Zoom_opti_factor:
			continue
		screen_coord = ui_map_utils_coord_to_px(tile_coord)
		rect = (
			(screen_coord[0], screen_coord[1] - int(Zoom.Zoom_tile_size)),
			(int(Zoom.Zoom_tile_size) + 1, int(Zoom.Zoom_tile_size) + 1)
		)
		ui_map_map_drawTile(tile_coord)(rect)
	
	# Draw Selected Tile
	if SelectedTile.SelectedTile_val:
		ui_map_map__drawTileOutline((255, 255, 255), SelectedTile.SelectedTile_val)
