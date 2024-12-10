import Window
from model.market import Goods
from model.market.stockpile import model_market_stockpile_get_stock
from ui import SelectedTile
from ui import visual_config as vc
from ui.framework.draw import ui_framework_draw_drawRect
from ui.map.goods import ui_map_goods_draw_goods
from ui.map.industry import ui_map_industry_PADDING
from ui.map.terrainTile import ui_map_terrainTile_print_terrain_tile
from ui.common.buttons import ui_common_centerRightTextButton, ui_common_centerTextButton, ui_common_exit_button
from ui.framework.framework import ui_framework_framework_component, ui_framework_framework_component_hide, ui_framework_framework_component_show
from model.terrain.terrain import model_terrain_terrain_get_terrain_tile


ui_component_stock_MENU_MARGIN = 5 #en pixels
ui_component_stock_EXIT_BUTTON_BORDER = 2 #en pixels
ui_component_stock_CLOSE_BUTTON_SIZE = (75, 75)
ui_component_stock_RESOURCE_BUTTON_HEIGHT = (Window.Window_resolution[1]- 2 * (ui_component_stock_MENU_MARGIN + vc.VC_MENU_BORDER_WIDTH + vc.VC_PADDING) - vc.VC_TOP_BAR_HEIGHT - 2 * vc.VC_PADDING- ui_component_stock_CLOSE_BUTTON_SIZE[1]) / 2

ui_component_stock_NUMBER_OF_GOODS = Goods.model_market_goods_GOODS_SAND
ui_component_stock_NUMBER_OF_COLUMNS = 3

ui_component_stock_RATIO = (
	ui_component_stock_NUMBER_OF_COLUMNS,
	ui_component_stock_NUMBER_OF_GOODS // ui_component_stock_NUMBER_OF_COLUMNS + 1,
)

def ui_component_stock_showStockMenu(pos):
	ui_framework_framework_component_show(ui_component_stock_stockMenu)

def ui_component_stock_closeStockMenu(pos):
	global ui_component_stock_stockMenu
	SelectedTile.SelectedTile_val = None
	ui_framework_framework_component_hide(ui_component_stock_stockMenu)

def ui_component_stock_drawStock(goods_id):
	good = ui_map_goods_draw_goods(goods_id)
	def res(rect):
		ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND3, vc.VC_ROUNDING_HARD)
		rectangle = ((rect[0][0] + vc.VC_PADDING, rect[0][1] + vc.VC_PADDING), (rect[1][1] - 2 * vc.VC_PADDING, rect[1][1] - 2 * vc.VC_PADDING))
		good(rectangle)
		ui_common_centerRightTextButton((
			(rectangle[0][0] + rectangle[1][0] + vc.VC_PADDING, rectangle[0][1]),
			(rect[1][0] - 2 * vc.VC_PADDING - rectangle[1][0] - vc.VC_PADDING, rect[1][1] - 2 * vc.VC_PADDING)
		), 'font3', '{}'.format(model_market_stockpile_get_stock(goods_id)), vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH, vc.VC_PADDING)
	return res


ui_component_stock_stockMenu = ui_framework_framework_component(
	z=3,
	margin=vc.VC_PADDING,
	padding=vc.VC_PADDING + vc.VC_MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, vc.VC_TOP_BAR_HEIGHT),
		(vc.VC_LARGEUR_SIDEMENU, parent[1][1] - vc.VC_TOP_BAR_HEIGHT),
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH) or \
					  ui_framework_draw_drawRect(rect, vc.VC_PRIMARY, vc.VC_ROUNDING_SMOOTH, vc.VC_MENU_BORDER_WIDTH),
	click=lambda pos: None,
	clickOutside=ui_component_stock_closeStockMenu,
	childs=[
		# Header
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: 
			(
				(0, 0),
				(
					parent[1][0] - vc.VC_PADDING - ui_component_stock_CLOSE_BUTTON_SIZE[0],
					ui_component_stock_CLOSE_BUTTON_SIZE[1]
				)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, "font2", "Stock", vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH)
		),

		# Close button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - ui_component_stock_CLOSE_BUTTON_SIZE[0], 0),
				ui_component_stock_CLOSE_BUTTON_SIZE
			),
			draw=ui_common_exit_button,
			click=ui_component_stock_closeStockMenu,
		),

		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(0 - vc.VC_PADDING // 2, ui_component_stock_CLOSE_BUTTON_SIZE[1] + vc.VC_PADDING // 2),
				(parent[1][0] + vc.VC_PADDING, parent[1][1] - ui_component_stock_CLOSE_BUTTON_SIZE[1] + vc.VC_PADDING)
			),
			draw=lambda rect: None,
			childs=[
				*[ui_framework_framework_component(
					z=2,
					margin=vc.VC_PADDING // 2,
					rect=lambda parent, x=(i % ui_component_stock_NUMBER_OF_COLUMNS), y=(i // ui_component_stock_NUMBER_OF_COLUMNS): (
						(
							x * (parent[1][0] // ui_component_stock_RATIO[0]),
							y * (parent[1][1] // ui_component_stock_RATIO[1]),
						),
						(
							parent[1][0] // ui_component_stock_RATIO[0],
							parent[1][1] // ui_component_stock_RATIO[1],
						)
					),
					draw=ui_component_stock_drawStock(i+1)
				) for i in range(Goods.model_market_goods_GOODS_SAND)],
			]
		),

	]
)
