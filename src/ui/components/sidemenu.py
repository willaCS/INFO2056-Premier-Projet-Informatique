import pygame
import Window
from globals import SelectedTile, all
from ui.components.topbar import TOP_BAR_HEIGHT
from ui.ui_array import button_new, composant_hide, composant_new, composant_show
from ui.utils import image


MENU_BORDER = 5 #en pixels
EXIT_BUTTON_BORDER = 2 #en pixels



def closeSideMenu(pos):
	global sideMenu
	SelectedTile.val = None
	composant_hide(sideMenu)







def __drawSideMenu(rect):
	pygame.draw.rect(Window.inst, all.COLOR_WHITE, ((rect[0][0] + MENU_BORDER, rect[0][1] + MENU_BORDER), (rect[1][0] - 2 * MENU_BORDER, rect[1][1] - 2 * MENU_BORDER)))


def __drawExitButon(rect):
	pygame.draw.rect(Window.inst, all.COLOR_RED, ((rect[0][0] + EXIT_BUTTON_BORDER, rect[0][1] + EXIT_BUTTON_BORDER), (rect[1][0] - 2 * EXIT_BUTTON_BORDER, rect[1][1] - 2 * EXIT_BUTTON_BORDER)))
	
	image.draw(image.img_exit, (
		(rect[1][0] - 2 * EXIT_BUTTON_BORDER, rect[1][1] - 2 * EXIT_BUTTON_BORDER),
		(rect[0][0] + EXIT_BUTTON_BORDER, rect[0][1] + EXIT_BUTTON_BORDER),
	))




sideMenu = composant_new(2, [
	button_new(1,
		lambda: (
			(0, TOP_BAR_HEIGHT),
			(470, Window.resolution[1] - TOP_BAR_HEIGHT)
		),
		__drawSideMenu,
		lambda pos: None,
		closeSideMenu,
	),
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