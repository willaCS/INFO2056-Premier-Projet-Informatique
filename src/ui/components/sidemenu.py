from ui.utils import longNumber
import utils.Window as Window
from ui import SelectedTile
from ui import visual_config as vc
from ui.components.placeBuildings import showplaceBuildingsMenu
from utils.Components import Component
from ui.map.terrainTile import print_terrain_tile
from ui.map.goods import draw_goods, ressources_to_goods, print_goods
from ui.map.industry import draw_industry_menu2, print_industry, draw_industry_product
from ui.common.buttons import backgroundSubmenu, centerLeftTextButton, centerRightTextButton, centerTextButton, exit_button
from model.terrain import Ressource, TerrainTile
from model.terrain.terrain import get_terrain_tile
from model.industry import plants
from model.industry import Plant


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
HEADER_HEIGHT = 75
CLOSE_BUTTON_SIZE = (75, 75)
RESOURCE_CARTE_HEIGHT = (Window.resolution[1] - 2 * (MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING) - vc.TOP_BAR_HEIGHT - 2 * vc.PADDING - CLOSE_BUTTON_SIZE[1]) / 2
RESOURCE_BUTTON_HEIGHT = (RESOURCE_CARTE_HEIGHT - 6 * vc.PADDING) / 5


def closeSideMenu():
	global sideMenu
	SelectedTile.val = None
	sideMenu.hide() 
	sideMenu.temp_remove()

def refreshSideMenu():
	global sideMenu
	sideMenu.temp_remove()
	createTemp()


def __drawRessourceButton(rect, window, good):
	window.draw_rect(rect, vc.BACKGROUND2, vc.ROUNDING_SMOOTH)
	position, taille = rect
	draw_func = draw_goods(good)
	draw_func(((position[0] + (taille[1] - 50) / 2, position[1] + (taille[1] - 50) / 2), (50, 50)))
	centerTextButton(
		(
			(position[0] + 50 + 2 * vc.PADDING, position[1] + vc.PADDING),
			(taille[0] - 2 * vc.PADDING - 50 - vc.PADDING, taille[1] - 2 * vc.PADDING)
		),
		'font3', '{}'.format(print_goods(good)),
		vc.BACKGROUND3, vc.ROUNDING_SMOOTH
	)

def __drawBuildingButton(rect, window, building_id):
	window.draw_rect(rect, vc.BACKGROUND2, vc.ROUNDING_SMOOTH)
	position, taille = rect
	draw_func = draw_industry_menu2(building_id)
	draw_func(((position[0] + (taille[1] - 50) / 2, position[1] + (taille[1] - 50) / 2), (50, 50)), False)
	centerTextButton(
		(
			(position[0] + 50 + 2 * vc.PADDING, position[1] + vc.PADDING),
			(taille[0] - 2 * vc.PADDING - 50 - vc.PADDING, taille[1] - 2 * vc.PADDING)
		),
		'font3', '{}'.format(print_industry(building_id)),
		vc.BACKGROUND2, vc.ROUNDING_SMOOTH
	)


sideMenu = Component(
	z=2,
	margin=MENU_MARGIN,
	padding=vc.PADDING + vc.MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, vc.TOP_BAR_HEIGHT),
		(vc.LARGEUR_SIDEMENU, parent[1][1] - vc.TOP_BAR_HEIGHT),
	),
	draw=backgroundSubmenu(vc.BACKGROUND, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.ROUNDING_SMOOTH),
	click=lambda: None,
	clickOutside=closeSideMenu,
	childs=[
		# Header
		Component(
			z=2,
			rect=lambda parent: 
			(
				(0, 0),
				(
					parent[1][0] - vc.PADDING - HEADER_HEIGHT,
					HEADER_HEIGHT
				)
			),
			draw=lambda rect, window: centerTextButton('font2', print_terrain_tile(get_terrain_tile(SelectedTile.val)) if SelectedTile.val else "", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)(rect, window)
		),

		# Close button
		Component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - CLOSE_BUTTON_SIZE[0], 0),
				(HEADER_HEIGHT, HEADER_HEIGHT)
			),
			draw=exit_button,
			click=closeSideMenu
		),
	]
)

