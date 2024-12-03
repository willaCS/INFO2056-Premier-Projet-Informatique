import Window
from ui import SelectedTile
from ui import visual_config as vc
from ui.framework.framework import composant_add_temp, composant_temp_remove
from ui.map.terrainTile import print_terrain_tile
from ui.map.ressource import print_ressource
from ui.map.goods import draw_goods, ressources_to_goods
from ui.common.buttons import centerTextButton
from ui.components.topbar import TOP_BAR_HEIGHT
from ui.framework import button_new, composant_hide, composant_new, composant_show, drawRect, drawImage, drawText
from model.terrain import Ressource, TerrainTile
from model.terrain.terrain import get_terrain_tile


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
CLOSE_BUTTON_SIZE = (75, 75)
RESOURCE_BUTTON_HEIGHT = (Window.resolution[1]- 2 * (MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING)  - TOP_BAR_HEIGHT - 2 * vc.PADDING- CLOSE_BUTTON_SIZE[1]) / 2
LARGEUR_SIDEMENU = 470



def closeSideMenu(pos):
	global sideMenu
	SelectedTile.val = None
	composant_hide(sideMenu) 
	composant_temp_remove(sideMenu)


def prio(rect):
	if SelectedTile.val and TerrainTile.ressource(get_terrain_tile(SelectedTile.val)) == None:
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

def __drawRessourceButton(rect):
	drawRect(rect, vc.BACKGROUND2, vc.ROUNDING_SMOOTH)

def __drawRessource(rect):
	terrain = get_terrain_tile(SelectedTile.val)
	ressource = TerrainTile.ressource(terrain)
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
	position, taille = rect
	drawText("font3", (position[0] + taille[0] / 2,position[1] + taille[0] * 1/15), print_ressource(ressource), vc.TEXT, "center" )
	#print(Ressource.type(ressource))
	goods = ressources_to_goods(Ressource.type(ressource))
	#print(goods)

	if len(goods) > 1:
		space = 0
		spacer = (RESOURCE_BUTTON_HEIGHT - 50) / len(goods)
		for good in goods:
			draw_func = draw_goods(good)
			draw_func(((position[0] + taille[0] * 1/15, position[1] + 50 + space), (spacer, spacer)))
			space += spacer
	else:
		good = goods[0]
		draw_func = draw_goods(good)
		# print((position[0] + taille[0] * 1/15, position[1] + 50 + taille[0] * 1/15), (taille[0] * 1/6, taille[0] * 1/6))
		draw_func(((position[0] + taille[0] * 1/15, position[1] + 50 + taille[0] * 1/15), (taille[0] * 1/6, taille[0] * 1/6)))
	


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


	# first button
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
				RESOURCE_BUTTON_HEIGHT
			)
		),
		prio
	),


    # second button
	# button_new(
	# 	2,
	# 	lambda: 
	# 	(
	# 		(
	# 			0 + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING,
	# 			TOP_BAR_HEIGHT + MENU_MARGIN + vc.MENU_BORDER_WIDTH + 3 * vc.PADDING + CLOSE_BUTTON_SIZE[1] + RESOURCE_BUTTON_HEIGHT
	# 		),
	# 		(
	# 			LARGEUR_SIDEMENU - 2 * (vc.MENU_BORDER_WIDTH + vc.PADDING) - 2 * MENU_MARGIN,
	# 			RESOURCE_BUTTON_HEIGHT
	# 		)
	# 	),
	# 	prio
	# ),


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
	if sideMenu['hidden']:
		composant_add_temp(sideMenu, [
			button_new(
				3,
				lambda: 
				(
					(
						0 + MENU_MARGIN + vc.MENU_BORDER_WIDTH + 2 * vc.PADDING,
						230
					),
					(
						LARGEUR_SIDEMENU - 2 * (vc.MENU_BORDER_WIDTH + vc.PADDING) - 2 * MENU_MARGIN - 2 * vc.PADDING,
						73.33333333333333
					)
				),
				__drawRessourceButton
			),
		])
		composant_show(sideMenu)