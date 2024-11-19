"""
Ce fichier gère les events custom pour le jeu
"""

import pygame

from globals import SelectedTile, Zoom
from ui import drawMenu
from ui import drawFrame

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
				SelectedTile.select(event.pos)
				handleClickEventsMenu(event.pos)

		

		# case _:
		# 	print(event)


def isInRectangle(pos, rect):
	return pos[0] > rect[0][0] and pos[1] > rect[0][1]\
		and pos[0] <= rect[0][0] + rect[1][0] and pos[1] <= rect[0][1] + rect[1][1]

def handleClickEventsMenu(position):
	if isInRectangle(position, drawMenu.bouton_settings):
		gestionMenu.change_menu(gestionMenu.MENU_REGLAGE)

	if isInRectangle(position, drawMenu.bouton_jouer):
		gestionMenu.change_menu(gestionMenu.MENU_JEU)

 		
		
	
	
	

	


