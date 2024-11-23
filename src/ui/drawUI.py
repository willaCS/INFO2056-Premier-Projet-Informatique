"""
Ce fichier permet d'afficher l'interface utilisateur.
"""

import pygame

import Window
from globals import all, SelectedTile, player
from ui.components.sidemenu import showSideMenu
from utils.mytyping import Color, coord_i
from utils.draw import longNumber

top_bar_height = 60
padding_out = 10
padding_in = 2

def getFont() -> pygame.font.Font:
	all.font = pygame.font.SysFont('monospace', top_bar_height - 2 * padding_out)
	all.font2 = pygame.font.SysFont('monospace', 24, True)

def drawText(font: pygame.font.Font, coord: coord_i, text: str, color: Color, anchor: str = "topleft"):
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

def drawModeButton(rect, text, color):
	pygame.draw.rect(Window.inst, color, rect)
	text_prepared = all.font.render(text, True, (0, 0, 0))
	Window.inst.blit(text_prepared, (rect[0][0] + 9, rect[0][1] - 3))


def drawUI():
	if SelectedTile.val:
		showSideMenu()
	
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