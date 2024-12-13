from utils.Components import Component
from ui import gestionMenu
from ui import visual_config as vc
from ui.common.buttons import centerLeftTextButton, centerTextButton
from ui import gestionClavier, gestionMode
from ui import visual_config

BOUTON_LARGEUR = 400
BOUTON_HAUTEUR = 50

OPTION_HEIGHT = BOUTON_HAUTEUR - 2 * vc.PADDING
OPTION_WIDTH = 120

settingsMenu = Component(
	rect=lambda window: (
		(0, 0),
		window.resolution
	),
	draw=lambda rect, window: window.drawRect(rect, vc.SECONDARY),
	click=lambda: None,
	childs=[
		# Keyboard Layout
		Component(
			padding=vc.PADDING,
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + vc.PADDING),
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=centerLeftTextButton('font2', 'Layout', vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.PADDING),
			click=lambda: None,
			childs=[
				# Bouton Azerty 
				Component(
					rect=lambda parent: (
						(parent[1][0] - OPTION_WIDTH, 0),
						(OPTION_WIDTH, OPTION_HEIGHT)
					),
					draw=centerTextButton('font2', 'AZERTY',
						vc.ACCENT if gestionClavier.clavier == gestionClavier.CLAVIER_AZERTY else vc.BACKGROUND3,
						vc.ROUNDING_SMOOTH, vc.ACCENT
					),
					click=lambda: gestionClavier.change_clavier(gestionClavier.CLAVIER_AZERTY)
				),

				# Bouton Qwerty 
				Component(
					rect=lambda parent: (
						(parent[1][0] - OPTION_WIDTH * 2 - vc.PADDING, 0),
						(OPTION_WIDTH, OPTION_HEIGHT)
					),
					draw=centerTextButton('font2', 'QWERTY',
						vc.ACCENT if gestionClavier.clavier == gestionClavier.CLAVIER_QWERTY else vc.BACKGROUND3,
						vc.ROUNDING_SMOOTH, vc.ACCENT
					),
					click=lambda: gestionClavier.change_clavier(gestionClavier.CLAVIER_QWERTY)
				),
			]
		),

		# Style
		Component(
			z=1,
			padding=vc.PADDING,
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + vc.PADDING) * 2,
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=centerLeftTextButton('font2', 'Style', vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.PADDING),
			click=lambda: None,
			childs=[
				# Bouton Light
				Component(
					rect=lambda parent: (
						(parent[1][0] - OPTION_WIDTH, 0),
						(OPTION_WIDTH, OPTION_HEIGHT)
					),
					draw=centerTextButton('font2', 'LIGHT',
						vc.ACCENT if gestionMode.mode == gestionMode.MODE_LIGHT else vc.BACKGROUND3,
						vc.ROUNDING_SMOOTH, vc.ACCENT
					),
					click=lambda: visual_config.change_Background(gestionMode.MODE_LIGHT),
				),

				# Bouton Dark
				Component(
					rect=lambda parent: (
						(parent[1][0] - OPTION_WIDTH * 2 - vc.PADDING, 0),
						(OPTION_WIDTH, OPTION_HEIGHT)
					),
					draw=centerTextButton('font2', 'DARK',
						vc.ACCENT if gestionMode.mode == gestionMode.MODE_DARK else vc.BACKGROUND3,
						vc.ROUNDING_SMOOTH, vc.ACCENT
					),
					click=lambda: visual_config.change_Background(gestionMode.MODE_DARK),
				),
			]
		),

		# Bouton Retour 
		Component(
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + vc.PADDING) * 3,
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=centerTextButton('font2', 'Exit', vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
			click=lambda: gestionMenu.change_menu(gestionMenu.MENU_INTRO),
		),
	]
)

def drawSettings():
	settingsMenu.show()
