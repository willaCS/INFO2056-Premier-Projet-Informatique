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
