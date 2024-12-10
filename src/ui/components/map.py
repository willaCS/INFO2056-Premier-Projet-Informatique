import Window
from ui import SelectedTile
from ui import visual_config as vc
from ui.framework.framework import ui_framework_framework_component, ui_framework_framework_component_show
from ui.map.map import ui_map_map_drawMap

ui_component_map_map_component = ui_framework_framework_component(
	z=1,
	rect=lambda: (
		(
			0,
			vc.VC_TOP_BAR_HEIGHT,
		),
		(
			Window.Window_resolution[0],
			Window.Window_resolution[1] - vc.VC_TOP_BAR_HEIGHT
		),
	),
	draw=ui_map_map_drawMap,
	click=lambda pos: SelectedTile.SelectedTile_select(pos),
)

def ui_component_map_drawMapComponent():
	ui_framework_framework_component_show(ui_component_map_map_component)
