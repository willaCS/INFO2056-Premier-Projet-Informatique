from model.terrain import Ressource
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.image import ui_framework_image_drawImage

ui_map_ressource_ressourceDrawMap = {
	Ressource.model_terrain_ressource_RESSOURCE_FISH:            ('fish'           , lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 0, 230 + h*4))),
	Ressource.model_terrain_ressource_RESSOURCE_SALT:            ('salt'           , lambda rect, h, h4: ui_framework_image_drawImage('salt', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_FERTILE_LAND:    ('fertile land'   , lambda rect, h, h4: ui_framework_image_drawImage('fertile_land', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_HUNTING_GROUNDS: ('fur'            , lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 82, 0))),
	Ressource.model_terrain_ressource_RESSOURCE_WOOD:            ('wood'           , lambda rect, h, h4: ui_framework_image_drawImage('wood', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_OIL:             ('oil'            , lambda rect, h, h4: ui_framework_image_drawImage('oil', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_COAL:            ('coal'           , lambda rect, h, h4: ui_framework_image_drawImage('coal', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_IRON:            ('iron'           , lambda rect, h, h4: ui_framework_image_drawImage('iron', rect) if h < 35 else ui_framework_image_drawImage('iron2', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_COPPER:          ('copper'         , lambda rect, h, h4: ui_framework_image_drawImage('copper', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_PRECIOUS_METALS: ('precious metals', lambda rect, h, h4: ui_framework_image_drawImage('precious', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_RARE_METALS:     ('rare metals'    , lambda rect, h, h4: ui_framework_image_drawImage('rare', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_SAND:            ('sand'           , lambda rect, h, h4: ui_framework_image_drawImage('sand', rect)),
	Ressource.model_terrain_ressource_RESSOURCE_STONE:           ('stone'          , lambda rect, h, h4: ui_framework_image_drawImage('stone', rect)),							
}

def ui_map_ressource_print_ressource(ressource):
	return ui_map_ressource_ressourceDrawMap[Ressource.model_terrain_ressource_type(ressource)][0]

def ui_map_ressource_draw_ressource(tile):
	func = ui_map_ressource_ressourceDrawMap.get(
		Ressource.model_terrain_ressource_type(tile),
		('', lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 0, 0)))
	)[1]
	h = Ressource.model_terrain_ressource_height(tile)
	return lambda rect, h=h, h4=h % 4 * 16: func(rect, h, h4)