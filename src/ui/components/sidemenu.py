import Window
from globals import all
from ui import SelectedTile
from ui.components.topbar import TOP_BAR_HEIGHT
from ui.framework import button_new, composant_hide, composant_new, composant_show, drawRect, drawImage

MENU_BORDER = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels



def closeSideMenu(pos):
	global sideMenu
	SelectedTile.val = None
	composant_hide(sideMenu)







def __drawSideMenu(rect):
	drawRect((
		(rect[0][0] + MENU_BORDER, rect[0][1] + MENU_BORDER),
		(rect[1][0] - 2 * MENU_BORDER, rect[1][1] - 2 * MENU_BORDER)
	), all.COLOR_WHITE)

def __drawExitButon(rect):
	rect = (
		(rect[0][0] + EXIT_BUTTON_BORDER, rect[0][1] + EXIT_BUTTON_BORDER),
		(rect[1][0] - 2 * EXIT_BUTTON_BORDER, rect[1][1] - 2 * EXIT_BUTTON_BORDER)
	)
	drawRect(rect, all.COLOR_RED)
	drawImage('exit', rect)




sideMenu = composant_new(2, [
	# Background
	button_new(1,
		lambda: (
			(0, TOP_BAR_HEIGHT),
			(470, Window.resolution[1] - TOP_BAR_HEIGHT)
		),
		__drawSideMenu,
		lambda pos: None,
		closeSideMenu,
	),

	# Close button
	button_new(2,
		(
			(425, TOP_BAR_HEIGHT),
			(30, 40)
		),
		__drawExitButon,
		closeSideMenu
	),
])


def showSideMenu():
	composant_show(sideMenu)