"""
Ce fichier gère les events custom pour le jeu
"""

import pygame

from ui import Zoom
from ui.components.main import ui_component_main_click
from ui.framework.draw import ui_framework_draw_updateHoverCursor

def events_handleEvents(event: pygame.event.Event):
	match event.type: # type: ignore
		case pygame.MOUSEWHEEL:
			if (event.y >= 0):
				Zoom.Zoom_decrement()
			else:
				Zoom.Zoom_increment()
		case pygame.MOUSEBUTTONUP:
			if (event.button == 1):
				ui_component_main_click(event.pos)
		case pygame.MOUSEMOTION:
			ui_framework_draw_updateHoverCursor(event.pos)
		# case _:
		# 	print(event)




	
	

	
 

 		
		
	
	
	

	


