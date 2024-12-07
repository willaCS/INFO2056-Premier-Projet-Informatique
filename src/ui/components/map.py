import Window
from ui import SelectedTile
from ui import visual_config as vc
from ui.framework import component, component_show
from ui.map.map import drawMap

map_component = component(
	z=1,
	rect=lambda: (
		(
			0,
			vc.TOP_BAR_HEIGHT,
		),
		(
			Window.resolution[0],
			Window.resolution[1] - vc.TOP_BAR_HEIGHT
		),
	),
	draw=drawMap,
	click=lambda pos: SelectedTile.select(pos),
)

def drawMapComponent():
	component_show(map_component)
