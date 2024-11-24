import pygame
import Window
from globals import gestionMenu
from ui import visual_config as vc
from ui.utils import text
from ui.utils.ui_array import composant_new, button_new, composant_show

BOUTON_LARGEUR = 300
BOUTON_HAUTEUR = 40
BOUTON_ESPACE = 5

def _drawBackground(rect):
	pygame.draw.rect(Window.inst, vc.SECONDARY, rect)
	text.drawText(text.font2, (rect[1][0] // 2, rect[1][1] // 2), "The Capitalism Island 2", vc.TEXT, "center")

def _drawButton(rect, message):
	pygame.draw.rect(Window.inst, vc.BACKGROUND, rect, 0, vc.ROUNDING_SMOOTH)
	text.drawText(text.font2, (rect[0][0] + rect[1][0] // 2, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "center")


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
		lambda rect: _drawButton(rect, "Play"),
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
		lambda rect: _drawButton(rect, "Settings"),
		lambda pos: gestionMenu.change_menu(gestionMenu.MENU_REGLAGE),
	),

	# Bouton Exit 
	button_new(
		1,
		lambda: (
			((Window.half_resolution[0] - 150), (Window.half_resolution[1] + (BOUTON_HAUTEUR + BOUTON_ESPACE) * 3)),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: _drawButton(rect, "Exit"),
		lambda pos: Window.stop(),
	),
])

def drawWelcome():
	composant_show(welcomeMenu)
