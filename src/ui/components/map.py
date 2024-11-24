import Window
from globals import SelectedTile
from ui.components.topbar import TOP_BAR_HEIGHT
from ui.framework import button_new, composant_new, composant_show
from ui.map.map import drawMap

map_component = composant_new(0, [
	# Map
	button_new(
		1,
		lambda: (
			(
				0,
				TOP_BAR_HEIGHT,
			),
			(
				Window.resolution[0],
				Window.resolution[1] - TOP_BAR_HEIGHT
			),
		),
		drawMap,
		lambda pos: SelectedTile.select(pos),
	),
])

def drawMapComponent():
	composant_show(map_component)
