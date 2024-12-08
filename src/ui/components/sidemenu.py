import Window
from ui import SelectedTile
from ui import visual_config as vc
from ui.framework.framework import component_add_temp, component_temp_remove
from ui.map.terrainTile import print_terrain_tile
from ui.map.ressource import print_ressource
from ui.map.goods import draw_goods, ressources_to_goods, print_goods
from ui.common.buttons import centerTextButton, exit_button
from ui.framework import component, component_hide, component_show, drawRect, drawImage, drawText
from model.terrain import Ressource, TerrainTile
from model.terrain.terrain import get_terrain_tile


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
HEADER_HEIGHT = 75
CLOSE_BUTTON_SIZE = (75, 75)
RESOURCE_CARTE_HEIGHT = (Window.resolution[1] - 2 * (MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING) - vc.TOP_BAR_HEIGHT - 2 * vc.PADDING - CLOSE_BUTTON_SIZE[1]) / 2
RESOURCE_BUTTON_HEIGHT = (RESOURCE_CARTE_HEIGHT - 6 * vc.PADDING) / 5


def closeSideMenu(pos):
	global sideMenu
	SelectedTile.val = None
	component_hide(sideMenu) 
	component_temp_remove(sideMenu)


def prio(rect):
	if SelectedTile.val and TerrainTile.ressource(get_terrain_tile(SelectedTile.val)) == None:
		return
	else:
		__draw_carte(rect)




def __drawExitButon(rect):
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD)
	drawImage('exit', rect)

def __drawRessourceButton(rect, good):
	drawRect(rect, vc.BACKGROUND2, vc.ROUNDING_SMOOTH)
	print(good)
	position, taille = rect
	draw_func = draw_goods(good)
	draw_func(((position[0] + (taille[1] - 50) / 2, position[1] + (taille[1] - 50) / 2), (50, 50)))
	centerTextButton((
			(position[0] + 50 + 2 * vc.PADDING, position[1] + vc.PADDING),
			(taille[0] - 2 * vc.PADDING - 50 - vc.PADDING, taille[1] - 2 * vc.PADDING)
		), 'font3', '{}'.format(print_goods(good)), vc.BACKGROUND3, vc.ROUNDING_SMOOTH, vc.PADDING)

def __draw_carte(rect):
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
	# position, taille = rect
	# drawText("font3", (position[0] + taille[0] / 2,position[1] + taille[0] * 1/15), print_ressource(ressource), vc.TEXT, "center" )
	#print(Ressource.type(ressource))
	# goods = ressources_to_goods(Ressource.type(ressource))
	#print(goods)

	# if len(goods) > 1:
		# for good in goods:
			# draw_func = draw_goods(good)
			# draw_func(((position[0] + taille[0] * 1/15, position[1] + 50 + space), (spacer, spacer)))
			# space += spacer
		# space = 0
		# spacer = (RESOURCE_BUTTON_HEIGHT - 50) / len(goods)
		# for good in goods:
			# draw_func = draw_goods(good)
			# draw_func(((position[0] + taille[0] * 1/15, position[1] + 50 + space), (spacer, spacer)))
			# space += spacer
	# else:
		# good = goods[0]
		# draw_func = draw_goods(good)
		# print((position[0] + taille[0] * 1/15, position[1] + 50 + taille[0] * 1/15), (taille[0] * 1/6, taille[0] * 1/6))
		# draw_func(((position[0] + taille[0] * 1/15, position[1] + 50 + taille[0] * 1/15), (taille[0] * 1/6, taille[0] * 1/6)))
	
def __drawRessource(rect):
	# terrain = get_terrain_tile(SelectedTile.val)
	# ressource = TerrainTile.ressource(terrain)
	# drawRect(rect, vc.BACKGROUND2, vc.ROUNDING_SMOOTH)
	# position, taille = rect
	# drawText("font3", (position[0] + taille[0] / 2,position[1] + taille[0] * 1/15), "Ressource", vc.TEXT, "center" )
	centerTextButton(rect, "font3", "Ressource", vc.BACKGROUND2, vc.ROUNDING_SMOOTH,)



sideMenu = component(
	z=2,
	margin=MENU_MARGIN,
	padding=vc.PADDING + vc.MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, vc.TOP_BAR_HEIGHT),
		(vc.LARGEUR_SIDEMENU, parent[1][1] - vc.TOP_BAR_HEIGHT),
	),
	draw=lambda rect: drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH) or\
					  drawRect(rect, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.MENU_BORDER_WIDTH),
	click=lambda pos: None,
	clickOutside=closeSideMenu,
	childs=[
		# Header
		component(
			z=2,
			rect=lambda parent: 
			(
				(0, 0),
				(
					parent[1][0] - vc.PADDING - HEADER_HEIGHT,
					HEADER_HEIGHT
				)
			),
			draw=lambda rect: centerTextButton(rect, "font2", print_terrain_tile(get_terrain_tile(SelectedTile.val)) if SelectedTile.val else "", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
		),

		# Close button
		component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - CLOSE_BUTTON_SIZE[0], 0),
				(HEADER_HEIGHT, HEADER_HEIGHT)
			),
			draw=exit_button,
			click=closeSideMenu
		),

		# first button
		component(
			z=2,
			rect=lambda parent: (
				(
					0,
					HEADER_HEIGHT + vc.PADDING,
				),
				(
					parent[1][0],
					RESOURCE_CARTE_HEIGHT
				)
			),
			draw=lambda rect: None,
			childs=[
				*[component(
					z=2,
					margin=vc.PADDING // 2,
					rect=lambda parent: (
						(
							0,
							0,
						),
						(
							parent[1][0],
							parent[1][1],
						)
					),
					draw=__draw_carte,
					)
				],
			]
		),


		# second button
		# component(
			# z=2,
			# rect=lambda parent: (
				# (
					# 0,
					# HEADER_HEIGHT + vc.PADDING + RESOURCE_BUTTON_HEIGHT + vc.PADDING,
				# ),
				# (
					# parent[1][0],
					# RESOURCE_BUTTON_HEIGHT
				# )
			# ),
			# draw=prio
		# ),
	]
)



def showSideMenu():
	if sideMenu['_hidden']:
		terrain = get_terrain_tile(SelectedTile.val)
		ressource = TerrainTile.ressource(terrain)
		if not ressource:
			return
		goods = ressources_to_goods(Ressource.type(ressource))
		print(goods)
		component_add_temp(sideMenu, [
			component(
				z=3,
				#margin=MENU_MARGIN,
				rect=lambda parent: (
					(
						vc.PADDING,
						(HEADER_HEIGHT + vc.PADDING) + vc.PADDING,
					),
					(
						parent[1][0] - 2 * vc.PADDING,
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=__drawRessource,
			),

			*(component(
				z=3,
				#margin=MENU_MARGIN,
				rect=lambda parent, y=index: (
					(
						vc.PADDING,
						(HEADER_HEIGHT + vc.PADDING) + (RESOURCE_BUTTON_HEIGHT + vc.PADDING) + vc.PADDING + y * (RESOURCE_BUTTON_HEIGHT + vc.PADDING),
					),
					(
						parent[1][0] - 2 * vc.PADDING,
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect, is_in, good=good: __drawRessourceButton(rect, good)
			)
			for index,good in enumerate(goods)
			),
							
		])
		component_show(sideMenu)