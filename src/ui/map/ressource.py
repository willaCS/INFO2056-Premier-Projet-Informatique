from model.terrain import Ressource
from ui.framework import drawRect, drawImage

ressourceDrawMap = {
	Ressource.RESSOURCE_FISH:            ('fish'           , lambda rect, h, h4: drawRect(rect, (0, 0, 230 + h*4))),
	Ressource.RESSOURCE_SALT:            ('salt'           , lambda rect, h, h4: drawImage('salt', rect)),
	Ressource.RESSOURCE_FERTILE_LAND:    ('fertile land'   , lambda rect, h, h4: drawImage('fertile_land', rect)),
	Ressource.RESSOURCE_HUNTING_GROUNDS: ('fur'            , lambda rect, h, h4: drawRect(rect, (0, 82, 0))),
	Ressource.RESSOURCE_WOOD:            ('wood'           , lambda rect, h, h4: drawImage('wood', rect)),
	Ressource.RESSOURCE_OIL:             ('oil'            , lambda rect, h, h4: drawImage('oil', rect)),
	Ressource.RESSOURCE_COAL:            ('coal'           , lambda rect, h, h4: drawImage('coal', rect)),
	Ressource.RESSOURCE_IRON:            ('iron'           , lambda rect, h, h4: drawImage('iron', rect) if h < 35 else drawImage('iron2', rect)),
	Ressource.RESSOURCE_COPPER:          ('copper'         , lambda rect, h, h4: drawImage('copper', rect)),
	Ressource.RESSOURCE_PRECIOUS_METALS: ('precious metals', lambda rect, h, h4: drawImage('precious', rect)),
	Ressource.RESSOURCE_RARE_METALS:     ('rare metals'    , lambda rect, h, h4: drawImage('rare', rect)),
	Ressource.RESSOURCE_SAND:            ('sand'           , lambda rect, h, h4: drawImage('sand', rect)),
	Ressource.RESSOURCE_STONE:           ('stone'          , lambda rect, h, h4: drawImage('stone', rect)),							
}

def print_ressource(type):
	return ressourceDrawMap[type][0]

def draw_ressource(tile):
	func = ressourceDrawMap.get(
		Ressource.type(tile),
		('', lambda rect, h, h4: drawRect(rect, (0, 0, 0)))
	)[1]
	h = Ressource.height(tile)
	return lambda rect, h=h, h4=h % 4 * 16: func(rect, h, h4)