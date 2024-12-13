import utils.Window as Window
from utils.Components import Component
from ui import SelectedTile
from ui import visual_config as vc
from ui.map.map import drawMap

map_component = Component(
	z=1,
	rect=lambda window: (
		(
			0,
			vc.TOP_BAR_HEIGHT,
		),
		(
			window.resolution[0],
			window.resolution[1] - vc.TOP_BAR_HEIGHT
		),
	),
	draw=drawMap,
	click=lambda pos: SelectedTile.select(pos),
)

def drawMapComponent():
	map_component.show()
