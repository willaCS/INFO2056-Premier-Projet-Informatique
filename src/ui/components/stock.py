import Window
from model.market import Goods
from model.market.stockpile import get_stock
from ui import SelectedTile
from ui import visual_config as vc
from ui.map.goods import draw_goods
from ui.map.industry import PADDING
from ui.map.terrainTile import print_terrain_tile
from ui.common.buttons import centerRightTextButton, centerTextButton, exit_button
from ui.framework import component, component_hide, component_show, drawRect, drawImage
from model.terrain.terrain import get_terrain_tile


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
CLOSE_BUTTON_SIZE = (75, 75)
RESOURCE_BUTTON_HEIGHT = (Window.resolution[1]- 2 * (MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING) - vc.TOP_BAR_HEIGHT - 2 * vc.PADDING- CLOSE_BUTTON_SIZE[1]) / 2

NUMBER_OF_GOODS = Goods.GOODS_SAND
NUMBER_OF_COLUMNS = 3

RATIO = (
	NUMBER_OF_COLUMNS,
	NUMBER_OF_GOODS // NUMBER_OF_COLUMNS + 1,
)

def showStockMenu(pos):
	component_show(stockMenu)

def closeStockMenu(pos):
	global stockMenu
	SelectedTile.val = None
	component_hide(stockMenu)

def drawStock(goods_id):
	good = draw_goods(goods_id)
	def res(rect):
		drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD)
		rectangle = ((rect[0][0] + vc.PADDING, rect[0][1] + vc.PADDING), (rect[1][1] - 2 * vc.PADDING, rect[1][1] - 2 * vc.PADDING))
		good(rectangle)
		centerRightTextButton((
			(rectangle[0][0] + rectangle[1][0] + vc.PADDING, rectangle[0][1]),
			(rect[1][0] - 2 * vc.PADDING - rectangle[1][0] - vc.PADDING, rect[1][1] - 2 * vc.PADDING)
		), 'font3', '{}'.format(get_stock(goods_id)), vc.BACKGROUND2, vc.ROUNDING_SMOOTH, vc.PADDING)
	return res


stockMenu = component(
	z=3,
	margin=vc.PADDING,
	padding=vc.PADDING + vc.MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, vc.TOP_BAR_HEIGHT),
		(vc.LARGEUR_SIDEMENU, parent[1][1] - vc.TOP_BAR_HEIGHT),
	),
	draw=lambda rect: drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH) or \
					  drawRect(rect, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.MENU_BORDER_WIDTH),
	click=lambda pos: None,
	clickOutside=closeStockMenu,
	childs=[
		# Header
		component(
			z=2,
			rect=lambda parent: 
			(
				(0, 0),
				(
					parent[1][0] - vc.PADDING - CLOSE_BUTTON_SIZE[0],
					CLOSE_BUTTON_SIZE[1]
				)
			),
			draw=lambda rect: centerTextButton(rect, "font2", "Stock", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
		),

		# Close button
		component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - CLOSE_BUTTON_SIZE[0], 0),
				CLOSE_BUTTON_SIZE
			),
			draw=exit_button,
			click=closeStockMenu,
		),

		component(
			z=2,
			rect=lambda parent: (
				(0 - vc.PADDING // 2, CLOSE_BUTTON_SIZE[1] + vc.PADDING // 2),
				(parent[1][0] + vc.PADDING, parent[1][1] - CLOSE_BUTTON_SIZE[1] + vc.PADDING)
			),
			draw=lambda rect: None,
			childs=[
				*[component(
					z=2,
					margin=vc.PADDING // 2,
					rect=lambda parent, x=(i % NUMBER_OF_COLUMNS), y=(i // NUMBER_OF_COLUMNS): (
						(
							x * (parent[1][0] // RATIO[0]),
							y * (parent[1][1] // RATIO[1]),
						),
						(
							parent[1][0] // RATIO[0],
							parent[1][1] // RATIO[1],
						)
					),
					draw=drawStock(i+1)
				) for i in range(Goods.GOODS_SAND)],
			]
		),

	]
)
