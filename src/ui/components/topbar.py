from model.stat import utils
from model import Speed
from model.market import player_wallet
from ui.utils import longNumber
from utils.Components import Component
from ui import Screenmode, visual_config as vc
from ui.common.buttons import centerTextButton, exit_button
from ui.components.stock import showStockMenu
from ui.components.tech import drawTech
from ui import gestionMenu
from utils.Window import Window

PADDING = 5

STAT_WIDTH = 300

COLOR_DARK_RED = (120, 0, 0)
COLOR_GRAY = (80, 80, 80)

def drawStat(rect, window: Window, num, num_incr, image_key):
	longNumber(num)
	message = f"{longNumber(num)}"
	window.draw_rect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH, hover=vc.SECONDARY)
	window.draw_image(image_key, (
		rect[0],
		(rect[1][1], rect[1][1])
	))
	window.draw_text('font2', (rect[0][0] + rect[1][0] - PADDING, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "midright")

topBar = Component(
	z=1,
	padding=vc.PADDING,
	rect=lambda parent: (
		(0, 0),
		(parent[1][0], vc.TOP_BAR_HEIGHT)
	),
	draw=lambda rect, window: window.draw_rect(rect, vc.BACKGROUND3),
	click=lambda: None,
	childs=[
		# Mode de la carte
		*(Component(
			z=2,
			# margin=vc.PADDING,
			rect=lambda parent, index=index: (
				((parent[1][1] + vc.PADDING) * index, 0),
				(parent[1][1], parent[1][1])
			),
			draw=lambda rect, value=value: centerTextButton(rect, 
				'font1', value[0],
				vc.ACCENT if Screenmode.val == value[1] else vc.BACKGROUND,
				vc.ROUNDING_SMOOTH, vc.PRIMARY
			),
			click=lambda pos, value=value: Screenmode.select(value[1])
		) for index, value in enumerate([
			("A", Screenmode.SCREENMODE_MAIN),
			("B", Screenmode.SCREENMODE_ECONOMY_SUPPLY),
		])),

		# Money
		Component(
			z=2,
			rect=lambda parent: (
				((parent[1][1] + vc.PADDING) * 2, 0),
				(STAT_WIDTH, parent[1][1])
			),
			draw=lambda rect, window: drawStat(rect, window, player_wallet.money, utils.get_stat('money'), 'money'),
			click=showStockMenu,
		),

		# Science
		Component(
			z=2,
			rect=lambda parent: (
				((parent[1][1] + vc.PADDING) * 2 + (STAT_WIDTH + vc.PADDING), 0),
				(STAT_WIDTH, parent[1][1])
			),
			draw=lambda rect, window: drawStat(rect, window, player_wallet.science, utils.get_stat('science'), 'science'),
			click=drawTech,
		),
		
		# Vitesse de la simulation
		*(Component(
			z=2,
			rect=lambda parent, i=i: (
				(parent[1][0] - (7-i) * (parent[1][1] + vc.PADDING) + vc.PADDING, 0),
				(parent[1][1], parent[1][1])
			),
			draw=lambda rect, window, is_in, i=i: centerTextButton( 
				'font1', f"{i}",
				vc.PRIMARY if Speed.val == 0 else vc.ACCENT if Speed.val >= i else vc.BACKGROUND,
				vc.ROUNDING_SMOOTH, vc.PRIMARY
			)(rect, window, is_in),
			click=lambda i=i: Speed.set(i),
		) for i in range(1, 6)),

		#exit
		Component(
			z=2, 
			rect=lambda parent: (
				(parent[1][0] - (parent[1][1]), 0),
				(parent[1][1], parent[1][1])
			), 
			draw=exit_button, 
			click=lambda: gestionMenu.change_menu(gestionMenu.MENU_INTRO)
		)
	]
)


def showTopBar():
	topBar.show() 