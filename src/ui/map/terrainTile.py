from ui import Screenmode
from model.terrain import TerrainTile
from ui import Zoom
from .ressource import draw_ressource

drawTerrainTileMap = {
	TerrainTile.TERRAINTILETYPE_DEEPSEA			: ('Deep sea',		lambda rect, window, h, h4: window.draw_rect(rect, (0, 0, 255 + h * 4))),
	TerrainTile.TERRAINTILETYPE_SEA				: ('Sea',			lambda rect, window, h, h4: window.draw_rect(rect, (0, 0, 255 + h * 4))),
	TerrainTile.TERRAINTILETYPE_BEACH			: ('Beach',			lambda rect, window, h, h4: window.draw_image('sand', rect)),
	TerrainTile.TERRAINTILETYPE_PLAIN			: ('Plain',			lambda rect, window, h, h4: window.draw_image('grass', rect)),
	TerrainTile.TERRAINTILETYPE_FOREST			: ('Forest',		lambda rect, window, h, h4: window.draw_image('wood', rect)),
	TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE	: ('Moutain Side',	lambda rect, window, h, h4: window.draw_image('stone', rect)),
	TerrainTile.TERRAINTILETYPE_MOUNTAIN_TOP	: ('Montain Top',	lambda rect, window, h, h4: window.draw_image('snow', rect)),
}

def print_terrain_tile(tile: TerrainTile.types):
	return drawTerrainTileMap.get(
		TerrainTile.type(tile),
		lambda rect, window, h, h4: ('', window.draw_rect(rect, (0, 0, 0)))
	)[0]

def draw_terrain(tile: TerrainTile.types):
	func = drawTerrainTileMap.get(
		TerrainTile.type(tile),
		lambda rect, window, h, h4: ('', window.draw_rect(rect, (0, 0, 0)))
	)[1]
	h = TerrainTile.height(tile)
	h4 = h % 4 * 16
	if TerrainTile.ressource(tile) != None:
		ressource_func = draw_ressource(TerrainTile.ressource(tile))

		def res(rect, h=h, h4=h4):
			if Zoom.opti_factor <= 1:
				ressource_func(rect)
			else:
				func(rect, h, h4)
		return res
	else:
		return lambda rect, h=h, h4=h4: func(rect, h, h4)

def draw_background_stat(tile: TerrainTile.types):
	h = TerrainTile.height(tile)
	h4 = h % 8 * 8
	if (h < 0):
		return lambda rect, window, h=h, h4=h4: window.draw_rect(rect, (0, 0, 180 + h * 4))
	else:
		return lambda rect, window, h=h, h4=h4: window.draw_rect(rect, (80 - h4, 80 - h4, 80 - h4))

def _draw_terrain_tile(rect, terrain, color):
	match Screenmode.val:
		case Screenmode.SCREENMODE_MAIN:
			return terrain(rect)
		case Screenmode.SCREENMODE_ECONOMY_DEMAND\
			| Screenmode.SCREENMODE_ECONOMY_SUPPLY\
			| Screenmode.SCREENMODE_TRANSPORT:
			return color(rect)
		case _:
			return None

def draw_terrain_tile(tile: TerrainTile.types):
	terrain = draw_terrain(tile)
	color = draw_background_stat(tile)
	return lambda rect, terrain=terrain, color=color: _draw_terrain_tile(rect, terrain, color)