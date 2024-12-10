from ui import Screenmode
from model.terrain import TerrainTile
from ui import Zoom
from .ressource import ui_map_ressource_draw_ressource
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.image import ui_framework_image_drawImage

ui_map_terrainTile_drawTerrainTileMap = {
	TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_DEEPSEA			: ('Deep sea',		lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 0, 255 + h * 4))),
	TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_SEA				: ('Sea',			lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 0, 255 + h * 4))),
	TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH			: ('Beach',			lambda rect, h, h4: ui_framework_image_drawImage('sand', rect)),
	TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN			: ('Plain',			lambda rect, h, h4: ui_framework_image_drawImage('grass', rect)),
	TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST			: ('Forest',		lambda rect, h, h4: ui_framework_image_drawImage('wood', rect)),
	TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE	: ('Moutain Side',	lambda rect, h, h4: ui_framework_image_drawImage('stone', rect)),
	TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_TOP	: ('Montain Top',	lambda rect, h, h4: ui_framework_image_drawImage('snow', rect)),
}

def ui_map_terrainTile_print_terrain_tile(tile: TerrainTile.model_terrain_terrainTile_types):
	return ui_map_terrainTile_drawTerrainTileMap.get(
		TerrainTile.model_terrain_terrainTile_type(tile),
		lambda rect, h, h4: ('', ui_framework_draw_drawRect(rect, (0, 0, 0)))
	)[0]

def ui_map_terrainTile_draw_terrain(tile: TerrainTile.model_terrain_terrainTile_types):
	func = ui_map_terrainTile_drawTerrainTileMap.get(
		TerrainTile.model_terrain_terrainTile_type(tile),
		lambda rect, h, h4: ('', ui_framework_draw_drawRect(rect, (0, 0, 0)))
	)[1]
	h = TerrainTile.model_terrain_terrainTile_height(tile)
	h4 = h % 4 * 16
	if TerrainTile.model_terrain_terrainTile_ressource(tile) != None:
		ressource_func = ui_map_ressource_draw_ressource(TerrainTile.model_terrain_terrainTile_ressource(tile))

		def res(rect, h=h, h4=h4):
			if Zoom.Zoom_opti_factor <= 1:
				ressource_func(rect)
			else:
				func(rect, h, h4)
		return res
	else:
		return lambda rect, h=h, h4=h4: func(rect, h, h4)

def ui_map_terrainTile_draw_background_stat(tile: TerrainTile.model_terrain_terrainTile_types):
	h = TerrainTile.model_terrain_terrainTile_height(tile)
	h4 = h % 8 * 8
	if (h < 0):
		return lambda rect, h=h, h4=h4: ui_framework_draw_drawRect(rect, (0, 0, 180 + h * 4))
	else:
		return lambda rect, h=h, h4=h4: ui_framework_draw_drawRect(rect, (80 - h4, 80 - h4, 80 - h4))

def ui_map_terrainTile__draw_terrain_tile(rect, terrain, color):
	match Screenmode.SCREENMODE_val:
		case Screenmode.SCREENMODE_MAIN:
			return terrain(rect)
		case Screenmode.SCREENMODE_ECONOMY_DEMAND\
			| Screenmode.SCREENMODE_ECONOMY_SUPPLY\
			| Screenmode.SCREENMODE_TRANSPORT:
			return color(rect)
		case _:
			return None

def ui_map_terrainTile_draw_terrain_tile(tile: TerrainTile.model_terrain_terrainTile_types):
	terrain = ui_map_terrainTile_draw_terrain(tile)
	color = ui_map_terrainTile_draw_background_stat(tile)
	return lambda rect, terrain=terrain, color=color: ui_map_terrainTile__draw_terrain_tile(rect, terrain, color)