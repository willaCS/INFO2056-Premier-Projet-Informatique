"""
Ce fichier permet d'afficher l'interface utilisateur.
"""

from typing import Tuple
import pygame

import window
import globals.speed
import globals.all
import globals.screenmode

top_bar_height = 60
padding_out = 10
padding_in = 2

def getFont():
	return pygame.font.SysFont('monospace', top_bar_height - 2 * padding_out)

def drawCoin(coord: Tuple[int, int], len: int, color, number, incr):
	pygame.draw.rect(window.inst, (255, 255, 255), ((coord[0] + padding_out, coord[1] + padding_out), (len, top_bar_height - 2 * padding_out)))
	pygame.draw.circle(window.inst, color,
		(coord[0] + top_bar_height / 2, coord[1] + top_bar_height / 2),
		top_bar_height / 2 - padding_out - padding_in
	)
	text = str(number) + "(+" + str(incr) + ")"
	text_prepared = globals.all.font.render(text, True, (0, 0, 0))
	window.inst.blit(text_prepared, (coord[0] + top_bar_height, coord[1] + padding_out - 4))

def drawSquare(coord: Tuple[int, int], color, text):
	pygame.draw.rect(window.inst, color, ((coord[0] + padding_out, coord[1] + padding_out), (top_bar_height - 2 * padding_out, top_bar_height - 2 * padding_out)))
	text_prepared = globals.all.font.render(text, True, (0, 0, 0))
	window.inst.blit(text_prepared, (coord[0] + padding_out + 8, coord[1] + padding_out - 4))

def drawUI():
	pygame.draw.rect(window.inst, (40, 40, 40), ((0, 0), (window.resolution[0], top_bar_height)))
	drawCoin((200, 0), 200, (255, 180, 0), 25, 1)
	drawCoin((410, 0), 200, (0, 200, 200), 11, 3)
	drawSquare((0, 0), (255, 255, 255) if globals.screenmode.val == globals.screenmode.SCREENMODE_MAIN else (80, 80, 80), "A")
	drawSquare((50, 0), (255, 255, 255) if globals.screenmode.val == globals.screenmode.SCREENMODE_ECONOMY_SUPPLY else (80, 80, 80), "B")
	drawSquare((100, 0), (255, 255, 255) if globals.screenmode.val == globals.screenmode.SCREENMODE_ECONOMY_DEMAND else (80, 80, 80), "C")
	drawSquare((150, 0), (255, 255, 255) if globals.screenmode.val == globals.screenmode.SCREENMODE_TRANSPORT else (80, 80, 80), "D")

	drawSquare((window.resolution[0] - 260, 0), (120, 0, 0) if globals.speed.val == 0 else (255, 255, 255) if globals.speed.val >= 1 else (80, 80, 80), "1")
	drawSquare((window.resolution[0] - 210, 0), (120, 0, 0) if globals.speed.val == 0 else (255, 255, 255) if globals.speed.val >= 2 else (80, 80, 80), "2")
	drawSquare((window.resolution[0] - 160, 0), (120, 0, 0) if globals.speed.val == 0 else (255, 255, 255) if globals.speed.val >= 3 else (80, 80, 80), "3")
	drawSquare((window.resolution[0] - 110, 0), (120, 0, 0) if globals.speed.val == 0 else (255, 255, 255) if globals.speed.val >= 4 else (80, 80, 80), "4")
	drawSquare((window.resolution[0] - 60,  0), (120, 0, 0) if globals.speed.val == 0 else (255, 255, 255) if globals.speed.val >= 5 else (80, 80, 80), "5")
