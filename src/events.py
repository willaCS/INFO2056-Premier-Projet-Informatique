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


def isInRectangle(pos, rect):
	return pos[0] > rect[0][0] and pos[1] > rect[0][1]\
		and pos[0] <= rect[0][0] + rect[1][0] and pos[1] <= rect[0][1] + rect[1][1]

def handleClickEventsMenu(position):
	if isInRectangle(position, drawMenu.bouton_settings):
		gestionMenu.change_menu(gestionMenu.MENU_REGLAGE)

	if isInRectangle(position, drawMenu.bouton_jouer):
		gestionMenu.change_menu(gestionMenu.MENU_JEU)
	
	if isInRectangle(position, drawSettings.bouton_back):
		gestionMenu.change_menu(gestionMenu.MENU_INTRO)
	
	if isInRectangle(position, drawSettings.bouton_azerty):
		gestionClavier.change_clavier(gestionClavier.CLAVIER_AZERTY)


	
	

	
 

 		
		
	
	
	

	


