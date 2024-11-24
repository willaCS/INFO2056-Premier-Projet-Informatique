"""
Ce fichier gère les events custom pour le jeu
"""

import pygame

from globals import SelectedTile, Zoom, gestionMenu
from ui.utils import ui_array

from globals import gestionMenu

def handleEvents(event: pygame.event.Event):
	match event.type: # type: ignore
		case pygame.MOUSEWHEEL:
			if (event.y >= 0):
				Zoom.decrement()
			else:
				Zoom.increment()
		case pygame.MOUSEBUTTONUP:
			if (event.button == 1):
				ui_array.menu_click(event.pos)
		# case _:
		# 	print(event)
