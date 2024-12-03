import Window
from model.market import Goods
from model.market.stockpile import get_stock
from ui import SelectedTile
from ui import visual_config as vc
from ui.map.goods import draw_goods
from ui.map.industry import PADDING
from ui.map.terrainTile import print_terrain_tile
from ui.common.buttons import centerRightTextButton, centerTextButton
from ui.framework import button_new, composant_hide, composant_new, composant_show, drawRect, drawImage
from model.terrain.terrain import get_terrain_tile


MENU_MARGIN = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels
CLOSE_BUTTON_SIZE = (75, 75)
RESOURCE_BUTTON_HEIGHT = (Window.resolution[1]- 2 * (MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING) - vc.TOP_BAR_HEIGHT - 2 * vc.PADDING- CLOSE_BUTTON_SIZE[1]) / 2
LARGEUR_SIDEMENU = 470

NUMBER_OF_GOODS = Goods.GOODS_SAND
NUMBER_OF_COLUMNS = 3

def showStockMenu(pos):
	composant_show(stockMenu)

def closeStockMenu(pos):
	global stockMenu
	SelectedTile.val = None
	composant_hide(stockMenu)


def rect_stock(i):
	print(i)
	size_menu = (
		LARGEUR_SIDEMENU - 2 * (MENU_MARGIN + vc.PADDING + vc.MENU_BORDER_WIDTH),
		(Window.resolution[1] - vc.TOP_BAR_HEIGHT - 2 * (vc.MENU_BORDER_WIDTH + vc.PADDING + MENU_MARGIN) - vc.PADDING - CLOSE_BUTTON_SIZE[1])
	)
	size_stock = (
		(size_menu[0] - (vc.PADDING - 1) * (NUMBER_OF_COLUMNS)) // (NUMBER_OF_COLUMNS),
		(size_menu[1] - (vc.PADDING - 1) * (NUMBER_OF_GOODS // NUMBER_OF_COLUMNS + 1)) // (NUMBER_OF_GOODS // NUMBER_OF_COLUMNS + 1)
	)
	return (
		(
			MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING + (i % NUMBER_OF_COLUMNS) * (size_stock[0] + vc.PADDING),
			vc.TOP_BAR_HEIGHT + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING + CLOSE_BUTTON_SIZE[1] + vc.PADDING + (i // NUMBER_OF_COLUMNS) * (size_stock[1] + vc.PADDING)
		),
		size_stock
	)

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


stockMenu = composant_new(2, [
	# Background
	button_new(1,
		lambda: (
			(0 + MENU_MARGIN, vc.TOP_BAR_HEIGHT + MENU_MARGIN),
			(LARGEUR_SIDEMENU - 2 * MENU_MARGIN, Window.resolution[1] - vc.TOP_BAR_HEIGHT - 2 * MENU_MARGIN),
		),
		lambda rect: drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH) or \
					drawRect(rect, vc.PRIMARY, vc.ROUNDING_SMOOTH, vc.MENU_BORDER_WIDTH),
		lambda pos: None,
		closeStockMenu,
	),


	# Header
	button_new(
		2,
		lambda: 
		(
			(
				0 + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING,
				vc.TOP_BAR_HEIGHT + MENU_MARGIN + vc.MENU_BORDER_WIDTH + vc.PADDING
			),
			(
				LARGEUR_SIDEMENU - 2 * (vc.MENU_BORDER_WIDTH + vc.PADDING) - vc.PADDING - 2 * MENU_MARGIN - CLOSE_BUTTON_SIZE[0],
				CLOSE_BUTTON_SIZE[1]
			)
		),
		lambda rect: centerTextButton(rect, "font2", "Stock", vc.BACKGROUND3, vc.ROUNDING_SMOOTH)
	),

	*[button_new(
		2,
		rect_stock(i=i),
		drawStock(i+1)
	) for i in range(Goods.GOODS_SAND)],


	# Close button
	button_new(
		2,
		lambda: (
			(
				LARGEUR_SIDEMENU - MENU_MARGIN - vc.PADDING - vc.MENU_BORDER_WIDTH - CLOSE_BUTTON_SIZE[0],
				vc.TOP_BAR_HEIGHT + MENU_MARGIN + vc.PADDING + vc.MENU_BORDER_WIDTH
			),
			CLOSE_BUTTON_SIZE
		),
		lambda rect: drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD) or \
					drawImage('exit', rect),
		closeStockMenu,
	),
])
