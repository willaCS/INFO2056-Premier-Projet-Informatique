import Window
from model import Speed
from model.market import player_wallet
from ui import Screenmode, visual_config as vc
from ui.common.buttons import centerTextButton
from ui.components.tech import drawTech
from ui.framework import button_new, composant_new, composant_show, drawRect, drawText, longNumber, drawCircle, drawImage 
from ui import gestionMenu
 

def draw_exit_button(rect):
	drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH, hover=vc.PRIMARY)
	drawImage('exit', rect)



TOP_BAR_HEIGHT = 60
PADDING = 5

STAT_WIDTH = 300

COLOR_DARK_RED = (120, 0, 0)
COLOR_GRAY = (80, 80, 80)

def drawStat(rect, num, num_incr, color, hasHover):
	longNumber(num)
	message = f"{longNumber(num)} (+{longNumber(num_incr)})"
	drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH, hover=vc.SECONDARY if hasHover else None)
	drawCircle(
		(rect[0][0] + rect[1][1] // 2, rect[0][1] + rect[1][1] // 2),
		TOP_BAR_HEIGHT // 2 - PADDING * 2,
		color,
	)
	drawText('font2', (rect[0][0] + rect[1][0] - PADDING, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "midright")

topBar = composant_new(1, [
	# Background
	button_new(1,
		lambda : (
			(0, 0),
			(Window.resolution[0], TOP_BAR_HEIGHT)
		),
		lambda rect: drawRect(rect, (40, 40, 40)),
		lambda pos: None,
	),

	# Mode de la carte
	*(button_new(2,
		(
			((TOP_BAR_HEIGHT - PADDING) * index + PADDING, PADDING),
			(TOP_BAR_HEIGHT - 2 * PADDING, TOP_BAR_HEIGHT - 2 * PADDING)
		),
		lambda rect, value=value: centerTextButton(rect, 
			'font1', f"{value[0]}",
			vc.ACCENT if Screenmode.val == value[1] else vc.BACKGROUND,
			vc.ROUNDING_SMOOTH, vc.PRIMARY
		),
		lambda pos, value=value: Screenmode.select(value[1])
	) for index, value in enumerate([
		("A", Screenmode.SCREENMODE_MAIN),
		("B", Screenmode.SCREENMODE_ECONOMY_SUPPLY),
		("C", Screenmode.SCREENMODE_ECONOMY_DEMAND),
		("D", Screenmode.SCREENMODE_TRANSPORT),
	])),

	# Money
	button_new(2,
		(
			((TOP_BAR_HEIGHT - PADDING) * 4 + PADDING, PADDING),
			(STAT_WIDTH, TOP_BAR_HEIGHT - 2 * PADDING)
		),
		lambda rect: drawStat(rect, player_wallet.money, player_wallet.money_incr, (255, 180, 0), False),
		lambda pos: None,
	),

	# Science
	button_new(2,
		(
			((TOP_BAR_HEIGHT - PADDING) * 4 + PADDING * 2 + STAT_WIDTH, PADDING),
			(STAT_WIDTH, TOP_BAR_HEIGHT - 2 * PADDING)
		),
		lambda rect: drawStat(rect, player_wallet.science, player_wallet.science_incr, (0, 200, 200), True),
		lambda pos: drawTech(),
	),
	
	# Vitesse de la simulation
	*(button_new(2,
		lambda i=i: (
			(Window.resolution[0] - (7-i) * (TOP_BAR_HEIGHT - PADDING), 0 + PADDING),
			(TOP_BAR_HEIGHT - 2 * PADDING, TOP_BAR_HEIGHT - 2 * PADDING)
		),
		lambda rect, i=i: centerTextButton(rect, 
			'font1', f"{i}",
			vc.PRIMARY if Speed.val == 0 else vc.ACCENT if Speed.val >= i else vc.BACKGROUND,
			vc.ROUNDING_SMOOTH, vc.PRIMARY
		),
		lambda pos, i=i: Speed.set(i),
	) for i in range(1, 6)),

	#exit
	button_new(2, 
		lambda: (
			(Window.resolution[0] - 1 * (TOP_BAR_HEIGHT - PADDING), 0 + PADDING),
			(TOP_BAR_HEIGHT - 2 * PADDING, TOP_BAR_HEIGHT - 2 * PADDING)
		), 
		draw_exit_button, 
		lambda pos: gestionMenu.change_menu(gestionMenu.MENU_INTRO)
	)
])


def showTopBar():
	composant_show(topBar) 