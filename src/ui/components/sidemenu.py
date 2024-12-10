import Window
from ui import SelectedTile
from ui import visual_config as vc
from ui.components.placeBuildings import ui_component_placeBuilding_showplaceBuildingsMenu
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.framework import ui_framework_framework_component_add_temp, ui_framework_framework_component_temp_remove
from ui.framework.image import ui_framework_image_drawImage
from ui.framework.text import longNumber
from ui.map.terrainTile import ui_map_terrainTile_print_terrain_tile
from ui.map.goods import ui_map_goods_draw_goods, ui_map_goods_ressources_to_goods, ui_map_goods_print_goods
from ui.map.industry import ui_map_industry_draw_industry_menu2, ui_map_industry_print_industry, ui_map_industry_draw_industry_product
from ui.common.buttons import ui_common_centerLeftTextButton, ui_common_centerRightTextButton, ui_common_centerTextButton, ui_common_exit_button
from ui.framework.framework import ui_framework_framework_component, ui_framework_framework_component_hide, ui_framework_framework_component_show
from model.terrain import Ressource, TerrainTile
from model.terrain.terrain import model_terrain_terrain_get_terrain_tile
from model.industry import plants
from model.industry import Plant


ui_component_sidemenu_MENU_MARGIN = 5 #en pixels
ui_component_sidemenu_HEADER_HEIGHT = 75
ui_component_sidemenu_CLOSE_BUTTON_SIZE = (75, 75)
ui_component_sidemenu_RESOURCE_CARTE_HEIGHT = (Window.Window_resolution[1] - 2 * (ui_component_sidemenu_MENU_MARGIN + vc.VC_MENU_BORDER_WIDTH + vc.VC_PADDING) - vc.VC_TOP_BAR_HEIGHT - 2 * vc.VC_PADDING - ui_component_sidemenu_CLOSE_BUTTON_SIZE[1]) / 2
ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT = (ui_component_sidemenu_RESOURCE_CARTE_HEIGHT - 6 * vc.VC_PADDING) / 5


def closeSideMenu():
	global sideMenu
	SelectedTile.SelectedTile_val = None
	ui_framework_framework_component_hide(sideMenu) 
	ui_framework_framework_component_temp_remove(sideMenu)

def refreshSideMenu():
	global sideMenu
	ui_framework_framework_component_temp_remove(sideMenu)
	createTemp()


def __drawRessourceButton(rect, good):
	ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH)
	position, taille = rect
	draw_func = ui_map_goods_draw_goods(good)
	draw_func(((position[0] + (taille[1] - 50) / 2, position[1] + (taille[1] - 50) / 2), (50, 50)))
	ui_common_centerTextButton(
		(
			(position[0] + 50 + 2 * vc.VC_PADDING, position[1] + vc.VC_PADDING),
			(taille[0] - 2 * vc.VC_PADDING - 50 - vc.VC_PADDING, taille[1] - 2 * vc.VC_PADDING)
		),
		'font3', '{}'.format(ui_map_goods_print_goods(good)),
		vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH
	)

def __drawBuildingButton(rect, building_id):
	ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH)
	position, taille = rect
	draw_func = ui_map_industry_draw_industry_menu2(building_id)
	draw_func(((position[0] + (taille[1] - 50) / 2, position[1] + (taille[1] - 50) / 2), (50, 50)), False)
	ui_common_centerTextButton(
		(
			(position[0] + 50 + 2 * vc.VC_PADDING, position[1] + vc.VC_PADDING),
			(taille[0] - 2 * vc.VC_PADDING - 50 - vc.VC_PADDING, taille[1] - 2 * vc.VC_PADDING)
		),
		'font3', '{}'.format(ui_map_industry_print_industry(building_id)),
		vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH
	)


sideMenu = ui_framework_framework_component(
	z=2,
	margin=ui_component_sidemenu_MENU_MARGIN,
	padding=vc.VC_PADDING + vc.VC_MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, vc.VC_TOP_BAR_HEIGHT),
		(vc.VC_LARGEUR_SIDEMENU, parent[1][1] - vc.VC_TOP_BAR_HEIGHT),
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH) or\
					  ui_framework_draw_drawRect(rect, vc.VC_PRIMARY, vc.VC_ROUNDING_SMOOTH, vc.VC_MENU_BORDER_WIDTH),
	click=lambda pos: None,
	clickOutside=closeSideMenu,
	childs=[
		# Header
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: 
			(
				(0, 0),
				(
					parent[1][0] - vc.VC_PADDING - ui_component_sidemenu_HEADER_HEIGHT,
					ui_component_sidemenu_HEADER_HEIGHT
				)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, "font2", ui_map_terrainTile_print_terrain_tile(model_terrain_terrain_get_terrain_tile(SelectedTile.SelectedTile_val)) if SelectedTile.SelectedTile_val else "", vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH)
		),

		# Close button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - ui_component_sidemenu_CLOSE_BUTTON_SIZE[0], 0),
				(ui_component_sidemenu_HEADER_HEIGHT, ui_component_sidemenu_HEADER_HEIGHT)
			),
			draw=ui_common_exit_button,
			click=closeSideMenu
		),
	]
)

