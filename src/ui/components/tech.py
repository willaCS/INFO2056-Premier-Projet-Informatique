import Window
from model.industry.technologiesTree import model_technologyTree_get_tech_for_draw, model_technologyTree_add_tech
from ui import visual_config as vc
from ui.common.buttons import ui_common_centerTextButton, ui_common_exit_button
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.framework import ui_framework_framework_component, ui_framework_framework_component_show, ui_framework_framework_component_hide
from ui.framework.text import ui_framework_text_drawText
from ui.map.industry import ui_map_industry_print_industry

ui_component_tech_tech_selected = None

ui_component_tech_NB_TECH_BRANCH = 5
ui_component_tech_TECH_PER_BRANCH = 3

ui_component_tech_TECH_MENU_SIZE = (500, 300)

ui_component_tech_HEADER_HEIGHT=75
ui_component_tech_TECH_HEIGHT=75
ui_component_tech_TECH_COST_WIDTH=150

def ui_component_tech_closeTech(pos):
	ui_framework_framework_component_hide(ui_component_tech_techMenu)

def ui_component_tech__selectTech(i, j):
	global ui_component_tech_tech_selected
	ui_component_tech_tech_selected = (i, j)



def ui_component_tech__drawTech(rect, i, j):
	global ui_component_tech_tech_selected
	tech = model_technologyTree_get_tech_for_draw(i, j)
	color = vc.VC_PRIMARY if ui_component_tech_tech_selected == (i, j) else vc.VC_SECONDARY if tech['unlocked'] else vc.VC_BACKGROUND3
	ui_common_centerTextButton(rect, 'font2', tech['name'], color, vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT if not ui_component_tech_tech_selected == (i, j) else None)

def ui_component_tech__drawTechInfo(rect):
	ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND3, vc.VC_ROUNDING_HARD)
	if ui_component_tech_tech_selected is None:
		return
	tech = model_technologyTree_get_tech_for_draw(ui_component_tech_tech_selected[0], ui_component_tech_tech_selected[1])
	for i in range(len(tech['unlocks'])):
		message = "Unlocks {}".format(ui_map_industry_print_industry(tech['unlocks'][i]))
		ui_framework_text_drawText('font2', (rect[0][0] + vc.VC_PADDING + vc.VC_MENU_BORDER_WIDTH, rect[0][1] + vc.VC_PADDING + vc.VC_MENU_BORDER_WIDTH + 30 * i), message, vc.VC_TEXT)

ui_component_tech_techMenu = ui_framework_framework_component(
	z=10,
	padding=vc.VC_PADDING + vc.VC_MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(
			parent[1][0] // 2 - ui_component_tech_TECH_MENU_SIZE[0],
			parent[1][1] // 2 - ui_component_tech_TECH_MENU_SIZE[1]
		),
		(
			ui_component_tech_TECH_MENU_SIZE[0] * 2,
			ui_component_tech_TECH_MENU_SIZE[1] * 2
		),
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND2, vc.VC_ROUNDING_HARD) or\
					  ui_framework_draw_drawRect(rect, vc.VC_PRIMARY, vc.VC_ROUNDING_HARD, vc.VC_MENU_BORDER_WIDTH),
	click=lambda pos: print('xd'),
	clickOutside=lambda pos: ui_framework_framework_component_hide(ui_component_tech_techMenu),
	childs=[
		# Header
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(0, 0),
				(
					parent[1][0] - ui_component_tech_HEADER_HEIGHT - vc.VC_PADDING,
					ui_component_tech_HEADER_HEIGHT,
				)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', 'Technologies', vc.VC_BACKGROUND3, vc.VC_ROUNDING_HARD),
			click=lambda pos: None,
		),

		# Close button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - ui_component_tech_HEADER_HEIGHT, 0),
				(ui_component_tech_HEADER_HEIGHT, ui_component_tech_HEADER_HEIGHT)
			),
			draw=ui_common_exit_button,
			click=ui_component_tech_closeTech,
		),

		# Techs
		*[(ui_framework_framework_component(
			z=2,
			rect=lambda parent, x=x, y=y: (
				(
					(((parent[1][0] - ui_component_tech_NB_TECH_BRANCH * vc.VC_PADDING) // ui_component_tech_NB_TECH_BRANCH) + vc.VC_PADDING) * x,
					(ui_component_tech_TECH_HEIGHT + vc.VC_PADDING) * y + ui_component_tech_HEADER_HEIGHT + vc.VC_PADDING,
				),
				(
					((parent[1][0] - ui_component_tech_NB_TECH_BRANCH * vc.VC_PADDING) // ui_component_tech_NB_TECH_BRANCH),
					ui_component_tech_TECH_HEIGHT
				),
			),
			draw=lambda rect, is_in, x=x, y=y: ui_component_tech__drawTech(rect, x, y),
			click=lambda pos, x=x, y=y: ui_component_tech__selectTech(x, y),
		)) for x in range(ui_component_tech_NB_TECH_BRANCH) for y in range(ui_component_tech_TECH_PER_BRANCH)],

		# Selected Tech Info
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(
					0,
					(ui_component_tech_TECH_HEIGHT + vc.VC_PADDING) * ui_component_tech_TECH_PER_BRANCH + ui_component_tech_HEADER_HEIGHT + vc.VC_PADDING,
				),
				(
					parent[1][0] - ui_component_tech_TECH_COST_WIDTH - vc.VC_PADDING,
					parent[1][1] - (ui_component_tech_TECH_HEIGHT + vc.VC_PADDING) * (ui_component_tech_TECH_PER_BRANCH) - (ui_component_tech_HEADER_HEIGHT + vc.VC_PADDING),
				),
			),
			draw=ui_component_tech__drawTechInfo,
			click=lambda pos: None,
		),

		# Add Tech Cost
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(
					parent[1][0] - ui_component_tech_TECH_COST_WIDTH,
					(ui_component_tech_TECH_HEIGHT + vc.VC_PADDING) * ui_component_tech_TECH_PER_BRANCH + ui_component_tech_HEADER_HEIGHT + vc.VC_PADDING,
				),
				(
					ui_component_tech_TECH_COST_WIDTH,
					parent[1][1] - (ui_component_tech_TECH_HEIGHT + vc.VC_PADDING) * (ui_component_tech_TECH_PER_BRANCH) - (ui_component_tech_HEADER_HEIGHT + vc.VC_PADDING) - (ui_component_tech_TECH_COST_WIDTH + vc.VC_PADDING),
				),
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 
				'font2', "{}".format(model_technologyTree_get_tech_for_draw(ui_component_tech_tech_selected[0], ui_component_tech_tech_selected[1])['cost']) if ui_component_tech_tech_selected else "",
				vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH
			),
			click=lambda pos: None,
		),

		# Add Tech Button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(
					parent[1][0] - ui_component_tech_TECH_COST_WIDTH,
					parent[1][1] - ui_component_tech_TECH_COST_WIDTH,
				),
				(ui_component_tech_TECH_COST_WIDTH, ui_component_tech_TECH_COST_WIDTH),
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "Add", vc.VC_BACKGROUND3, vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT),
			click=lambda pos: model_technologyTree_add_tech(ui_component_tech_tech_selected[0], ui_component_tech_tech_selected[1]),
		),
	]
)

def ui_component_tech_drawTech():
	ui_framework_framework_component_show(ui_component_tech_techMenu)
