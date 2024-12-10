"""
Ce fichier gère la fonction drawFrame appelée chaque tick
"""

from ui import SelectedTile
from ui.components.main import ui_component_main_draw
import ui.components.placeBuildings
import ui.components.settings
import ui.components.map
import ui.components.tech
import ui.components.topbar
import ui.components.sidemenu
import ui.components.welcome
from ui import gestionMenu

# menu
# sidemenu -> info case menu construction
# tech tree
# affichage texture sur map

def ui_drawFrame_drawFrame():
	match gestionMenu.menu:
		case gestionMenu.GestionMenu_MENU_INTRO:
			ui.components.welcome.ui_component_welcome_drawWelcome()
			
		case gestionMenu.GestionMenu_MENU_REGLAGE:
			ui.components.settings.ui_component_settings_drawSettings()
			
		case gestionMenu.GestionMenu_MENU_JEU:
			if SelectedTile.SelectedTile_val:
				ui.components.sidemenu.showSideMenu()
				# ui.components.placeBuildings.showplaceBuildingsMenu()
			ui.components.map.ui_component_map_drawMapComponent()
			ui.components.topbar.ui_component_tobpar_showTopBar()
	ui_component_main_draw()





