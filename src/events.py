import pygame

import globals.selectedTile
import globals.zoom

def handleEvents(event):
	match event.type:
		case pygame.MOUSEWHEEL:
			if (event.y >= 0):
				globals.zoom.decrement()
			else:
				globals.zoom.increment()
		case pygame.MOUSEBUTTONUP:
			if (event.button == 1):
				globals.selectedTile.select(event.pos)
		case _:
			pass
