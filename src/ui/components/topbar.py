import pygame
import Window
from globals import Screenmode, Speed, all
from ui.utils.ui_array import button_new, composant_new, composant_show


TOP_BAR_HEIGHT = 60
PADDING_OUT = 10
PADDING_IN = 10

COLOR_DARK_RED = (120, 0, 0)
COLOR_GRAY = (80, 80, 80)



def drawModeButton(rect, text, color):
	pygame.draw.rect(Window.inst, color, rect)
	text_prepared = all.font.render(text, True, (0, 0, 0))
	Window.inst.blit(text_prepared, (rect[0][0] + 9, rect[0][1] - 3))




topBar = composant_new(1, [
	# Background
	button_new(1,
		lambda : (
			(0, 0),
			(Window.resolution[0], TOP_BAR_HEIGHT)
		),
		lambda rect: pygame.draw.rect(Window.inst, (40, 40, 40), rect),
		lambda pos: None,
	),

	# Mode de la carte
	*(button_new(2,
		(
			(50 * index + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect, value=value: drawModeButton(rect, f"{value[0]}", all.COLOR_WHITE if Screenmode.val == value[1] else COLOR_GRAY),
		lambda pos, value=value: Screenmode.select(value[1])
	) for index, value in enumerate([
		("A", Screenmode.SCREENMODE_MAIN),
		("B", Screenmode.SCREENMODE_ECONOMY_SUPPLY),
		("C", Screenmode.SCREENMODE_ECONOMY_DEMAND),
		("D", Screenmode.SCREENMODE_TRANSPORT),
	])),
	
	# Vitesse de la simulation
	*(button_new(2,
		lambda i=i: (
			(Window.resolution[0] - 10 - (6-i) * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect, i=i: drawModeButton(rect, f"{i}", COLOR_DARK_RED if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= i else COLOR_GRAY),
		lambda pos, i=i: Speed.set(i),
	) for i in range(1, 6)),
])


def showTopBar():
	composant_show(topBar)