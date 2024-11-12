"""
Ce fichier permet d'afficher l'interface utilisateur.
"""

from typing import Tuple
from pygame import font
import pygame

import Window
from globals import Screenmode, Speed, all, SelectedTile, ui_game
from utils.mytyping import Color, coord_i

top_bar_height = 60
padding_out = 10
padding_in = 2

def getFont() -> font.Font:
	return font.SysFont('monospace', top_bar_height - 2 * padding_out)

def drawCoin(coord: Tuple[int, int], len: int, color: Color, number: int, incr: int):
	pygame.draw.rect(Window.inst, (255, 255, 255), ((coord[0] + padding_out, coord[1] + padding_out), (len, top_bar_height - 2 * padding_out)))
	pygame.draw.circle(Window.inst, color,
		(coord[0] + top_bar_height / 2, coord[1] + top_bar_height / 2),
		top_bar_height / 2 - padding_out - padding_in
	)
	text = str(number) + "(+" + str(incr) + ")"
	text_prepared = all.font.render(text, True, (0, 0, 0))
	Window.inst.blit(text_prepared, (coord[0] + top_bar_height, coord[1] + padding_out - 4))

def drawSquare(coord: Tuple[int, int], color: Color, text: str):
	pygame.draw.rect(Window.inst, color, ((coord[0] + padding_out, coord[1] + padding_out), (top_bar_height - 2 * padding_out, top_bar_height - 2 * padding_out)))
	text_prepared = all.font.render(text, True, (0, 0, 0))
	Window.inst.blit(text_prepared, (coord[0] + padding_out + 8, coord[1] + padding_out - 4))

def drawUI():
	pygame.draw.rect(Window.inst, (40, 40, 40), ((0, 0), (Window.resolution[0], top_bar_height)))
	drawCoin((200, 0), 200, (255, 180, 0), 25, 1)
	drawCoin((410, 0), 200, (0, 200, 200), 11, 3)
	drawSquare((0, 0), (255, 255, 255) if Screenmode.val == Screenmode.SCREENMODE_MAIN else (80, 80, 80), "A")
	drawSquare((50, 0), (255, 255, 255) if Screenmode.val == Screenmode.SCREENMODE_ECONOMY_SUPPLY else (80, 80, 80), "B")
	drawSquare((100, 0), (255, 255, 255) if Screenmode.val == Screenmode.SCREENMODE_ECONOMY_DEMAND else (80, 80, 80), "C")
	drawSquare((150, 0), (255, 255, 255) if Screenmode.val == Screenmode.SCREENMODE_TRANSPORT else (80, 80, 80), "D")

	drawSquare((Window.resolution[0] - 260, 0), (120, 0, 0) if Speed.val == 0 else (255, 255, 255) if Speed.val >= 1 else (80, 80, 80), "1")
	drawSquare((Window.resolution[0] - 210, 0), (120, 0, 0) if Speed.val == 0 else (255, 255, 255) if Speed.val >= 2 else (80, 80, 80), "2")
	drawSquare((Window.resolution[0] - 160, 0), (120, 0, 0) if Speed.val == 0 else (255, 255, 255) if Speed.val >= 3 else (80, 80, 80), "3")
	drawSquare((Window.resolution[0] - 110, 0), (120, 0, 0) if Speed.val == 0 else (255, 255, 255) if Speed.val >= 4 else (80, 80, 80), "4")
	drawSquare((Window.resolution[0] - 60,  0), (120, 0, 0) if Speed.val == 0 else (255, 255, 255) if Speed.val >= 5 else (80, 80, 80), "5")
	
	#ad
	if SelectedTile.val:
		if not ui_game.side_menu_present:
			ui_game.side_menu_present = True
			ui_game.precedent_position = SelectedTile.val
		elif ui_game.precedent_position != SelectedTile.val:
			ui_game.side_menu_present = False
		if ui_game.side_menu_present:
			__drawSideMenu()

#ad

def __drawSideMenu():
	pygame.draw.rect(Window.inst, all.COLOR_WHITE, ((10, top_bar_height + Window.resolution[1] / 100), (450, Window.resolution[1] - top_bar_height - 16)))
	pygame.draw.rect(Window.inst, all.COLOR_BLACK, ((425, top_bar_height + Window.resolution[1] / 100 + 5), (30,30)))
	Window.inst.blit(EXIT_BUTTON, (425, top_bar_height + Window.resolution[1] / 100 + 5))
	
def setup_image():
	global EXIT_BUTTON
	EXIT_BUTTON = pygame.image.load('/home/adriencormann/university/INFO2056-Premier-Projet-Informatique/assets/close_button.png').convert_alpha(Window.inst)
	EXIT_BUTTON = pygame.transform.scale(EXIT_BUTTON, (30, 30))