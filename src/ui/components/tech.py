from model.industry.technologiesTree import get_tech_for_draw, add_tech
from ui.framework.framework import Component
from ui import visual_config as vc
from ui.common.buttons import centerTextButton, exit_button
from ui.framework import drawRect, drawText
from ui.map.industry import print_industry

tech_selected = None

NB_TECH_BRANCH = 5
TECH_PER_BRANCH = 3

TECH_MENU_SIZE = (500, 300)

HEADER_HEIGHT=75
TECH_HEIGHT=75
TECH_COST_WIDTH=150

def closeTech(pos):
	techMenu.hide()

def _selectTech(i, j):
	global tech_selected
	tech_selected = (i, j)



def _drawTech(rect, i, j):
	global tech_selected
	tech = get_tech_for_draw(i, j)
	color = vc.PRIMARY if tech_selected == (i, j) else vc.SECONDARY if tech['unlocked'] else vc.BACKGROUND3
	centerTextButton(rect, 'font2', tech['name'], color, vc.ROUNDING_SMOOTH, vc.ACCENT if not tech_selected == (i, j) else None)

def _drawTechInfo(rect):
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD)
	if tech_selected is None:
		return
	tech = get_tech_for_draw(tech_selected[0], tech_selected[1])
	for i in range(len(tech['unlocks'])):
		message = "Unlocks {}".format(print_industry(tech['unlocks'][i]))
		drawText('font2', (rect[0][0] + vc.PADDING + vc.MENU_BORDER_WIDTH, rect[0][1] + vc.PADDING + vc.MENU_BORDER_WIDTH + 30 * i), message, vc.TEXT)

techMenu = Component(
	z=10,
	padding=vc.PADDING + vc.MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(
			parent[1][0] // 2 - TECH_MENU_SIZE[0],
			parent[1][1] // 2 - TECH_MENU_SIZE[1]
		),
		(
			TECH_MENU_SIZE[0] * 2,
			TECH_MENU_SIZE[1] * 2
		),
	),
	draw=lambda rect: drawRect(rect, vc.BACKGROUND2, vc.ROUNDING_HARD) or\
					  drawRect(rect, vc.PRIMARY, vc.ROUNDING_HARD, vc.MENU_BORDER_WIDTH),
	click=lambda pos: print('xd'),
	clickOutside=lambda pos: techMenu.hide(),
	childs=[
		# Header
		Component(
			z=2,
			rect=lambda parent: (
				(0, 0),
				(
					parent[1][0] - HEADER_HEIGHT - vc.PADDING,
					HEADER_HEIGHT,
				)
			),
			draw=lambda rect: centerTextButton(rect, 'font2', 'Technologies', vc.BACKGROUND3, vc.ROUNDING_HARD),
			click=lambda pos: None,
		),

		# Close button
		Component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - HEADER_HEIGHT, 0),
				(HEADER_HEIGHT, HEADER_HEIGHT)
			),
			draw=exit_button,
			click=closeTech,
		),

		# Techs
		*[(Component(
			z=2,
			rect=lambda parent, x=x, y=y: (
				(
					(((parent[1][0] - NB_TECH_BRANCH * vc.PADDING) // NB_TECH_BRANCH) + vc.PADDING) * x,
					(TECH_HEIGHT + vc.PADDING) * y + HEADER_HEIGHT + vc.PADDING,
				),
				(
					((parent[1][0] - NB_TECH_BRANCH * vc.PADDING) // NB_TECH_BRANCH),
					TECH_HEIGHT
				),
			),
			draw=lambda rect, is_in, x=x, y=y: _drawTech(rect, x, y),
			click=lambda pos, x=x, y=y: _selectTech(x, y),
		)) for x in range(NB_TECH_BRANCH) for y in range(TECH_PER_BRANCH)],

		# Selected Tech Info
		Component(
			z=2,
			rect=lambda parent: (
				(
					0,
					(TECH_HEIGHT + vc.PADDING) * TECH_PER_BRANCH + HEADER_HEIGHT + vc.PADDING,
				),
				(
					parent[1][0] - TECH_COST_WIDTH - vc.PADDING,
					parent[1][1] - (TECH_HEIGHT + vc.PADDING) * (TECH_PER_BRANCH) - (HEADER_HEIGHT + vc.PADDING),
				),
			),
			draw=_drawTechInfo,
			click=lambda pos: None,
		),

		# Add Tech Cost
		Component(
			z=2,
			rect=lambda parent: (
				(
					parent[1][0] - TECH_COST_WIDTH,
					(TECH_HEIGHT + vc.PADDING) * TECH_PER_BRANCH + HEADER_HEIGHT + vc.PADDING,
				),
				(
					TECH_COST_WIDTH,
					parent[1][1] - (TECH_HEIGHT + vc.PADDING) * (TECH_PER_BRANCH) - (HEADER_HEIGHT + vc.PADDING) - (TECH_COST_WIDTH + vc.PADDING),
				),
			),
			draw=lambda rect: centerTextButton(rect, 
				'font2', "{}".format(get_tech_for_draw(tech_selected[0], tech_selected[1])['cost']) if tech_selected else "",
				vc.BACKGROUND3, vc.ROUNDING_SMOOTH
			),
			click=lambda pos: None,
		),

		# Add Tech Button
		Component(
			z=2,
			rect=lambda parent: (
				(
					parent[1][0] - TECH_COST_WIDTH,
					parent[1][1] - TECH_COST_WIDTH,
				),
				(TECH_COST_WIDTH, TECH_COST_WIDTH),
			),
			draw=lambda rect: centerTextButton(rect, 'font2', "Add", vc.BACKGROUND3, vc.ROUNDING_SMOOTH, vc.ACCENT),
			click=lambda pos: add_tech(tech_selected[0], tech_selected[1]),
		),
	]
)

def drawTech():
	techMenu.show()
