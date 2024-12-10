import pygame

import Window

ui_framework_draw_hover_cursor = (0, 0)

def ui_framework_draw_updateHoverCursor(pos):
	global ui_framework_draw_hover_cursor
	ui_framework_draw_hover_cursor = pos

def ui_framework_draw_drawRect(rect, color, rounding = 0, outline = 0, hover = None):
	global ui_framework_draw_hover_cursor
	if hover is not None and pygame.Rect(rect).collidepoint(ui_framework_draw_hover_cursor):
		color = hover
	else:
		color = color
	pygame.draw.rect(Window.Window_inst, color, rect, outline, rounding)

def ui_framework_draw_drawCircle(center, radius, color, outline = 0):
	pygame.draw.circle(Window.Window_inst, color, center, radius, outline)