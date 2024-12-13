import utils.Window as Window
from ui.framework.framework import Component
from ui import gestionMenu
from ui import visual_config as vc
from ui.common.buttons import centerTextButton
from ui.framework import drawText
from ui.framework.image import drawImage

BOUTON_LARGEUR = 300
BOUTON_HAUTEUR = 40
BOUTON_ESPACE = 5

easterEgg = 0

def toggleEasterEgg(mode=0):
	global easterEgg
	if easterEgg == mode:
		easterEgg = 0
	else:
		easterEgg = mode

def getEasterEgg(mode):
	match mode:
		case 0:
			return ('Capitalism Island 2', 'background')
		case 1:
			return ('Communism Island 2', 'background2')
		case 2:
			return ('Colonisalism Island 2', 'background3')

def _drawBackground(rect):
	xxx = getEasterEgg(easterEgg)
	drawImage(xxx[1], rect)
	# drawRect(rect, vc.SECONDARY)
	drawText('title', (rect[1][0] // 2, rect[1][1] // 2), xxx[0], (255, 255, 255), "center")

		


welcomeMenu = Component(
	z=0,
	rect=lambda parent: parent,
	draw=_drawBackground,
	childs=[
		# Bouton Play
		Component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + BOUTON_ESPACE)
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=lambda rect: centerTextButton(rect, 'font2', "Play", vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
			click=lambda: gestionMenu.change_menu(gestionMenu.MENU_JEU),
		),

		# # Bouton Settings 
		Component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + BOUTON_ESPACE) * 2
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=lambda rect: centerTextButton(rect, 'font2', "Settings", vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
			click=lambda: gestionMenu.change_menu(gestionMenu.MENU_REGLAGE),
		),

		# Bouton Exit 
		Component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + BOUTON_ESPACE) * 3
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=lambda rect: centerTextButton(rect, 'font2', "Exit", vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
			click=Window.stop,
		),

		# Bouton Easter Egg 
		Component(
			z=1,
			rect=lambda parent: (
				(0, 0),
				(100, 100)
			),
			draw=lambda rect: None,
			click=lambda: toggleEasterEgg(1),
		),

		# Bouton Easter Egg 
		Component(
			z=1,
			rect=lambda parent: (
				(parent[1][0] - 100, 0),
				(100, 100)
			),
			draw=lambda rect: None,
			click=lambda: toggleEasterEgg(2),
		),
	]
)

def drawWelcome():
	welcomeMenu.show()
