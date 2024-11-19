"""
Ce fichier gère les events custom pour le jeu
"""

import pygame

from globals import SelectedTile, Zoom
from ui import ui_array

def handleEvents(event: pygame.event.Event):
	match event.type: # type: ignore
		case pygame.MOUSEWHEEL:
			if (event.y >= 0):
				Zoom.decrement()
			else:
				Zoom.increment()
		case pygame.MOUSEBUTTONUP:
			if (event.button == 1):
				SelectedTile.select(event.pos)
				ui_array.exec_click(event.pos)
		# case _:
		# 	print(event)
