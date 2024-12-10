from model.industry import plants
from model.industry.technologiesTree import model_technologyTree_get_placable_on
from ui import SelectedTile
from ui import visual_config as vc

from ui.framework.framework import ui_framework_framework_component_add_temp, ui_framework_framework_component_temp_remove
from ui.map.industry import ui_map_industry_draw_industry_menu
from ui.common.buttons import ui_common_centerTextButton, ui_common_exit_button
from ui.framework.framework import ui_framework_framework_component, ui_framework_framework_component_hide, ui_framework_framework_component_show
from ui.framework.draw import ui_framework_draw_drawRect

ui_component_placeBuilding_EXIT_BUTTON_BORDER = 2 #en pixels
ui_component_placeBuilding_CLOSE_BUTTON_SIZE = (75, 75)
ui_component_placeBuilding_RESOURCE_BUTTON_WIDTH = 250
ui_component_placeBuilding_NOMBRE_DE_COLONNES = 5

def ui_component_placeBuilding_closeplaceBuildingsMenu():
	global ui_component_placeBuilding_placeBuildingsMenu
	# SelectedTile.val = None
	ui_framework_framework_component_hide(ui_component_placeBuilding_placeBuildingsMenu)
	ui_framework_framework_component_temp_remove(ui_component_placeBuilding_placeBuildingsMenu)
	from ui.components.sidemenu import refreshSideMenu
	refreshSideMenu()

ui_component_placeBuilding_placeBuildingsMenu = ui_framework_framework_component(
	z=4,
	margin=vc.VC_MENU_BORDER_WIDTH,
	padding=vc.VC_PADDING + vc.VC_MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, vc.VC_TOP_BAR_HEIGHT),
		(vc.VC_LARGEUR_SIDEMENU, parent[1][1] - vc.VC_TOP_BAR_HEIGHT),
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH) or\
					  ui_framework_draw_drawRect(rect, vc.VC_PRIMARY, vc.VC_ROUNDING_SMOOTH, vc.VC_MENU_BORDER_WIDTH),
	clickOutside=ui_component_placeBuilding_closeplaceBuildingsMenu,
	childs=[
		# Header
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(0, 0),
				(
					parent[1][0] - (ui_component_placeBuilding_CLOSE_BUTTON_SIZE[0] + vc.VC_PADDING),
					ui_component_placeBuilding_CLOSE_BUTTON_SIZE[1]
				)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, "font2", "Place Building", vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH),
		),

		# Close button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - ui_component_placeBuilding_CLOSE_BUTTON_SIZE[0], 0),
				ui_component_placeBuilding_CLOSE_BUTTON_SIZE
			),
			draw=ui_common_exit_button,
			click=ui_component_placeBuilding_closeplaceBuildingsMenu,
		),
	]
)



def ui_component_placeBuilding_showplaceBuildingsMenu():
	if ui_component_placeBuilding_placeBuildingsMenu['_hidden']:
		can_be_build = model_technologyTree_get_placable_on(SelectedTile.SelectedTile_val)
		print('xd')

		tile_width = ((vc.VC_LARGEUR_SIDEMENU - 2 * (vc.VC_MENU_BORDER_WIDTH + vc.VC_PADDING + vc.VC_MENU_BORDER_WIDTH)) - (ui_component_placeBuilding_NOMBRE_DE_COLONNES - 1) * vc.VC_PADDING) // ui_component_placeBuilding_NOMBRE_DE_COLONNES
		ui_framework_framework_component_add_temp(ui_component_placeBuilding_placeBuildingsMenu, [
			ui_framework_framework_component(
				z=2,
				rect=lambda parent, x=index % ui_component_placeBuilding_NOMBRE_DE_COLONNES, y=index // ui_component_placeBuilding_NOMBRE_DE_COLONNES: (
					(
						x * (tile_width + vc.VC_PADDING),
						y * (tile_width + vc.VC_PADDING) + ui_component_placeBuilding_CLOSE_BUTTON_SIZE[1] + vc.VC_PADDING,
					),
					(
						tile_width,
						tile_width,
					)
				),
				draw=ui_map_industry_draw_industry_menu(building_id),
				click=lambda pos, building_id=building_id: plants.model_plants_place(building_id, SelectedTile.SelectedTile_val)\
					or ui_component_placeBuilding_closeplaceBuildingsMenu()
			)
			for index, building_id in enumerate(can_be_build)
		])
		ui_framework_framework_component_show(ui_component_placeBuilding_placeBuildingsMenu)
 



 