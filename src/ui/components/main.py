import Window
from ui.framework.framework import ui_framework_framework_component_click, ui_framework_framework_component_draw, ui_framework_framework_component_hide, ui_framework_framework_component_show, ui_framework_framework_component
from ui.components.map import ui_component_map_map_component
from ui.components.placeBuildings import ui_component_placeBuilding_placeBuildingsMenu
from ui.components.settings import ui_component_settings_settingsMenu
from ui.components.sidemenu import sideMenu
from ui.components.stock import ui_component_stock_stockMenu
from ui.components.tech import ui_component_tech_techMenu
from ui.components.topbar import ui_component_tobpar_topBar
from ui.components.welcome import ui_component_welcome_welcomeMenu

ui_component_main_main_component = ui_framework_framework_component(
	z=0,
	rect=lambda: (
		(0, 0),
		Window.Window_resolution,
	),
	draw=lambda rect: None,
	childs=[
		ui_component_map_map_component,
		ui_component_placeBuilding_placeBuildingsMenu,
		ui_component_settings_settingsMenu,
		sideMenu,
		ui_component_stock_stockMenu,
		ui_component_tech_techMenu,
		ui_component_tobpar_topBar,
		ui_component_welcome_welcomeMenu,
	]
)

def ui_component_main_draw():
	ui_framework_framework_component_draw(ui_component_main_main_component, Window.Window_mouse_position)

def ui_component_main_click(pos):
	ui_framework_framework_component_click(ui_component_main_main_component, pos)

def ui_component_main_hide_all():
	for child in ui_component_main_main_component['_childs']:
		ui_framework_framework_component_hide(child)

ui_component_main_hide_all()