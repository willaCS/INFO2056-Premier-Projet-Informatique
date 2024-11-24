"""
Ce fichier gère une structure pour les cases appelées tile.
Une case est une structure ayant ces variables :
	type: TILETYPE
	position: [int, int]
"""

from typing import Dict, Tuple

from globals import all
from map import Industry
from ui.utils.draw import drawRect

coord = Tuple[int, int]
types = Dict[str, int | coord]

TILETYPE_EMPTY			= 0
TILETYPE_TRANSPORT		= 1
TILETYPE_TRANSPORTHUB	= 2
TILETYPE_INDUSTRY		= 3
TILETYPE_CITY			= 4
TILETYPE_CITYCENTER		= 5

def init(type: int, subtype: int, position: coord) -> types:
	return {
		"type": type,
		"subtype": subtype,
		"position": position,
	}

def type(tile: types) -> int:
	return tile["type"]

def subtype(tile: types) -> int:
	return tile["subtype"]

def position(tile: types) -> coord:
	return tile["position"]

drawFunc = {
	TILETYPE_EMPTY			: (False, lambda rect: rect(rect, (  0,   0,   0))),
	TILETYPE_TRANSPORT		: (False, lambda rect: rect(rect, ( 76,  87,  97))),
	TILETYPE_CITY			: (False, lambda rect: rect(rect, ( 22,  17,  84))),
	TILETYPE_CITYCENTER		: (False, lambda rect: rect(rect, (163,  28,  53))),
	TILETYPE_TRANSPORTHUB	: (False, lambda rect: rect(rect, all.COLOR_RED)),
	TILETYPE_INDUSTRY		: (True,  lambda tile: Industry.draw_industry(subtype(tile))),
}

def draw(tile: types):
	func = drawFunc.get(
		type(tile),
		lambda rect: rect(rect, (0, 0, 0))
	)
	func = func[1](tile) if func[0] else func[1]
	return lambda rect: func(rect)
