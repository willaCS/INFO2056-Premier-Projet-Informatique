"""
Ce fichier permet d'afficher l'interface utilisateur.
"""

from typing import Tuple
from pygame import font
import pygame

import Window
from globals import Screenmode, Speed, all, SelectedTile, ui_game, player
from utils.mytyping import Color, coord_i
from ui import ui_array


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

def drawSquare(coord: coord_i, color: Color, text: str):
	pygame.draw.rect(Window.inst, color, ((coord[0] + padding_out, coord[1] + padding_out), (top_bar_height - 2 * padding_out, top_bar_height - 2 * padding_out)))
	text_prepared = all.font.render(text, True, (0, 0, 0))
	Window.inst.blit(text_prepared, (coord[0] + padding_out + 8, coord[1] + padding_out - 4))

def __drawSideMenu(rect):
	pygame.draw.rect(Window.inst, all.COLOR_WHITE, ((rect[0][0] + MENU_BORDER, rect[0][1] + MENU_BORDER), (rect[1][0] - 2 * MENU_BORDER, rect[1][1] - 2 * MENU_BORDER)))

def __drawExitButon(rect):
	global EXIT_BUTTON
	pygame.draw.rect(Window.inst, all.COLOR_RED, ((rect[0][0] + EXIT_BUTTON_BORDER, rect[0][1] + EXIT_BUTTON_BORDER), (rect[1][0] - 2 * EXIT_BUTTON_BORDER, rect[1][1] - 2 * EXIT_BUTTON_BORDER)))
	EXIT_BUTTON = resize_image(EXIT_BUTTON, (rect[1][0] - 2 * EXIT_BUTTON_BORDER, rect[1][1] - 2 * EXIT_BUTTON_BORDER))
	Window.inst.blit(EXIT_BUTTON, (rect[0][0] + EXIT_BUTTON_BORDER, rect[0][1] + EXIT_BUTTON_BORDER))

def test_exec():
	print("TEST")

def close_side_menu():
	ui_game.side_menu_present = False

def longNumber(number: int) -> str:
	if number < 1000:
		return str(number)
	elif number < 1000000:
		return str((number // 10) / 100) + "K"
	elif number < 1000000000:
		return str((number // 10000) / 100) + "M"
	elif number < 1000000000000:
		return str((number // 10000000) / 100) + "B"
	else:
		return str((number // 10000000000) / 100) + "T"

def drawUI():
	pygame.draw.rect(Window.inst, (40, 40, 40), ((0, 0), (Window.resolution[0], top_bar_height)))
	drawCoin((200, 0), 400, (255, 180, 0), player.money, player.money_incr)
	drawCoin((610, 0), 400, (0, 200, 200), player.science, player.science_incr)
	drawSquare((0, 0), all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_MAIN else (80, 80, 80), "A")
	drawSquare((50, 0), all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_ECONOMY_SUPPLY else (80, 80, 80), "B")
	drawSquare((100, 0), all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_ECONOMY_DEMAND else (80, 80, 80), "C")
	drawSquare((150, 0), all.COLOR_WHITE if Screenmode.val == Screenmode.SCREENMODE_TRANSPORT else (80, 80, 80), "D")

	drawSquare((Window.resolution[0] - 260, 0), (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 1 else (80, 80, 80), "1")
	drawSquare((Window.resolution[0] - 210, 0), (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 2 else (80, 80, 80), "2")
	drawSquare((Window.resolution[0] - 160, 0), (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 3 else (80, 80, 80), "3")
	drawSquare((Window.resolution[0] - 110, 0), (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 4 else (80, 80, 80), "4")
	drawSquare((Window.resolution[0] - 60,  0), (120, 0, 0) if Speed.val == 0 else all.COLOR_WHITE if Speed.val >= 5 else (80, 80, 80), "5")
	
	#ad
#                                                                     (niveau,((x, y), (longueur, hauteur))
	if SelectedTile.val:
		if not ui_game.side_menu_present:
			ui_game.side_menu_present = True
			ui_game.precedent_position = SelectedTile.val
			ui_game.selected_sideMenu_id = ui_array.append_array(1, ((0, top_bar_height), (470, Window.resolution[1] - top_bar_height)), __drawSideMenu, test_exec)
			ui_game.exit_button_sideMenu_id = ui_array.append_array(2, ((425, top_bar_height + MENU_BORDER), (30, 30)), __drawExitButon, close_side_menu)
		elif ui_game.precedent_position != SelectedTile.val:
			ui_game.side_menu_present = False
			ui_array.remove_array(ui_array.find(ui_game.selected_sideMenu_id))
			ui_array.remove_array(ui_array.find(ui_game.exit_button_sideMenu_id))
		if ui_game.side_menu_present:
			ui_array.draw_all_rect()

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