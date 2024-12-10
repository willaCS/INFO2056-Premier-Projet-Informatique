import Window
from ui import gestionMenu, gestionMode
from ui import visual_config as vc
from ui.common.buttons import centerTextButton
from ui.framework import component, component_show, component_hide, drawText, drawRect
from ui.framework.image import drawImage

BOUTON_LARGEUR = 300
BOUTON_HAUTEUR = 40
BOUTON_ESPACE = 5

easterEgg = False

def toggleEasterEgg():
	global easterEgg
	easterEgg = not easterEgg

def _drawBackground(rect):
	drawImage('background' if not easterEgg else 'background2', rect)
	# drawRect(rect, vc.SECONDARY)
	drawText('title', (rect[1][0] // 2, rect[1][1] // 2), "Capitalism Island 2" if not easterEgg else 'Communism Island 2', (255, 255, 255), "center")

		


welcomeMenu = component(
	z=0,
	rect=lambda parent: parent,
	draw=_drawBackground,
	childs=[
		# Bouton Play
		component(
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
		component(
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
		component(
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
		component(
			z=1,
			rect=lambda parent: (
				(0, 0),
				(100, 100)
			),
			draw=lambda rect: None,
			click=toggleEasterEgg,
		),
	]
)

def drawWelcome():
	component_show(welcomeMenu)
