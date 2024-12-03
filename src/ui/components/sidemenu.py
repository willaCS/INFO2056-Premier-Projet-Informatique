import Window
from globals import all
from ui import SelectedTile
from ui import visual_config as vc
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



def closeSideMenu(pos):
	global sideMenu
	SelectedTile.val = None
	composant_hide(sideMenu)



def prio(rect):
	if TerrainTile.ressource(get_terrain_tile(SelectedTile.val)) == None:
		return
	else:
		__drawRessource(rect)




def __drawSideMenu(rect):
	global tiletype
	drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH)
	drawRect(rect, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.MENU_BORDER_WIDTH)

def __drawExitButon(rect):
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD)
	drawImage('exit', rect)

def __drawRessource(rect):
	if not SelectedTile.val:
		centerTextButton(rect, "font1", "", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
		return
	terrain = get_terrain_tile(SelectedTile.val)
	ressource = TerrainTile.ressource(terrain)
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
	position, taille = rect
	if ressource == None:
		return
		#centerTextButton(((position[0] + taille[0] / 3,position[1]), (taille[0] * 2/3, taille[1])), "font3", "no ressource present", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
	else:
		drawText("font3", (position[0] + taille[0] / 3,position[1] + taille[0] * 1/15), print_ressource(ressource), vc.TEXT)
		drawImage('stone', ((position[0] + taille[0] * 1/15, position[1] + taille[0] * 1/15), (taille[0] * 1/6, taille[0] * 1/6)))
		#centerTextButton(((position[0] + taille[0] / 3,position[1]), (taille[0] * 2/3, taille[1])), "font3", print_ressource(ressource), vc.BACKGROUND3, vc.ROUNDING_SMOOTH)



sideMenu = composant_new(2, [
	# Background
	button_new(1,
		lambda: (
			(0 + MENU_MARGIN, TOP_BAR_HEIGHT + MENU_MARGIN),
			(LARGEUR_SIDEMENU - 2 * MENU_MARGIN, Window.resolution[1] - TOP_BAR_HEIGHT - 2 * MENU_MARGIN),
		),
		__drawSideMenu,
		lambda pos: None,
		closeSideMenu,
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
		lambda rect: centerTextButton(rect, "font2", print_terrain_tile(get_terrain_tile(SelectedTile.val)) if SelectedTile.val else "", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
	),


	# second button
	button_new(
		2,
		lambda: 
		(
			(
				0 + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING,
				TOP_BAR_HEIGHT + MENU_MARGIN + vc.MENU_BORDER_WIDTH + 2 * vc.PADDING + CLOSE_BUTTON_SIZE[1] 
			),
			(
				LARGEUR_SIDEMENU - 2 * (vc.MENU_BORDER_WIDTH + vc.PADDING) - 2 * MENU_MARGIN,
				RESOURCE_BUTTON_WIDTH
			)
		),
		prio
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
		closeSideMenu

	),
])



def showSideMenu():
	composant_show(sideMenu)