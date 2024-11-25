import pygame

import Window

hover_cursor = (0, 0)

def updateHoverCursor(pos):
	global hover_cursor
	hover_cursor = pos

def drawRect(rect, color, rounding = 0, outline = 0, hover = None):
	global hover_cursor
	if hover is not None and pygame.Rect(rect).collidepoint(hover_cursor):
		color = hover
	else:
		color = color
	pygame.draw.rect(Window.inst, color, rect, outline, rounding)

def drawCircle(center, radius, color, outline = 0):
	pygame.draw.circle(Window.inst, color, center, radius, outline)