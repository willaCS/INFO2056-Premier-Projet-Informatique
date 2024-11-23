import pygame

import Window

def drawRect(rect, color):
	pygame.draw.rect(Window.inst, color, rect)