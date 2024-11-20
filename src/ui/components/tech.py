import pygame
import Window
from logic.techTree import get_tech_for_draw, get_unlocked_techs, add_tech
from map.Industry import print_industry
from ui.utils import image, text
from ui.ui_array import composant_hide, composant_new, button_new, composant_show

tech_selected = None

NB_TECH_BRANCH = 5
TECH_PER_BRANCH = 3

TECH_MENU_SIZE = (500, 300)
PADDING_BOX = 10
PADDING_IN = 5
ROUNDING = 10
ROUNDING_SMOOTH = 5

CLOSE_BUTTON_SIZE = (75, 75)

HEADER_SIZE = (
	(TECH_MENU_SIZE[0] - PADDING_BOX) * 2 - CLOSE_BUTTON_SIZE[1] - PADDING_IN,
	CLOSE_BUTTON_SIZE[1]
)

TECH_SIZE = (
	((TECH_MENU_SIZE[0] - PADDING_BOX) * 2 - (NB_TECH_BRANCH - 1) * PADDING_IN) / NB_TECH_BRANCH,
	75
)

ADD_TECH_SIZE = (
	150,
	150,
)

ADD_TECH_COST_SIZE = (
	150,
	(TECH_MENU_SIZE[1] - PADDING_BOX) * 2 - (TECH_SIZE[1] + PADDING_IN) * (TECH_PER_BRANCH + 1) - ADD_TECH_SIZE[1] - PADDING_IN,
)

TECH_INFO_SIZE = (
	(TECH_MENU_SIZE[0] - PADDING_BOX) * 2 - (ADD_TECH_SIZE[0] + PADDING_IN),
	(TECH_MENU_SIZE[1] - PADDING_BOX) * 2 - (TECH_SIZE[1] + PADDING_IN) * (TECH_PER_BRANCH + 1),
)


TEXT = (14, 17, 22)
BACKGROUND = (228, 235, 241)
BACKGROUND2 = (217, 224, 230)
BACKGROUND3 = (191, 201, 211)
PRIMARY = (43, 65, 90)
SECONDARY = (134, 168, 203)
ACCENT = (62, 111, 163)





def closeTech(pos):
	composant_hide(techMenu)

def _selectTech(i, j):
	global tech_selected
	tech_selected = (i, j)





def _drawBackground(rect):
	pygame.draw.rect(Window.inst, BACKGROUND2, rect, 0, ROUNDING)
	pygame.draw.rect(Window.inst, PRIMARY, rect, 5, ROUNDING)

def _drawExitButon(rect):
	pygame.draw.rect(Window.inst, BACKGROUND3, rect, 0, ROUNDING)
	image.draw(image.img_exit, rect)

def _drawHeader(rect):
	pygame.draw.rect(Window.inst, BACKGROUND3, rect, 0, ROUNDING)
	text.drawText(text.font1, (rect[0][0] + 10, rect[0][1] + 15), "Technologies", (0, 0, 0))

def _drawTech(rect, i, j):
	global tech_selected
	tech = get_tech_for_draw(i, j)
	color = PRIMARY if tech_selected == (i, j) else SECONDARY if tech['unlocked'] else BACKGROUND3
	pygame.draw.rect(Window.inst, color, rect, 0, ROUNDING_SMOOTH)
	text.drawText(text.font2, (rect[0][0] + 10, rect[0][1] + 22), tech['name'], TEXT)


def _drawTechInfo(rect):
	pygame.draw.rect(Window.inst, BACKGROUND3, rect, 0, ROUNDING)
	if tech_selected is None:
		return
	tech = get_tech_for_draw(tech_selected[0], tech_selected[1])
	for i in range(len(tech['unlocks'])):
		message = "Unlocks {}".format(print_industry(tech['unlocks'][i]))
		text.drawText(text.font2, (rect[0][0] + PADDING_BOX, rect[0][1] + PADDING_BOX + 30 * i), message, TEXT)

def _drawAddTechCost(rect):
	pygame.draw.rect(Window.inst, BACKGROUND3, rect, 0, ROUNDING)
	if tech_selected is None:
		return
	tech = get_tech_for_draw(tech_selected[0], tech_selected[1])
	message = "{}".format(tech['cost'])
	text.drawText(text.font2, (rect[0][0] + 10, rect[0][1] + 22), message, TEXT)

