"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

import Window

from ui.drawMap import drawMap
from globals import all, testing, gestionMenu
from ui.drawUI import drawUI
import pygame
import ui.drawMenu
ORANGE    = (255, 165,   0)
Corn_Flower_Blue = (100,149,237)





def drawFrame():
	
	match gestionMenu.menu:
		case gestionMenu.MENU_INTRO:
			message = all.font2.render("The Capitalism Island 2", True, ORANGE)
			messageLargeur, messageHauteur = all.font2.size("The Capitalism Island 2")
			Window.inst.fill(Corn_Flower_Blue)
			Window.inst.blit(message, ((Window.resolution[0] - messageLargeur)//2, (Window.resolution[1] - messageHauteur)// 2))
			ui.drawMenu.bouton_reglage()
			ui.drawMenu.bouton_play()
			


			
		case gestionMenu.MENU_REGLAGE:
			pass
			
		case gestionMenu.MENU_JEU:
			drawMap()
			drawUI()
			selectedbuilding = all.font.render(testing.activeBuilding()['name'], True, (255, 0, 0)) # type: ignore
			Window.inst.blit(selectedbuilding, (Window.resolution[0] // 8, Window.resolution[0] // 10))
	
	
	






