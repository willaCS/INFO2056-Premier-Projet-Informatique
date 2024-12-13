from model.terrain import Ressource

ressourceDrawMap = {
	Ressource.RESSOURCE_FISH:            ('fish'           , lambda rect, window, h, h4: window.draw_rect(rect, (0, 0, 230 + h*4))),
	Ressource.RESSOURCE_SALT:            ('salt'           , lambda rect, window, h, h4: window.draw_image('salt', rect)),
	Ressource.RESSOURCE_FERTILE_LAND:    ('fertile land'   , lambda rect, window, h, h4: window.draw_image('fertile_land', rect)),
	Ressource.RESSOURCE_HUNTING_GROUNDS: ('fur'            , lambda rect, window, h, h4: window.draw_rect(rect, (0, 82, 0))),
	Ressource.RESSOURCE_WOOD:            ('wood'           , lambda rect, window, h, h4: window.draw_image('wood', rect)),
	Ressource.RESSOURCE_OIL:             ('oil'            , lambda rect, window, h, h4: window.draw_image('oil', rect)),
	Ressource.RESSOURCE_COAL:            ('coal'           , lambda rect, window, h, h4: window.draw_image('coal', rect)),
	Ressource.RESSOURCE_IRON:            ('iron'           , lambda rect, window, h, h4: window.draw_image('iron', rect) if h < 35 else window.draw_image('iron2', rect)),
	Ressource.RESSOURCE_COPPER:          ('copper'         , lambda rect, window, h, h4: window.draw_image('copper', rect)),
	Ressource.RESSOURCE_PRECIOUS_METALS: ('precious metals', lambda rect, window, h, h4: window.draw_image('precious', rect)),
	Ressource.RESSOURCE_RARE_METALS:     ('rare metals'    , lambda rect, window, h, h4: window.draw_image('rare', rect)),
	Ressource.RESSOURCE_SAND:            ('sand'           , lambda rect, window, h, h4: window.draw_image('sand', rect)),
	Ressource.RESSOURCE_STONE:           ('stone'          , lambda rect, window, h, h4: window.draw_image('stone', rect)),							
}

def print_ressource(ressource):
	return ressourceDrawMap[Ressource.type(ressource)][0]

def draw_ressource(tile):
	func = ressourceDrawMap.get(
		Ressource.type(tile),
		('', lambda rect, window, h, h4: window.draw_rect(rect, (0, 0, 0)))
	)[1]
	h = Ressource.height(tile)
	return lambda rect, window, h=h, h4=h % 4 * 16: func(rect, window, h, h4)