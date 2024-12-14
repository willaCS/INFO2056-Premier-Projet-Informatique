"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

from ui import SelectedTile
from ui.components.main import draw
import ui.components.placeBuildings
import ui.components.settings
import ui.components.map
import ui.components.tech
import ui.components.topbar
import ui.components.sidemenu
import ui.components.welcome
from ui import gestionMenu

def drawFrame(window):
	match gestionMenu.menu:
		case gestionMenu.MENU_INTRO:
			ui.components.welcome.drawWelcome()
			
		case gestionMenu.MENU_REGLAGE:
			ui.components.settings.drawSettings()
			
		case gestionMenu.MENU_JEU:
			if SelectedTile.val:
				ui.components.sidemenu.showSideMenu()
				# ui.components.placeBuildings.showplaceBuildingsMenu()
			ui.components.map.drawMapComponent()
			ui.components.topbar.showTopBar()
	draw(window)





