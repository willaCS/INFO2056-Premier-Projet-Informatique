import pygame
import Window
from pygame import font

FONT1_SIZE = 40
font1: font.Font = None # type: ignore

FONT2_SIZE = 24
font2: font.Font = None # type: ignore

def setup():
	global font1, font2

	font1 = font.SysFont('monospace', 40)
	font2 = font.SysFont('monospace', 24, True)

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

# anchor can be one of the following:
# topleft, bottomleft, topright, bottomright
# midtop, midleft, midbottom, midright
# center, centerx, centery
def drawText(
	font: font.Font,
	coord,
	text: str,
	color,
	anchor: str = "topleft"
):
	text_prepared = font.render(text, True, color)
	rect = text_prepared.get_rect()
	setattr(rect, anchor, coord)
	Window.inst.blit(text_prepared, rect)
