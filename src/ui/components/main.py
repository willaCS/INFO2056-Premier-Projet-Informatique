import utils.Window as Window
from ui.framework.framework import Component
from ui.components.map import map_component
from ui.components.placeBuildings import placeBuildingsMenu
from ui.components.settings import settingsMenu
from ui.components.sidemenu import sideMenu
from ui.components.stock import stockMenu
from ui.components.tech import techMenu
from ui.components.topbar import topBar
from ui.components.welcome import welcomeMenu

main_component = Component(
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
	main_component.draw(Window.mouse_position)

def click(pos):
	main_component.click(pos)

def hide_all():
	for child in main_component._childs:
		child.hide()

hide_all()