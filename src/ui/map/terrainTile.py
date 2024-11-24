from globals import Screenmode, Zoom
from map import TerrainTile
from .ressource import draw_ressource
from ui.framework import drawRect, drawImage

drawTerrainTileMap = {
	TerrainTile.TERRAINTILETYPE_DEEPSEA			: lambda rect, h, h4: drawRect(rect, (0, 0, 255 + h * 4)),
	TerrainTile.TERRAINTILETYPE_SEA				: lambda rect, h, h4: drawRect(rect, (0, 0, 255 + h * 4)),
	TerrainTile.TERRAINTILETYPE_BEACH			: lambda rect, h, h4: drawImage('sand', rect),
	TerrainTile.TERRAINTILETYPE_PLAIN			: lambda rect, h, h4: drawImage('grass', rect),
	TerrainTile.TERRAINTILETYPE_FOREST			: lambda rect, h, h4: drawImage('wood', rect),
	TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE	: lambda rect, h, h4: drawImage('stone', rect),
	TerrainTile.TERRAINTILETYPE_MOUNTAIN_TOP	: lambda rect, h, h4: drawImage('snow', rect),
}

def draw_terrain(tile: TerrainTile.types):
	func = drawTerrainTileMap.get(
		TerrainTile.type(tile),
		lambda rect, h, h4: drawRect(rect, (0, 0, 0))
	)
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

def draw_terrain_tile(tile: TerrainTile.types):
	terrain = draw_terrain(tile)
	color = draw_background_stat(tile)
	return lambda rect, terrain=terrain, color=color: _draw_terrain_tile(rect, terrain, color)