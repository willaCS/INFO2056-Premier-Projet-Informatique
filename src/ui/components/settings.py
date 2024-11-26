import Window
from ui import gestionMenu
from ui import visual_config as vc
from ui.common.buttons import centerTextButton
from ui.framework import composant_new, button_new, composant_show, drawRect, drawText
from ui import gestionClavier, gestionMode
from ui import visual_config

BOUTON_LARGEUR = 400
BOUTON_HAUTEUR = 50

OPTION_HEIGHT = BOUTON_HAUTEUR - 2 * vc.PADDING
OPTION_WIDTH = 120


def _drawBackground(rect):
	drawRect(rect, vc.SECONDARY)

def _drawSettingBar(rect, message):
	drawRect(rect, vc.BACKGROUND, vc.ROUNDING_SMOOTH)
	drawText('font2', (rect[0][0] + vc.PADDING, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "midleft")

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
		lambda rect: centerTextButton(rect, 'font2', "AZERTY", vc.ACCENT if gestionClavier.clavier == gestionClavier.CLAVIER_AZERTY else vc.BACKGROUND3, vc.ROUNDING_SMOOTH, vc.ACCENT),
		lambda pos: gestionClavier.change_clavier(gestionClavier.CLAVIER_AZERTY)
		
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
		lambda rect: centerTextButton(rect, 'font2', "QWERTY", vc.ACCENT if gestionClavier.clavier == gestionClavier.CLAVIER_QWERTY else vc.BACKGROUND3, vc.ROUNDING_SMOOTH, vc.ACCENT),
		lambda pos: gestionClavier.change_clavier(gestionClavier.CLAVIER_QWERTY)
	),

		# MODE
	button_new(
		3,
		lambda: (
			((Window.half_resolution[0] - BOUTON_LARGEUR // 2), (Window.half_resolution[1] + (BOUTON_HAUTEUR + vc.PADDING)) *1.1),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: _drawSettingBar(rect, "MODE"),
		lambda pos: None,
	),

	# Bouton DARK 
	button_new(
		4,
		lambda: (
			(
				Window.half_resolution[0] + BOUTON_LARGEUR // 2 - (OPTION_WIDTH + vc.PADDING) *2,
				(Window.half_resolution[1] + (BOUTON_HAUTEUR + vc.PADDING) * 1 + vc.PADDING) * 1.1
			),
			(OPTION_WIDTH, OPTION_HEIGHT)
		),
		lambda rect: centerTextButton(rect, 'font2', "DARK", vc.ACCENT if gestionMode.mode == gestionMode.MODE_DARK else vc.BACKGROUND3, vc.ROUNDING_SMOOTH, vc.ACCENT),
		lambda pos: visual_config.change_Background(gestionMode.MODE_DARK)
		
	),

	# Bouton LIGHT 
	button_new(
		4,
		lambda: (
			(
				Window.half_resolution[0] + BOUTON_LARGEUR // 2 - (OPTION_WIDTH + vc.PADDING),
				(Window.half_resolution[1] + (BOUTON_HAUTEUR + vc.PADDING) * 1 + vc.PADDING) * 1.1
			),
			(OPTION_WIDTH, OPTION_HEIGHT)
		),
		lambda rect: centerTextButton(rect, 'font2', "LIGHT", vc.ACCENT if gestionMode.mode == gestionMode.MODE_LIGHT else vc.BACKGROUND3, vc.ROUNDING_SMOOTH, vc.ACCENT),
		lambda pos: visual_config.change_Background(gestionMode.MODE_LIGHT)
	),

	# Bouton Retour 
	button_new(
		5,
		lambda: (
			((Window.half_resolution[0] - BOUTON_LARGEUR // 2), (Window.half_resolution[1] + (BOUTON_HAUTEUR + vc.PADDING) * 3)),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: centerTextButton(rect, 'font2', "Exit", vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
		lambda pos: gestionMenu.change_menu(gestionMenu.MENU_INTRO),
	),
])

def drawSettings():
	composant_show(settingsMenu)
