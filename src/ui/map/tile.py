from globals import all
from map import Tile
from .industry import draw_industry
from ui.framework import drawRect

drawFunc = {
	Tile.TILETYPE_EMPTY			: (False, lambda rect: drawRect(rect, (  0,   0,   0))),
	Tile.TILETYPE_TRANSPORT		: (False, lambda rect: drawRect(rect, ( 76,  87,  97))),
	Tile.TILETYPE_CITY			: (False, lambda rect: drawRect(rect, ( 22,  17,  84))),
	Tile.TILETYPE_CITYCENTER	: (False, lambda rect: drawRect(rect, (163,  28,  53))),
	Tile.TILETYPE_TRANSPORTHUB	: (False, lambda rect: drawRect(rect, all.COLOR_RED)),
	Tile.TILETYPE_INDUSTRY		: (True,  lambda tile: draw_industry(Tile.subtype(tile))),
}

def draw_tile(tile):
	func = drawFunc.get(
		Tile.type(tile),
		lambda rect: rect(rect, (0, 0, 0))
	)
	func = func[1](tile) if func[0] else func[1]
	return lambda rect: func(rect)
