"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

import utils.Window as Window
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
from ui.framework.text import drawText

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
				# ui.components.placeBuildings.showplaceBuildingsMenu()
			ui.components.map.drawMapComponent()
			ui.components.topbar.showTopBar()
	draw()





