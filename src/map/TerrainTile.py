"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

from globals import Screenmode, Zoom
from map import Ressource
from ui.utils import image
from ui.utils.draw import drawRect

TERRAINTILETYPE_DEEPSEA			= 1
TERRAINTILETYPE_SEA				= 2
TERRAINTILETYPE_BEACH			= 3
TERRAINTILETYPE_PLAIN			= 4
TERRAINTILETYPE_FOREST			= 5
TERRAINTILETYPE_MOUNTAIN_SIDE	= 6
TERRAINTILETYPE_MOUNTAIN_TOP	= 7

coord = Tuple[int, int]
types = Dict[str, int | coord | Ressource.types | None]

def init(type: int, position: coord, height: int) -> types:
	return {
		"type": type,
		"position": position,
		"height": height,
		"ressource": None,
	}

def type(tile: types) -> int:
	return tile["type"]

def position(tile: types) -> coord:
	return tile["position"]

def height(tile: types) -> int:
	return tile["height"]

def ressource(tile: types) -> Ressource.types | None:
	return tile["ressource"]

drawTerrainTileMap = {
	TERRAINTILETYPE_DEEPSEA			: lambda rect, h, h4: drawRect(rect, (       0,        0, 255 + h * 4)),
	TERRAINTILETYPE_SEA				: lambda rect, h, h4: drawRect(rect, (       0,        0, 255 + h * 4)),
	TERRAINTILETYPE_BEACH			: lambda rect, h, h4: image.draw('sand', rect),
	TERRAINTILETYPE_PLAIN			: lambda rect, h, h4: image.draw('grass', rect),
	TERRAINTILETYPE_FOREST			: lambda rect, h, h4: image.draw('wood', rect),
	TERRAINTILETYPE_MOUNTAIN_SIDE	: lambda rect, h, h4: image.draw('stone', rect),
	TERRAINTILETYPE_MOUNTAIN_TOP	: lambda rect, h, h4: image.draw('snow', rect),
}

def draw_terrain(tile: types):
	func = drawTerrainTileMap.get(
		type(tile),
		lambda rect, h, h4: drawRect(rect, (0, 0, 0))
	)
	h = height(tile)
	h4 = h % 4 * 16
	if ressource(tile) != None:
		ressource_func = Ressource.draw(ressource(tile))

		def res(rect, h=h, h4=h4):
			if Zoom.opti_factor <= 1:
				ressource_func(rect)
			else:
				# print(position(tile))
				func(rect, h, h4)
		return res
	else:
		return lambda rect, h=h, h4=h4: func(rect, h, h4)

def draw_background_stat(tile: types):
	h = height(tile)
	h4 = h % 8 * 8
	if (h < 0):
		return lambda rect, h=h, h4=h4: drawRect(rect, (0, 0, 180 + h * 4))
	else:
		return lambda rect, h=h, h4=h4: drawRect(rect, (80 - h4, 80 - h4, 80 - h4))


def draw_(rect, terrain, color):
	match Screenmode.val:
		case Screenmode.SCREENMODE_MAIN:
			return terrain(rect)
		case Screenmode.SCREENMODE_ECONOMY_DEMAND\
			| Screenmode.SCREENMODE_ECONOMY_SUPPLY\
			| Screenmode.SCREENMODE_TRANSPORT:
			return color(rect)
		case _:
			return None

def draw(tile: types):
	terrain = draw_terrain(tile)
	color = draw_background_stat(tile)
	return lambda rect, terrain=terrain, color=color: draw_(rect, terrain, color)