def carteRessource(pos):
	terrain = get_terrain_tile(SelectedTile.val)
	ressource = TerrainTile.ressource(terrain)
	if not ressource:
		return
	goods = ressources_to_goods(Ressource.type(ressource))
	return Component(
		z=2,
		padding=vc.PADDING,
		rect=lambda parent: (
			(
				0,
				HEADER_HEIGHT + vc.PADDING + pos * (RESOURCE_CARTE_HEIGHT + vc.PADDING),
			),
			(
				parent[1][0],
				RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect, window: window.draw_rect(rect, vc.BACKGROUND3, vc.ROUNDING_SMOOTH),
		childs=[
			Component(
				z=3,
				rect=lambda parent: (
					(0, 0),
					(
						parent[1][0],
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: centerTextButton(rect, "font3", "Ressources", vc.BACKGROUND2, vc.ROUNDING_SMOOTH,),
			),

			*(Component(
				z=3,
				rect=lambda parent, y=index: (
					(
						0,
						(y + 1) * (RESOURCE_BUTTON_HEIGHT + vc.PADDING),
					),
					(
						parent[1][0],
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect, is_in, good=good: __drawRessourceButton(rect, good)
			)
			for index,good in enumerate(goods)
			),
		]
	)


def carteIndustry(pos):
	building = plants.get(SelectedTile.val)
	building_id = Plant.type(building)
	if not plants.get(SelectedTile.val):
		return

	return Component(
		z=2,
		padding=vc.PADDING,
		rect=lambda parent: (
			(
				0,
				HEADER_HEIGHT + vc.PADDING + pos * (RESOURCE_CARTE_HEIGHT + vc.PADDING),
			),
			(
				parent[1][0],
				RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect, window: window.draw_rect(rect, vc.BACKGROUND3, vc.ROUNDING_SMOOTH),
		childs=[
			Component(
				z=3,
				rect=lambda parent: (
					(0, 0),
					(
						parent[1][0],
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=centerTextButton("font3", "Building", vc.BACKGROUND2, vc.ROUNDING_SMOOTH),
			),

			Component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(RESOURCE_BUTTON_HEIGHT + vc.PADDING) * 1,
					),
					(
						parent[1][0],
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect, is_in, building_id=building_id: __drawBuildingButton(rect, building_id)
			),

			Component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(RESOURCE_BUTTON_HEIGHT + vc.PADDING) * 2,
					),
					(
						parent[1][0],
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=draw_industry_product(building_id),
				childs=[],
			),

			Component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(RESOURCE_BUTTON_HEIGHT + vc.PADDING) * 3,
					),
					(
						parent[1][0],
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: None,
				childs=[
					Component(
						z=3,
						rect=lambda parent: (
							(
								0,
								0,
							),
							(
								parent[1][0] // 2,
								parent[1][1],
							)
						),
						draw=centerLeftTextButton(
							'font3', '{}'.format("Generated"),
							vc.BACKGROUND2, vc.ROUNDING_SMOOTH, vc.PADDING
						)
					),
					
					Component(
						z=3,
						rect=lambda parent: (
							(
								parent[1][0] // 2 + vc.PADDING,
								0,
							),
							(
								parent[1][0] // 2 - vc.PADDING,
								parent[1][1],
							)
						),
						draw=centerRightTextButton(
							'font3', longNumber(building['generated']),
							vc.BACKGROUND2, vc.ROUNDING_SMOOTH, vc.PADDING
						)
					),
				],
			),

			Component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(RESOURCE_BUTTON_HEIGHT + vc.PADDING) * 4,
					),
					(
						parent[1][0],
						RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: None,
				childs=[
					Component(
						z=3,
						rect=lambda parent: (
							(
								0,
								0,
							),
							(
								parent[1][0] // 2,
								parent[1][1],
							)
						),
						draw=centerLeftTextButton(
							'font3', '{}'.format("Level"),
							vc.BACKGROUND2, vc.ROUNDING_SMOOTH, vc.PADDING
						)
					),
					
					Component(
						z=3,
						rect=lambda parent: (
							(
								parent[1][0] // 2 + vc.PADDING,
								0,
							),
							(
								parent[1][0] // 2 - vc.PADDING,
								parent[1][1],
							)
						),
						draw=centerRightTextButton(
							'font3', longNumber(0),
							vc.BACKGROUND2, vc.ROUNDING_SMOOTH, vc.PADDING
						)
					),
				],
			),

		]
	)

def cartePlus(pos):
	return Component(
		z=2,
		padding=vc.PADDING,
		rect=lambda parent: (
			(
				0,
				HEADER_HEIGHT + vc.PADDING + pos * (RESOURCE_CARTE_HEIGHT + vc.PADDING),
			),
			(
				parent[1][0],
				RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect, window: window.draw_rect(rect, vc.BACKGROUND3, vc.ROUNDING_SMOOTH, hover=vc.ACCENT),
		click=showplaceBuildingsMenu,
		childs=[
			Component(
				z=3,
				rect=lambda parent: (
					((parent[1][0] - parent[1][1]) // 2, 0),
					(
						parent[1][1],
						parent[1][1],
					)
				),
				draw=lambda rect, window: window.draw_image('plus', rect),
				click=None
			),
		]
	)

def createTemp():
	res = []
	index = 0

	if index < 2 and plants.get(SelectedTile.val):
		res.append(carteIndustry(index))
		index += 1

	if index < 2 and TerrainTile.ressource(get_terrain_tile(SelectedTile.val)):
		res.append(carteRessource(index))
		index += 1
	
	if index < 2:
		res.append(cartePlus(index))
		index += 1

	sideMenu.add_temp(res)
	sideMenu.show()

def showSideMenu():
	if sideMenu._hidden:
		createTemp()