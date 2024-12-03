import Window
from globals import all
from model.industry.technologiesTree import get_placable_on
from ui import SelectedTile
from ui import visual_config as vc
from ui.framework.framework import composant_add_temp, composant_temp_remove
from ui.map.terrainTile import print_terrain_tile
from ui.map.ressource import print_ressource
from ui.common.buttons import centerTextButton
from ui.components.topbar import TOP_BAR_HEIGHT
from ui.framework import button_new, composant_hide, composant_new, composant_show, drawRect, drawImage, drawText
from model.terrain import TerrainTile
from model.terrain.terrain import get_terrain_tile


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
CLOSE_BUTTON_SIZE = (75, 75)
RESOURCE_BUTTON_WIDTH = 250
LARGEUR_SIDEMENU = 470
NOMBRE_DE_COLONNES = 3



def closeplaceBuildingsMenu(pos):
	global placeBuildingsMenu
	SelectedTile.val = None
	composant_hide(placeBuildingsMenu)
	composant_temp_remove(placeBuildingsMenu)



 




def __drawSideMenu(rect):
	drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH)
	drawRect(rect, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.MENU_BORDER_WIDTH)
	


def __drawExitButon(rect):
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD)
	drawImage('exit', rect)



placeBuildingsMenu = composant_new(3, [
	# Background
	button_new(1,
		lambda: (
			(0 + MENU_MARGIN, TOP_BAR_HEIGHT + MENU_MARGIN),
			(LARGEUR_SIDEMENU - 2 * MENU_MARGIN, Window.resolution[1] - TOP_BAR_HEIGHT - 2 * MENU_MARGIN),
		),
		__drawSideMenu,
		lambda pos: None,
		closeplaceBuildingsMenu,
	),
	

	# Header
	button_new(
		2,
		lambda: 
		(
			(
				0 + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING,
				TOP_BAR_HEIGHT + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING
			),
			(
				LARGEUR_SIDEMENU - 2 * (vc.MENU_BORDER_WIDTH + vc.PADDING) - vc.PADDING - 2 * MENU_MARGIN - CLOSE_BUTTON_SIZE[0],
				CLOSE_BUTTON_SIZE[1]
			)
		),
		lambda rect: centerTextButton(rect, "font2", "Place Building", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
	),




	# Close button
	button_new(
		2,
		lambda: (
			(
				LARGEUR_SIDEMENU - MENU_MARGIN - vc.PADDING - vc.MENU_BORDER_WIDTH - CLOSE_BUTTON_SIZE[0],
				TOP_BAR_HEIGHT + MENU_MARGIN + vc.PADDING + vc.MENU_BORDER_WIDTH
			),
			CLOSE_BUTTON_SIZE
		),
		__drawExitButon,
		closeplaceBuildingsMenu

	),
])



def showplaceBuildingsMenu():
	print(len(placeBuildingsMenu['buttons']))
	if placeBuildingsMenu['hidden']:
		can_be_build = get_placable_on(SelectedTile.val)
		composant_add_temp(placeBuildingsMenu, [
			button_new(
				2,
				lambda i=i: (
					(
						0 + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING + i * ((LARGEUR_SIDEMENU - 2 * (MENU_MARGIN + vc.PADDING + vc.MENU_BORDER_WIDTH)) - (NOMBRE_DE_COLONNES - 1) * vc.PADDING) // NOMBRE_DE_COLONNES,
						TOP_BAR_HEIGHT + MENU_MARGIN + vc.MENU_BORDER_WIDTH + 2 * vc.PADDING  + CLOSE_BUTTON_SIZE[1]
					),
					(
						((LARGEUR_SIDEMENU - 2 * (MENU_MARGIN + vc.PADDING + vc.MENU_BORDER_WIDTH)) - (NOMBRE_DE_COLONNES - 1) * vc.PADDING) // NOMBRE_DE_COLONNES,
						((LARGEUR_SIDEMENU - 2 * (MENU_MARGIN + vc.PADDING + vc.MENU_BORDER_WIDTH)) - (NOMBRE_DE_COLONNES - 1) * vc.PADDING) // NOMBRE_DE_COLONNES
					)
				),
				lambda rect: drawRect(rect, (0, 0, 255)),
			)
			for i in range(len(can_be_build))
		])
		composant_show(placeBuildingsMenu)
 

 