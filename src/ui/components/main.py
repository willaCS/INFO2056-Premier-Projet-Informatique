import Window
from ui.framework import component
from ui.framework.framework import component_click, component_draw, component_hide, component_show
from ui.components.map import map_component
from ui.components.placeBuildings import placeBuildingsMenu
from ui.components.settings import settingsMenu
from ui.components.sidemenu import sideMenu
from ui.components.stock import stockMenu
from ui.components.tech import techMenu
from ui.components.topbar import topBar
from ui.components.welcome import welcomeMenu

main_component = component(
	z=0,
	rect=lambda: (
		(0, 0),
		Window.resolution,
	),
	draw=lambda rect: None,
	childs=[
		map_component,
		placeBuildingsMenu,
		settingsMenu,
		sideMenu,
		stockMenu,
		techMenu,
		topBar,
		welcomeMenu,
	]
)

def draw():
	component_draw(main_component, Window.mouse_position)

def click(pos):
	component_click(main_component, pos)

def hide_all():
	for child in main_component['_childs']:
		component_hide(child)

hide_all()