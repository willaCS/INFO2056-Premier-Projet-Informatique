from model.stat import utils
import Window
from model import Speed
from model.market import player_wallet
from ui import Screenmode, visual_config as vc
from ui.common.buttons import ui_common_centerTextButton, ui_common_exit_button
from ui.components.stock import ui_component_stock_showStockMenu
from ui.components.tech import ui_component_tech_drawTech
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.framework import ui_framework_framework_component, ui_framework_framework_component_show, ui_framework_framework_component_hide
from ui import gestionMenu
from ui.framework.image import ui_framework_image_drawImage
from ui.framework.text import ui_framework_text_drawText, longNumber

ui_component_tobpar_PADDING = 5

ui_component_tobpar_STAT_WIDTH = 300

ui_component_tobpar_COLOR_DARK_RED = (120, 0, 0)
ui_component_tobpar_COLOR_GRAY = (80, 80, 80)

def ui_component_tobpar_drawStat(rect, num, num_incr, image_key):
	longNumber(num)
	message = f"{longNumber(num)} ({'+' if num_incr >= 0 else ''}{longNumber(num_incr)})"
	ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH, hover=vc.VC_SECONDARY)
	ui_framework_image_drawImage(image_key, (
		rect[0],
		(rect[1][1], rect[1][1])
	))
	ui_framework_text_drawText('font2', (rect[0][0] + rect[1][0] - ui_component_tobpar_PADDING, rect[0][1] + rect[1][1] // 2), message, vc.VC_TEXT, "midright")

ui_component_tobpar_topBar = ui_framework_framework_component(
	z=1,
	padding=vc.VC_PADDING,
	rect=lambda parent: (
		(0, 0),
		(parent[1][0], vc.VC_TOP_BAR_HEIGHT)
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND3),
	click=lambda pos: None,
	childs=[
		# Mode de la carte
		*(ui_framework_framework_component(
			z=2,
			# margin=vc.PADDING,
			rect=lambda parent, index=index: (
				((parent[1][1] + vc.VC_PADDING) * index, 0),
				(parent[1][1], parent[1][1])
			),
			draw=lambda rect, is_in, value=value: ui_common_centerTextButton(rect, 
				'font1', value[0],
				vc.VC_ACCENT if Screenmode.SCREENMODE_val == value[1] else vc.VC_BACKGROUND,
				vc.VC_ROUNDING_SMOOTH, vc.VC_PRIMARY
			),
			click=lambda pos, value=value: Screenmode.select(value[1])
		) for index, value in enumerate([
			("A", Screenmode.SCREENMODE_MAIN),
			("B", Screenmode.SCREENMODE_ECONOMY_SUPPLY),
		])),

		# Money
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				((parent[1][1] + vc.VC_PADDING) * 2, 0),
				(ui_component_tobpar_STAT_WIDTH, parent[1][1])
			),
			draw=lambda rect: ui_component_tobpar_drawStat(rect, player_wallet.model_market_wallet_money, utils.model_stat_setup_get_stat('money'), 'money'),
			click=ui_component_stock_showStockMenu,
		),

		# Science
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				((parent[1][1] + vc.VC_PADDING) * 2 + (ui_component_tobpar_STAT_WIDTH + vc.VC_PADDING), 0),
				(ui_component_tobpar_STAT_WIDTH, parent[1][1])
			),
			draw=lambda rect: ui_component_tobpar_drawStat(rect, player_wallet.model_market_wallet_science, utils.model_stat_setup_get_stat('science'), 'science'),
			click=ui_component_tech_drawTech,
		),
		
		# Vitesse de la simulation
		*(ui_framework_framework_component(
			z=2,
			rect=lambda parent, i=i: (
				(parent[1][0] - (7-i) * (parent[1][1] + vc.VC_PADDING) + vc.VC_PADDING, 0),
				(parent[1][1], parent[1][1])
			),
			draw=lambda rect, hover, i=i: ui_common_centerTextButton(rect, 
				'font1', f"{i}",
				vc.VC_PRIMARY if Speed.val == 0 else vc.VC_ACCENT if Speed.val >= i else vc.VC_BACKGROUND,
				vc.VC_ROUNDING_SMOOTH, vc.VC_PRIMARY
			),
			click=lambda pos, i=i: Speed.model_speed_set(i),
		) for i in range(1, 6)),

		#exit
		ui_framework_framework_component(
			z=2, 
			rect=lambda parent: (
				(parent[1][0] - (parent[1][1]), 0),
				(parent[1][1], parent[1][1])
			), 
			draw=ui_common_exit_button, 
			click=lambda: gestionMenu.change_menu(gestionMenu.GestionMenu_MENU_INTRO)
		)
	]
)


def ui_component_tobpar_showTopBar():
	ui_framework_framework_component_show(ui_component_tobpar_topBar) 