from model.industry import plants
from model.industry.technologiesTree import get_placable_on
from ui import SelectedTile
from ui import visual_config as vc

from utils.Components import Component
from ui.map.industry import draw_industry_menu
from ui.common.buttons import backgroundSubmenu, centerTextButton, exit_button


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
CLOSE_BUTTON_SIZE = (75, 75)
RESOURCE_BUTTON_WIDTH = 250
NOMBRE_DE_COLONNES = 5


def closeplaceBuildingsMenu():
	global placeBuildingsMenu
	# SelectedTile.val = None
	placeBuildingsMenu.hide()
	placeBuildingsMenu.temp_remove()
	from ui.components.sidemenu import refreshSideMenu
	refreshSideMenu()

placeBuildingsMenu = Component(
	margin=MENU_MARGIN,
	padding=vc.PADDING + vc.MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, vc.TOP_BAR_HEIGHT),
		(vc.LARGEUR_SIDEMENU, parent[1][1] - vc.TOP_BAR_HEIGHT),
	),
	draw=backgroundSubmenu(vc.BACKGROUND, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.MENU_BORDER_WIDTH),
	clickOutside=closeplaceBuildingsMenu,
	childs=[
		# Header
		Component(
			rect=lambda parent: (
				(0, 0),
				(
					parent[1][0] - (CLOSE_BUTTON_SIZE[0] + vc.PADDING),
					CLOSE_BUTTON_SIZE[1]
				)
			),
			draw=centerTextButton("font2", "Place Building", vc.BACKGROUND3, vc.ROUNDING_SMOOTH),
		),

		# Close button
		Component(
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
	if placeBuildingsMenu._hidden:
		can_be_build = get_placable_on(SelectedTile.val)

		tile_width = ((vc.LARGEUR_SIDEMENU - 2 * (MENU_MARGIN + vc.PADDING + vc.MENU_BORDER_WIDTH)) - (NOMBRE_DE_COLONNES - 1) * vc.PADDING) // NOMBRE_DE_COLONNES
		placeBuildingsMenu.add_temp([
			Component(
				z=2,
				rect=lambda x=index % NOMBRE_DE_COLONNES, y=index // NOMBRE_DE_COLONNES: (
					(
						x * (tile_width + vc.PADDING),
						y * (tile_width + vc.PADDING) + CLOSE_BUTTON_SIZE[1] + vc.PADDING,
					),
					(
						tile_width,
						tile_width,
					)
				),
				draw=draw_industry_menu(building_id),
				click=lambda building_id=building_id: \
					plants.place(building_id, SelectedTile.val)\
					or closeplaceBuildingsMenu()
			)
			for index, building_id in enumerate(can_be_build)
		])
		placeBuildingsMenu.show()
 



 