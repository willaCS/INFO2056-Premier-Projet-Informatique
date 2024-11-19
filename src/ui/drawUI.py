"""
Ce fichier permet d'afficher l'interface utilisateur.
"""

from pygame import font
import pygame

import Window
from globals import Screenmode, Speed, all, SelectedTile, player
from utils.mytyping import Color, coord_i
from utils.draw import longNumber
from ui import ui_array

TOP_BAR_HEIGHT = 60
PADDING_OUT = 10
PADDING_IN = 10

top_bar_height = 60
padding_out = 10
padding_in = 2

MENU_BORDER = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels

def getFont() -> font.Font:
	all.font = font.SysFont('monospace', top_bar_height - 2 * padding_out)
	all.font2 = font.SysFont('monospace', 24, True)

def drawText(font: font.Font, coord: coord_i, text: str, color: Color, anchor: str = "topleft"):
	text_prepared = font.render(text, True, color)
	rect = text_prepared.get_rect()
	setattr(rect, anchor, coord)
	Window.inst.blit(text_prepared, rect)

def drawCoin(coord: coord_i, len: int, color: Color, number: int, incr: int):
	pygame.draw.rect(Window.inst, all.COLOR_WHITE, ((coord[0] + padding_out, coord[1] + padding_out), (len, top_bar_height - 2 * padding_out)))
	pygame.draw.circle(Window.inst, color,
		(coord[0] + top_bar_height / 2, coord[1] + top_bar_height / 2),
		top_bar_height / 2 - padding_out - padding_in
	)
	text = longNumber(number) + "(+" + longNumber(incr) + ")"
	drawText(all.font, (coord[0] + len, coord[1] + padding_out - 5), text, all.COLOR_BLACK, "topright")

def __drawSideMenu(rect):
	pygame.draw.rect(Window.inst, all.COLOR_WHITE, ((rect[0][0] + MENU_BORDER, rect[0][1] + MENU_BORDER), (rect[1][0] - 2 * MENU_BORDER, rect[1][1] - 2 * MENU_BORDER)))


def __drawExitButon(rect):
	global EXIT_BUTTON
	pygame.draw.rect(Window.inst, all.COLOR_RED, ((rect[0][0] + EXIT_BUTTON_BORDER, rect[0][1] + EXIT_BUTTON_BORDER), (rect[1][0] - 2 * EXIT_BUTTON_BORDER, rect[1][1] - 2 * EXIT_BUTTON_BORDER)))
	EXIT_BUTTON = resize_image(EXIT_BUTTON, (rect[1][0] - 2 * EXIT_BUTTON_BORDER, rect[1][1] - 2 * EXIT_BUTTON_BORDER))
	Window.inst.blit(EXIT_BUTTON, (rect[0][0] + EXIT_BUTTON_BORDER, rect[0][1] + EXIT_BUTTON_BORDER))

def drawModeButton(rect, text, color):
	pygame.draw.rect(Window.inst, color, rect)
	text_prepared = all.font.render(text, True, (0, 0, 0))
	Window.inst.blit(text_prepared, (rect[0][0] + 9, rect[0][1] - 3))

def closeSideMenu():
	global sideMenu
	SelectedTile.val = None
	ui_array.composant_hide(sideMenu)

sideMenu = ui_array.composant_new(2, [
	ui_array.button_new(1,
		lambda: (
			(0, TOP_BAR_HEIGHT),
			(470, Window.resolution[1] - TOP_BAR_HEIGHT)
		),
		__drawSideMenu,
		lambda: None,
		closeSideMenu,
	),
	ui_array.button_new(2,
		(
			(425, TOP_BAR_HEIGHT),
			(30, 40)
		),
		__drawExitButon,
		closeSideMenu
	),
])

topBar = ui_array.composant_new(1, [
	ui_array.button_new(1,
		lambda : (
			(0, 0),
			(Window.resolution[0], TOP_BAR_HEIGHT)
		),
		lambda rect: pygame.draw.rect(Window.inst, (40, 40, 40), rect),
		lambda: None,
	),


	ui_array.button_new(2,
		(
			(0 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "A", all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_MAIN else (80, 80, 80)),
		lambda: Screenmode.select(Screenmode.SCREENMODE_MAIN)
	),
	ui_array.button_new(2,
		(
			(50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "B", all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_ECONOMY_SUPPLY else (80, 80, 80)),
		lambda: Screenmode.select(Screenmode.SCREENMODE_ECONOMY_SUPPLY)
	),
	ui_array.button_new(2,
		(
			(100 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "C", all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_ECONOMY_DEMAND else (80, 80, 80)),
		lambda: Screenmode.select(Screenmode.SCREENMODE_ECONOMY_DEMAND)
	),
	ui_array.button_new(2,
		(
			(150 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "D", all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_TRANSPORT else (80, 80, 80)),
		lambda: Screenmode.select(Screenmode.SCREENMODE_TRANSPORT)
	),

	
	ui_array.button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 5 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "1", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 1 else (80, 80, 80)),
		lambda: Speed.set(1),
	),
	ui_array.button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 4 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "2", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 2 else (80, 80, 80)),
		lambda: Speed.set(2),
	),
	ui_array.button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 3 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "3", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 3 else (80, 80, 80)),
		lambda: Speed.set(3),
	),
	ui_array.button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 2 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "4", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 4 else (80, 80, 80)),
		lambda: Speed.set(4),
	),
	ui_array.button_new(2,
		lambda: (
			(Window.resolution[0] - 10 - 1 * 50 + PADDING_IN, 0 + PADDING_IN),
			(TOP_BAR_HEIGHT - 2 * PADDING_IN, TOP_BAR_HEIGHT - 2 * PADDING_IN)
		),
		lambda rect: drawModeButton(rect, "5", (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 5 else (80, 80, 80)),
		lambda: Speed.set(5),
	),
])

ui_array.composant_show(topBar)
ui_array.composants.append(sideMenu)
ui_array.composants.append(topBar)

def drawUI():
	global sideMenu	
	
	if SelectedTile.val:
		ui_array.composant_show(sideMenu)
	ui_array.menu_draw()
	drawCoin((200, 0), 400, (255, 180, 0), player.money, player.money_incr)
	drawCoin((610, 0), 400, (0, 200, 200), player.science, player.science_incr)


#ad

#def __drawSideMenu():
#	pygame.draw.rect(Window.inst, all.COLOR_WHITE, ((10, top_bar_height + Window.resolution[1] / 100), (450, Window.resolution[1] - top_bar_height - 16)))
#	pygame.draw.rect(Window.inst, all.COLOR_BLACK, ((425, top_bar_height + Window.resolution[1] / 100 + 5), (30,30)))
#	Window.inst.blit(EXIT_BUTTON, (425, top_bar_height + Window.resolution[1] / 100 + 5))
	
def setup_image():
	global EXIT_BUTTON
	EXIT_BUTTON = pygame.image.load('./assets/close_button.png').convert_alpha(Window.inst)

def resize_image(image, size):
	image = pygame.transform.scale(image, size)
	return image