from typing import Dict

from ui.utils.draw import drawRect

RESSOURCE_FISH				= 1
RESSOURCE_SALT				= 2
RESSOURCE_FERTILE_LAND		= 3
RESSOURCE_HUNTING_GROUNDS	= 4
RESSOURCE_WOOD				= 5
RESSOURCE_OIL				= 6
RESSOURCE_COAL				= 7
RESSOURCE_IRON				= 8
RESSOURCE_COPPER			= 9
RESSOURCE_PRECIOUS_METALS	= 10
RESSOURCE_RARE_METALS		= 11
RESSOURCE_SAND				= 12
RESSOURCE_STONE				= 13

types = Dict[str, int | str]

def init(type: int, richness: int, height: int) -> types:
	return {
		"type": type,
		"richness": richness,
		"height": height,
	}

def type(tile: types) -> int:
	return tile["type"] # type: ignore

def richness(tile: types) -> int:
	return tile["richness"] # type: ignore

def height(tile: types) -> int:
	return tile["height"] # type: ignore

ressourceDrawMap = {
	RESSOURCE_FISH:            ('fish'           , lambda rect, h, h4: drawRect(rect, (        0,        0, 230 + h*4))),
	RESSOURCE_SALT:            ('salt'           , lambda rect, h, h4: drawRect(rect, (      255,      255,       129))),
	RESSOURCE_FERTILE_LAND:    ('fertile land'   , lambda rect, h, h4: drawRect(rect, ( 134 - h4, 255 - h4,         0))),
	RESSOURCE_HUNTING_GROUNDS: ('fur'            , lambda rect, h, h4: drawRect(rect, (        0,       82,         0))),
	RESSOURCE_WOOD:            ('wood'           , lambda rect, h, h4: drawRect(rect, (        0, 102 + h4,         0))),
	RESSOURCE_OIL:             ('oil'            , lambda rect, h, h4: drawRect(rect, (      191,      196,         0))),
	RESSOURCE_COAL:            ('coal'           , lambda rect, h, h4: drawRect(rect, (       70,       70,        70))),
	RESSOURCE_IRON:            ('iron'           , lambda rect, h, h4: drawRect(rect, (      218,      227,       227))),
	RESSOURCE_COPPER:          ('copper'         , lambda rect, h, h4: drawRect(rect, (      197,      106,        57))),
	RESSOURCE_PRECIOUS_METALS: ('precious metals', lambda rect, h, h4: drawRect(rect, (       78,      226,       236))),
	RESSOURCE_RARE_METALS:     ('rare metals'    , lambda rect, h, h4: drawRect(rect, (       88,      156,        88))),
	RESSOURCE_SAND:            ('sand'           , lambda rect, h, h4: drawRect(rect, ( 255 - h4, 255 - h4,         0))),
	RESSOURCE_STONE:           ('stone'          , lambda rect, h, h4: drawRect(rect, ( 150 - h4, 150 - h4,  150 - h4))),							
}

def print_ressource(type):
	return ressourceDrawMap[type][0]

def draw(tile):
	func = ressourceDrawMap.get(
		type(tile),
		('', lambda rect, h, h4: drawRect(rect, (0, 0, 0)))
	)[1]
	return lambda rect, h=height(tile), h4=height(tile) % 4 * 16: func(rect, h, h4)
