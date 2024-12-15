from model.terrain.Ressource import Ressource, RessourceType
from ui.framework import drawRect, drawImage

ressourceDrawMap = {
	RessourceType.FISH:            ('fish'           , lambda rect, h, h4: drawRect(rect, (0, 0, 230 + h*4))),
	RessourceType.SALT:            ('salt'           , lambda rect, h, h4: drawImage('salt', rect)),
	RessourceType.FERTILE_LAND:    ('fertile land'   , lambda rect, h, h4: drawImage('fertile_land', rect)),
	RessourceType.HUNTING_GROUNDS: ('fur'            , lambda rect, h, h4: drawRect(rect, (0, 82, 0))),
	RessourceType.WOOD:            ('wood'           , lambda rect, h, h4: drawImage('wood', rect)),
	RessourceType.OIL:             ('oil'            , lambda rect, h, h4: drawImage('oil', rect)),
	RessourceType.COAL:            ('coal'           , lambda rect, h, h4: drawImage('coal', rect)),
	RessourceType.IRON:            ('iron'           , lambda rect, h, h4: drawImage('iron', rect) if h < 35 else drawImage('iron2', rect)),
	RessourceType.COPPER:          ('copper'         , lambda rect, h, h4: drawImage('copper', rect)),
	RessourceType.PRECIOUS_METALS: ('precious metals', lambda rect, h, h4: drawImage('precious', rect)),
	RessourceType.RARE_METALS:     ('rare metals'    , lambda rect, h, h4: drawImage('rare', rect)),
	RessourceType.SAND:            ('sand'           , lambda rect, h, h4: drawImage('sand', rect)),
	RessourceType.STONE:           ('stone'          , lambda rect, h, h4: drawImage('stone', rect)),							
}

def print_ressource(ressource: Ressource):
	return ressourceDrawMap[ressource.type][0]

def draw_ressource(tile: Ressource):
	func = ressourceDrawMap.get(
		tile.type,
		('', lambda rect, h, h4: drawRect(rect, (0, 0, 0)))
	)[1]
	h = tile.height
	return lambda rect, h=h, h4=h % 4 * 16: func(rect, h, h4)