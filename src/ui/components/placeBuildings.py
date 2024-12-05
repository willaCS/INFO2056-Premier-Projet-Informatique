import Window
from model.industry import Plant, plants
from model.industry.technologiesTree import get_placable_on
from ui import SelectedTile
from ui import visual_config as vc
from ui.map.industry import draw_industry_by_id
from ui.common.buttons import centerTextButton, exit_button
from ui.framework import component, component_hide, component_show, drawRect, drawImage


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
CLOSE_BUTTON_SIZE = (75, 75)
RESOURCE_BUTTON_WIDTH = 250
NOMBRE_DE_COLONNES = 4



def closeplaceBuildingsMenu(pos):
	global placeBuildingsMenu
	SelectedTile.val = None
	component_hide(placeBuildingsMenu)
	# composant_temp_remove(placeBuildingsMenu)

placeBuildingsMenu = component(
	z=1,
	margin=MENU_MARGIN,
	padding=vc.PADDING + vc.MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, vc.TOP_BAR_HEIGHT),
		(vc.LARGEUR_SIDEMENU, parent[1][1] - vc.TOP_BAR_HEIGHT),
	),
	draw=lambda rect: drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH) or\
					  drawRect(rect, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.MENU_BORDER_WIDTH),
	clickOutside=closeplaceBuildingsMenu,
	childs=[
		# Header
		component(
			z=2,
			rect=lambda parent: (
				(0, 0),
				(
					parent[1][0] - (CLOSE_BUTTON_SIZE[0] + vc.PADDING),
					CLOSE_BUTTON_SIZE[1]
				)
			),
			draw=lambda rect: centerTextButton(rect, "font2", "Place Building", vc.BACKGROUND3, vc.ROUNDING_SMOOTH),
		),

		# Close button
		component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - CLOSE_BUTTON_SIZE[0], 0),
				CLOSE_BUTTON_SIZE
			),
			draw=exit_button,
			click=closeplaceBuildingsMenu,
		),
	]
)



def showplaceBuildingsMenu():
	# if placeBuildingsMenu['_hidden']:
		can_be_build = get_placable_on(SelectedTile.val)

		tile_width = ((vc.LARGEUR_SIDEMENU - 2 * (MENU_MARGIN + vc.PADDING + vc.MENU_BORDER_WIDTH)) - (NOMBRE_DE_COLONNES - 1) * vc.PADDING) // NOMBRE_DE_COLONNES
		# composant_add_temp(placeBuildingsMenu, [
		# 	button_new(
		# 		2,
		# 		lambda index=index: (
		# 			(
		# 				0 + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING + (index % NOMBRE_DE_COLONNES) * (tile_width + vc.PADDING),
		# 				vc.TOP_BAR_HEIGHT + MENU_MARGIN + vc.MENU_BORDER_WIDTH + 2 * vc.PADDING  + CLOSE_BUTTON_SIZE[1] + (index // NOMBRE_DE_COLONNES)*(tile_width + vc.PADDING)
		# 			),
		# 			(
		# 				tile_width,
		# 				tile_width,
		# 			)
		# 		),
		# 		draw_industry_by_id(building_id),
		# 		lambda pos, building_id=building_id: plants.place(Plant.init(building_id, SelectedTile.val))
		# 	)
		# 	for index, building_id in enumerate(can_be_build)
		# ])
		# component_show(placeBuildingsMenu)
 



 