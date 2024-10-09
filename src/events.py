"""
Ce fichier gère les events custom pour le jeu
"""

import pygame

from globals import selectedTile, zoom

def handleEvents(event):
	match event.type:
		case pygame.MOUSEWHEEL:
			if (event.y >= 0):
				zoom.decrement()
			else:
				zoom.increment()
		case pygame.MOUSEBUTTONUP:
			if (event.button == 1):
				selectedTile.select(event.pos)
		case _:
			pass
