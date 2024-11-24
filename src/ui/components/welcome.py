import pygame
import Window
from globals import all, gestionMenu
from ui.components.tech import ROUNDING
from ui.utils import image, text
from ui.utils.ui_array import composant_hide, composant_new, button_new, composant_show

JAUNE = (255,255,0)
NOIR = (0, 0, 0)

TEXT = (14, 17, 22)
BACKGROUND = (228, 235, 241)
BACKGROUND2 = (217, 224, 230)
BACKGROUND3 = (191, 201, 211)
PRIMARY = (43, 65, 90)
SECONDARY = (134, 168, 203)
ACCENT = (62, 111, 163)


BOUTON_LARGEUR = 300
BOUTON_HAUTEUR = 40
BOUTON_ESPACE = 5



def _drawBackground(rect):
	pygame.draw.rect(Window.inst, SECONDARY, rect)
	text.drawText(text.font2, (rect[1][0] // 2, rect[1][1] // 2), "The Capitalism Island 2", TEXT, "center")

def _drawButton(rect, message):
	pygame.draw.rect(Window.inst, BACKGROUND, rect, 0, ROUNDING)
	text.drawText(text.font2, (rect[0][0] + rect[1][0] // 2, rect[0][1] + rect[1][1] // 2), message, TEXT, "center")


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
			((Window.half_resolution[0] - 150), (Window.half_resolution[1] + (BOUTON_HAUTEUR + BOUTON_ESPACE))),
			(BOUTON_LARGEUR, BOUTON_HAUTEUR)
		),
		lambda rect: _drawButton(rect, "Play"),
		lambda pos: gestionMenu.change_menu(gestionMenu.MENU_JEU),
	),

	# Bouton Settings 
	button_new(
		1,
		lambda: (
			((Window.half_resolution[0] - 150), (Window.half_resolution[1] + (BOUTON_HAUTEUR + BOUTON_ESPACE) * 2)),
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
		lambda pos: gestionMenu.change_menu(gestionMenu.MENU_REGLAGE),
	),
])

def drawWelcome():
	composant_show(welcomeMenu)
