import pygame
import Window
from globals import Screenmode, Speed, all
from ui.ui_array import button_new, composant_new, composant_show


TOP_BAR_HEIGHT = 60
PADDING_OUT = 10
PADDING_IN = 10




def drawModeButton(rect, text, color):
	pygame.draw.rect(Window.inst, color, rect)
	text_prepared = all.font.render(text, True, (0, 0, 0))
	Window.inst.blit(text_prepared, (rect[0][0] + 9, rect[0][1] - 3))




topBar = composant_new(1, [
	button_new(1,
		lambda : (
			(0, 0),
			(Window.resolution[0], TOP_BAR_HEIGHT)
		),
		lambda rect: pygame.draw.rect(Window.inst, (40, 40, 40), rect),
		lambda pos: None,
	),


	button_new(2,
		(
			(0 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "A", all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_MAIN else (80, 80, 80)),
		lambda pos: Screenmode.select(Screenmode.SCREENMODE_MAIN)
	),
	button_new(2,
		(
			(50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "B", all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_ECONOMY_SUPPLY else (80, 80, 80)),
		lambda pos: Screenmode.select(Screenmode.SCREENMODE_ECONOMY_SUPPLY)
	),
	button_new(2,
		(
			(100 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "C", all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_ECONOMY_DEMAND else (80, 80, 80)),
		lambda pos: Screenmode.select(Screenmode.SCREENMODE_ECONOMY_DEMAND)
	),
	button_new(2,
		(
			(150 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "D", all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_TRANSPORT else (80, 80, 80)),
		lambda pos: Screenmode.select(Screenmode.SCREENMODE_TRANSPORT)
	),

	
	button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 5 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "1", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 1 else (80, 80, 80)),
		lambda pos: Speed.set(1),
	),
	button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 4 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "2", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 2 else (80, 80, 80)),
		lambda pos: Speed.set(2),
	),
	button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 3 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "3", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 3 else (80, 80, 80)),
		lambda pos: Speed.set(3),
	),
	button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 2 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "4", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 4 else (80, 80, 80)),
		lambda pos: Speed.set(4),
	),
	button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 1 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "5", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 5 else (80, 80, 80)),
		lambda pos: Speed.set(5),
	),
])


def showTopBar():
	composant_show(topBar)