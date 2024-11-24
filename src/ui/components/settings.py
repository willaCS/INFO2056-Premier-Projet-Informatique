import pygame
import Window
from globals import gestionMenu
from ui import visual_config as vc
from ui.utils import text
from ui.utils.ui_array import composant_new, button_new, composant_show

BOUTON_LARGEUR = 400
BOUTON_HAUTEUR = 50

OPTION_HEIGHT = BOUTON_HAUTEUR - 2 * vc.PADDING
OPTION_WIDTH = 120


def _drawBackground(rect):
	pygame.draw.rect(Window.inst, vc.SECONDARY, rect)

def _drawSettingBar(rect, message):
	pygame.draw.rect(Window.inst, vc.BACKGROUND, rect, 0, vc.ROUNDING_SMOOTH)
	text.drawText(text.font2, (rect[0][0] + vc.PADDING, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "midleft")

def _drawSettingExit(rect, message):
	pygame.draw.rect(Window.inst, vc.BACKGROUND, rect, 0, vc.ROUNDING_SMOOTH)
	text.drawText(text.font2, (rect[0][0] + rect[1][0] // 2, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "center")

def _drawSettingButton(rect, message):
	pygame.draw.rect(Window.inst, vc.BACKGROUND3, rect, 0, vc.ROUNDING_SMOOTH)
	text.drawText(text.font2, (rect[0][0] + vc.PADDING, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "midleft")


settingsMenu = composant_new(0, [
	# Background
	button_new(
		0,
		lambda: (
			(0, 0),
			Window.resolution
		),
		_drawBackground,
		lambda pos: None,
	),

	# Keyboard Layout
	button_new(
		1,
		lambda: (
			((Window.half_resolution[0] - BOUTON_LARGEUR // 2), (Window.half_resolution[1] + (BOUTON_HAUTEUR + vc.PADDING))),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: _drawSettingBar(rect, "Layout"),
		lambda pos: None,
	),

	# Bouton Azerty 
	button_new(
		2,
		lambda: (
			(
				Window.half_resolution[0] + BOUTON_LARGEUR // 2 - (OPTION_WIDTH + vc.PADDING),
				Window.half_resolution[1] + (BOUTON_HAUTEUR + vc.PADDING) * 1 + vc.PADDING
			),
			(OPTION_WIDTH, OPTION_HEIGHT)
		),
		lambda rect: _drawSettingButton(rect, "AZERTY"),
		lambda pos: None,
	),

	# Bouton Qwerty 
	button_new(
		2,
		lambda: (
			(
				Window.half_resolution[0] + BOUTON_LARGEUR // 2 - (OPTION_WIDTH + vc.PADDING) * 2,
				Window.half_resolution[1] + (BOUTON_HAUTEUR + vc.PADDING) * 1 + vc.PADDING
			),
			(OPTION_WIDTH, OPTION_HEIGHT)
		),
		lambda rect: _drawSettingButton(rect, "QWERTY"),
		lambda pos: None,
	),

	# Bouton Retour 
	button_new(
		1,
		lambda: (
			((Window.half_resolution[0] - BOUTON_LARGEUR // 2), (Window.half_resolution[1] + (BOUTON_HAUTEUR + vc.PADDING) * 2)),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: _drawSettingExit(rect, "Exit"),
		lambda pos: gestionMenu.change_menu(gestionMenu.MENU_INTRO),
	),
])

def drawSettings():
	composant_show(settingsMenu)
