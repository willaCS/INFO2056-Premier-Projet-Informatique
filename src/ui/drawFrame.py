"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

import Window

from globals import SelectedTile, all, gestionMenu, testing
import ui.components.settings
import ui.components.map
import ui.components.tech
import ui.components.topbar
import ui.components.sidemenu
import ui.components.welcome
from ui.utils.ui_array import menu_draw

# menu
# sidemenu -> info case menu construction
# tech tree
# affichage texture sur map

def drawFrame():
	
	match gestionMenu.menu:
		case gestionMenu.MENU_INTRO:
			ui.components.welcome.drawWelcome()
			
		case gestionMenu.MENU_REGLAGE:
			ui.components.settings.drawSettings()
			
		case gestionMenu.MENU_JEU:
			if SelectedTile.val:
				ui.components.sidemenu.showSideMenu()
			ui.components.map.drawMap()
			ui.components.topbar.showTopBar()
			# selectedbuilding = all.font.render(testing.activeBuilding()['name'], True, (255, 0, 0)) # type: ignore
			# Window.inst.blit(selectedbuilding, (Window.resolution[0] // 8, Window.resolution[0] // 10))
	menu_draw()
	
	
	