def carteRessource(pos):
	terrain = model_terrain_terrain_get_terrain_tile(SelectedTile.SelectedTile_val)
	ressource = TerrainTile.model_terrain_terrainTile_ressource(terrain)
	if not ressource:
		return
	goods = ui_map_goods_ressources_to_goods(Ressource.model_terrain_ressource_type(ressource))
	return ui_framework_framework_component(
		z=2,
		padding=vc.VC_PADDING,
		rect=lambda parent: (
			(
				0,
				ui_component_sidemenu_HEADER_HEIGHT + vc.VC_PADDING + pos * (ui_component_sidemenu_RESOURCE_CARTE_HEIGHT + vc.VC_PADDING),
			),
			(
				parent[1][0],
				ui_component_sidemenu_RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect: ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH),
		childs=[
			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(0, 0),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: ui_common_centerTextButton(rect, "font3", "Ressources", vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH,),
			),

			*(ui_framework_framework_component(
				z=3,
				rect=lambda parent, y=index: (
					(
						0,
						(y + 1) * (ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + vc.VC_PADDING),
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect, is_in, good=good: __drawRessourceButton(rect, good)
			)
			for index,good in enumerate(goods)
			),
		]
	)


def carteIndustry(pos):
	building = plants.model_plants_get(SelectedTile.SelectedTile_val)
	building_id = Plant.model_Plant_type(building)
	if not plants.model_plants_get(SelectedTile.SelectedTile_val):
		return

	return ui_framework_framework_component(
		z=2,
		padding=vc.VC_PADDING,
		rect=lambda parent: (
			(
				0,
				ui_component_sidemenu_HEADER_HEIGHT + vc.VC_PADDING + pos * (ui_component_sidemenu_RESOURCE_CARTE_HEIGHT + vc.VC_PADDING),
			),
			(
				parent[1][0],
				ui_component_sidemenu_RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect: ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH),
		childs=[
			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(0, 0),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: ui_common_centerTextButton(rect, "font3", "Building", vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH),
			),

			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + vc.VC_PADDING) * 1,
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect, is_in, building_id=building_id: __drawBuildingButton(rect, building_id)
			),

			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + vc.VC_PADDING) * 2,
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=ui_map_industry_draw_industry_product(building_id),
				childs=[],
			),

			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + vc.VC_PADDING) * 3,
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: None,
				childs=[
					ui_framework_framework_component(
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
						draw=lambda rect: ui_common_centerLeftTextButton(
							rect,
							'font3', '{}'.format("Generated"),
							vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH, vc.VC_PADDING
						)
					),
					
					ui_framework_framework_component(
						z=3,
						rect=lambda parent: (
							(
								parent[1][0] // 2 + vc.VC_PADDING,
								0,
							),
							(
								parent[1][0] // 2 - vc.VC_PADDING,
								parent[1][1],
							)
						),
						draw=lambda rect: ui_common_centerRightTextButton(
							rect,
							'font3', longNumber(building['generated']),
							vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH, vc.VC_PADDING
						)
					),
				],
			),

			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + vc.VC_PADDING) * 4,
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: None,
				childs=[
					ui_framework_framework_component(
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
						draw=lambda rect: ui_common_centerLeftTextButton(
							rect,
							'font3', '{}'.format("Level"),
							vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH, vc.VC_PADDING
						)
					),
					
					ui_framework_framework_component(
						z=3,
						rect=lambda parent: (
							(
								parent[1][0] // 2 + vc.VC_PADDING,
								0,
							),
							(
								parent[1][0] // 2 - vc.VC_PADDING,
								parent[1][1],
							)
						),
						draw=lambda rect: ui_common_centerRightTextButton(
							rect,
							'font3', longNumber(0),
							vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH, vc.VC_PADDING
						)
					),
				],
			),

		]
	)

def cartePlus(pos):
	return ui_framework_framework_component(
		z=2,
		padding=vc.VC_PADDING,
		rect=lambda parent: (
			(
				0,
				ui_component_sidemenu_HEADER_HEIGHT + vc.VC_PADDING + pos * (ui_component_sidemenu_RESOURCE_CARTE_HEIGHT + vc.VC_PADDING),
			),
			(
				parent[1][0],
				ui_component_sidemenu_RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect: ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH, hover=vc.VC_ACCENT),
		click=ui_component_placeBuilding_showplaceBuildingsMenu,
		childs=[
			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					((parent[1][0] - parent[1][1]) // 2, 0),
					(
						parent[1][1],
						parent[1][1],
					)
				),
				draw=lambda rect: ui_framework_image_drawImage('plus', rect),
				click=None
			),
		]
	)

def createTemp():
	res = []
	index = 0
	# print(get(SelectedTile.val))


	if index < 2 and plants.model_plants_get(SelectedTile.SelectedTile_val):
		res.append(carteIndustry(index))
		index += 1

	if index < 2 and TerrainTile.model_terrain_terrainTile_ressource(model_terrain_terrain_get_terrain_tile(SelectedTile.SelectedTile_val)):
		res.append(carteRessource(index))
		index += 1
	
	if index < 2:
		res.append(cartePlus(index))
		index += 1

	ui_framework_framework_component_add_temp(sideMenu, res)
	ui_framework_framework_component_show(sideMenu)

def showSideMenu():
	if sideMenu['_hidden']:
		createTemp()