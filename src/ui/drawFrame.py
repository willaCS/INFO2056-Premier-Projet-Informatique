"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

import Window

from globals import all, gestionMenu, testing
from ui.drawUI import drawUI
import ui.components.map
import ui.components.tech
import ui.components.topbar
import ui.components.sidemenu
import ui.drawMenu
import ui.drawSettings
from ui.utils.ui_array import menu_draw

# menu
# sidemenu -> info case menu construction
# tech tree
# affichage texture sur map

def drawFrame():
	
	match gestionMenu.menu:
		case gestionMenu.MENU_INTRO:
			message = all.font2.render("The Capitalism Island 2", True, all.COLOR_ORANGE)
			messageLargeur, messageHauteur = all.font2.size("The Capitalism Island 2")
			Window.inst.fill(all.COLOR_CORN_FLOWER_BLUE)
			Window.inst.blit(message, ((Window.resolution[0] - messageLargeur)//2, (Window.resolution[1] - messageHauteur)// 2))
			ui.drawMenu.bouton_reglage()
			ui.drawMenu.bouton_play()
			
		case gestionMenu.MENU_REGLAGE:
			message = all.font2.render("The Capitalism Island 2", True, all.COLOR_ORANGE)
			messageLargeur, messageHauteur = all.font2.size("The Capitalism Island 2")
			Window.inst.fill(all.COLOR_CORN_FLOWER_BLUE)
			Window.inst.blit(message, ((Window.resolution[0] - messageLargeur)//2, (Window.resolution[1] - messageHauteur)// 2))
			ui.drawSettings.bouton_retour()
			ui.drawSettings.gestion_settings()
			
		case gestionMenu.MENU_JEU:
			ui.components.map.drawMap()
			ui.components.topbar.showTopBar()
			menu_draw()
			drawUI()
			# selectedbuilding = all.font.render(testing.activeBuilding()['name'], True, (255, 0, 0)) # type: ignore
			# Window.inst.blit(selectedbuilding, (Window.resolution[0] // 8, Window.resolution[0] // 10))
	
	
	






