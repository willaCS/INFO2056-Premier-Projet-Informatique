"""
Ce fichier gère les events custom pour le jeu
"""

import pygame

from globals import SelectedTile, Zoom, gestionMenu
from ui import drawMenu
from ui import ui_array

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
				if not ui_array.menu.click(event.pos):
					match gestionMenu.menu:
						case gestionMenu.MENU_INTRO:
							handleClickEventsMenu(event.pos)
						case gestionMenu.MENU_REGLAGE:
							pass
						case gestionMenu.MENU_JEU:
							SelectedTile.select(event.pos)
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

 		
		
	
	
	

	


