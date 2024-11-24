import pygame

import Window

def drawRect(rect, color, rounding = 0, outline = 0):
	pygame.draw.rect(Window.inst, color, rect, outline, rounding)

def drawCircle(center, radius, color, outline = 0):
	pygame.draw.circle(Window.inst, color, center, radius, outline)