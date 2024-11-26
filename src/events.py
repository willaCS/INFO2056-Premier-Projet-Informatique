"""
Ce fichier gère les events custom pour le jeu
"""

import pygame

from ui import Zoom
from ui.framework import menu_click
from ui.framework.draw import updateHoverCursor
from ui import gestionMenu

def handleEvents(event: pygame.event.Event):
	match event.type: # type: ignore
		case pygame.MOUSEWHEEL:
			if (event.y >= 0):
				Zoom.decrement()
			else:
				Zoom.increment()
		case pygame.MOUSEBUTTONUP:
			if (event.button == 1):
				menu_click(event.pos)
		case pygame.MOUSEMOTION:
			updateHoverCursor(event.pos)
		# case _:
		# 	print(event)




	
	

	
 

 		
		
	
	
	

	


