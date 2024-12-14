from utils.Components import Component
from ui.components.map import map_component
from ui.components.placeBuildings import placeBuildingsMenu
from ui.components.settings import settingsMenu
from ui.components.sidemenu import sideMenu
from ui.components.stock import stockMenu
from ui.components.tech import techMenu
from ui.components.topbar import topBar
from ui.components.welcome import welcomeMenu
from utils.Window import Window

main_component = Component(
	z=0,
	rect=lambda: (
		(0, 0),
		(800, 800),
	),
	draw=lambda: None,
	childs=[
		map_component,
		placeBuildingsMenu,
		settingsMenu,
		sideMenu,
		stockMenu,
		techMenu,
		topBar,
		welcomeMenu,
	],
	arguments={'window': None}
)

def draw(window: Window):
	main_component.draw(window.mouse_position)

def click(window: Window):
	main_component.click(window.mouse_position)

def hide_all():
	for child in main_component._childs:
		child.hide()

hide_all()