def _drawAddTechButton(rect):
	pygame.draw.rect(Window.inst, BACKGROUND3, rect, 0, ROUNDING)
	text.drawText(text.font2, (rect[0][0] + 10, rect[0][1] + 22), "Add", TEXT)

techMenu = composant_new(10, [
	# Background
	button_new(
		1,
		lambda: (
			(
				Window.half_resolution[0] - TECH_MENU_SIZE[0],
				Window.half_resolution[1] - TECH_MENU_SIZE[1]
			),
			(
				TECH_MENU_SIZE[0] * 2,
				TECH_MENU_SIZE[1] * 2
			),
		),
		_drawBackground,
		lambda pos: None,
		lambda pos: composant_hide(techMenu)
	),

	# Header
	button_new(
		2,
		lambda: (
			(
				Window.half_resolution[0] - TECH_MENU_SIZE[0] + PADDING_BOX,
				Window.half_resolution[1] - TECH_MENU_SIZE[1] + PADDING_BOX,
			),
			HEADER_SIZE,
		),
		_drawHeader,
		lambda pos: None,
	),

	# Close button
	button_new(
		2,
		lambda: (
			(
				Window.half_resolution[0] - TECH_MENU_SIZE[0] + PADDING_BOX + HEADER_SIZE[0] + PADDING_IN,
				Window.half_resolution[1] - TECH_MENU_SIZE[1] + PADDING_BOX,
			),
			CLOSE_BUTTON_SIZE,
		),
		_drawExitButon,
		closeTech,
	),

	# Techs
	*[(button_new(
		2,
		lambda i=i, j=j: (
			(
				Window.half_resolution[0] - TECH_MENU_SIZE[0] + PADDING_BOX + (TECH_SIZE[0] + PADDING_IN) * i,
				Window.half_resolution[1] - TECH_MENU_SIZE[1] + PADDING_BOX + (TECH_SIZE[1] + PADDING_IN) * j + HEADER_SIZE[1] + PADDING_IN,
			),
			TECH_SIZE,
		),
		lambda rect, i=i, j=j: _drawTech(rect, i, j),
		lambda pos, i=i, j=j: _selectTech(i, j),
	)) for i in range(NB_TECH_BRANCH) for j in range(TECH_PER_BRANCH)],

	# Selected Tech Info
	button_new(
		2,
		lambda: (
			(
				Window.half_resolution[0] - TECH_MENU_SIZE[0] + PADDING_BOX,
				Window.half_resolution[1] - TECH_MENU_SIZE[1] + PADDING_BOX + (TECH_SIZE[1] + PADDING_IN) * (TECH_PER_BRANCH + 1),
			),
			TECH_INFO_SIZE,
		),
		_drawTechInfo,
		lambda pos: None,
	),

	# Add Tech Cost
	button_new(
		2,
		lambda: (
			(
				Window.half_resolution[0] - TECH_MENU_SIZE[0] + PADDING_BOX + TECH_INFO_SIZE[0] + PADDING_IN,
				Window.half_resolution[1] - TECH_MENU_SIZE[1] + PADDING_BOX + (TECH_SIZE[1] + PADDING_IN) * (TECH_PER_BRANCH + 1),
			),
			ADD_TECH_COST_SIZE,
		),
		_drawAddTechCost,
		lambda pos: None,
	),

	# Add Tech Button
	button_new(
		2,
		lambda: (
			(
				Window.half_resolution[0] - TECH_MENU_SIZE[0] + PADDING_BOX + TECH_INFO_SIZE[0] + PADDING_IN,
				Window.half_resolution[1] - TECH_MENU_SIZE[1] + PADDING_BOX + (TECH_SIZE[1] + PADDING_IN) * (TECH_PER_BRANCH + 1) + ADD_TECH_COST_SIZE[1] + PADDING_IN,
			),
			ADD_TECH_SIZE,
		),
		_drawAddTechButton,
		lambda pos: add_tech(tech_selected[0], tech_selected[1]),
	),
])

def drawTech():
	composant_show(techMenu)
