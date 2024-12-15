from model.terrain.TerrainTile import TerrainTile, TerrainTileType
from ui import Screenmode
from ui import Zoom
from .ressource import draw_ressource
from ui.framework import drawRect, drawImage

drawTerrainTileMap = {
	TerrainTileType.DEEPSEA			: ('Deep sea',		lambda rect, h, h4: drawRect(rect, (0, 0, 255 + h * 4))),
	TerrainTileType.SEA				: ('Sea',			lambda rect, h, h4: drawRect(rect, (0, 0, 255 + h * 4))),
	TerrainTileType.BEACH			: ('Beach',			lambda rect, h, h4: drawImage('sand', rect)),
	TerrainTileType.PLAIN			: ('Plain',			lambda rect, h, h4: drawImage('grass', rect)),
	TerrainTileType.FOREST			: ('Forest',		lambda rect, h, h4: drawImage('wood', rect)),
	TerrainTileType.MOUNTAIN_SIDE	: ('Moutain Side',	lambda rect, h, h4: drawImage('stone', rect)),
	TerrainTileType.MOUNTAIN_TOP	: ('Montain Top',	lambda rect, h, h4: drawImage('snow', rect)),
}

def print_terrain_tile(tile: TerrainTile):
	return drawTerrainTileMap.get(
		tile.type,
		lambda rect, h, h4: ('', drawRect(rect, (0, 0, 0)))
	)[0]

def draw_terrain(tile: TerrainTile):
	func = drawTerrainTileMap.get(
		tile.type,
		lambda rect, h, h4: ('', drawRect(rect, (0, 0, 0)))
	)[1]
	h = tile.height
	h4 = h % 4 * 16
	if tile.ressource != None:
		ressource_func = draw_ressource(tile.ressource)

		def res(rect, h=h, h4=h4):
			if Zoom.opti_factor <= 1:
				ressource_func(rect)
			else:
				func(rect, h, h4)
		return res
	else:
		return lambda rect, h=h, h4=h4: func(rect, h, h4)

def draw_background_stat(tile: TerrainTile):
	h = tile.height
	h4 = h % 8 * 8
	if (h < 0):
		return lambda rect, h=h, h4=h4: drawRect(rect, (0, 0, 180 + h * 4))
	else:
		return lambda rect, h=h, h4=h4: drawRect(rect, (80 - h4, 80 - h4, 80 - h4))

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

def draw_terrain_tile(tile: TerrainTile):
	terrain = draw_terrain(tile)
	color = draw_background_stat(tile)
	return lambda rect, terrain=terrain, color=color: _draw_terrain_tile(rect, terrain, color)