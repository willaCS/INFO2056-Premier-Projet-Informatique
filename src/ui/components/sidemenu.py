import Window
from globals import all
from ui import SelectedTile
from ui import visual_config as vc
from ui.components.topbar import TOP_BAR_HEIGHT
from model.terrain.terrain import get_terrain_tile
from ui.framework import button_new, composant_hide, composant_new, composant_show, drawRect, drawImage, drawText
from model.terrain import TerrainTile
from ui.common.buttons import centerTextButton


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
CLOSE_BUTTON_SIZE = (75, 75)
LARGEUR_SIDEMENU = 470



def closeSideMenu(pos):
	global sideMenu
	SelectedTile.val = None
	composant_hide(sideMenu)







def __drawSideMenu(rect):
	drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH)
	drawRect(rect, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.MENU_BORDER_WIDTH)
	terrain = get_terrain_tile(SelectedTile.val)
	#print(TerrainTile.type(terrain))
	Tiletype = ""
	match TerrainTile.type(terrain):
		case 7:
			Tiletype = "MOUNTAIN_TOP Tile"
		case 6:
			Tiletype = "MOUNTAIN_SIDE Tile"
		case 5:
			Tiletype = "FOREST Tile"
		case 4:
			Tiletype = "PLAIN Tile"
		case 3:
			Tiletype = "BEACH Tile"
		case 2:
			Tiletype = "SEA Tile"
		case 1:
			Tiletype = "DEEPSEA Tile"

def __drawExitButon(rect):
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD)
	drawImage('exit', rect)




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
		lambda rect: centerTextButton(rect, "font2", "test", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
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