import Window
from ui import gestionMenu, gestionMode
from ui import visual_config as vc
from ui.common.buttons import centerTextButton
from ui.framework import composant_new, button_new, composant_show, drawText, drawRect

BOUTON_LARGEUR = 300
BOUTON_HAUTEUR = 40
BOUTON_ESPACE = 5

def _drawBackground(rect):
	drawRect(rect, vc.SECONDARY)
	drawText('font2', (rect[1][0] // 2, rect[1][1] // 2), "The Capitalism Island 2", vc.TEXT, "center")

		


welcomeMenu = composant_new(0, [
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
	

	# Bouton Play
	button_new(
		1,
		lambda: (
			(
				Window.half_resolution[0] - BOUTON_LARGEUR // 2,
				Window.half_resolution[1] + (BOUTON_HAUTEUR + BOUTON_ESPACE)
			),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: centerTextButton(rect, 'font2', "Play", vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
		lambda pos: gestionMenu.change_menu(gestionMenu.MENU_JEU),
	),

	# Bouton Settings 
	button_new(
		1,
		lambda: (
			(
				Window.half_resolution[0] - BOUTON_LARGEUR // 2,
				Window.half_resolution[1] + (BOUTON_HAUTEUR + BOUTON_ESPACE) * 2
			),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: centerTextButton(rect, 'font2', "Settings", vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
		lambda pos: gestionMenu.change_menu(gestionMenu.MENU_REGLAGE),
	),

	# Bouton Exit 
	button_new(
		1,
		lambda: (
			((Window.half_resolution[0] - 150), (Window.half_resolution[1] + (BOUTON_HAUTEUR + BOUTON_ESPACE) * 3)),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: centerTextButton(rect, 'font2', "Exit", vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
		lambda pos: Window.stop(),
	),
])

def drawWelcome():
	composant_show(welcomeMenu)
