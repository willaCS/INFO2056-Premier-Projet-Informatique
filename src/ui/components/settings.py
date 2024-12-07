import Window
from ui import gestionMenu
from ui import visual_config as vc
from ui.common.buttons import centerTextButton
from ui.framework import component, component_show, component_hide, drawRect, drawText
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

settingsMenu = component(
	z=0,
	rect=lambda: (
		(0, 0),
		Window.resolution
	),
	draw=_drawBackground,
	click=lambda: None,
	childs=[
		# Keyboard Layout
		component(
			z=1,
			padding=vc.PADDING,
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + vc.PADDING),
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=lambda rect: _drawSettingBar(rect, "Layout"),
			click=lambda: None,
			childs=[
				# Bouton Azerty 
				component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - OPTION_WIDTH, 0),
						(OPTION_WIDTH, OPTION_HEIGHT)
					),
					draw=lambda rect: centerTextButton(rect, 'font2', "AZERTY",
						vc.ACCENT if gestionClavier.clavier == gestionClavier.CLAVIER_AZERTY else vc.BACKGROUND3,
						vc.ROUNDING_SMOOTH, vc.ACCENT
					),
					click=lambda: gestionClavier.change_clavier(gestionClavier.CLAVIER_AZERTY)
				),

				# Bouton Qwerty 
				component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - OPTION_WIDTH * 2 - vc.PADDING, 0),
						(OPTION_WIDTH, OPTION_HEIGHT)
					),
					draw=lambda rect: centerTextButton(rect, 'font2', "QWERTY",
						vc.ACCENT if gestionClavier.clavier == gestionClavier.CLAVIER_QWERTY else vc.BACKGROUND3,
						vc.ROUNDING_SMOOTH, vc.ACCENT
					),
					click=lambda: gestionClavier.change_clavier(gestionClavier.CLAVIER_QWERTY)
				),
			]
		),

		# Style
		component(
			z=1,
			padding=vc.PADDING,
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + vc.PADDING) * 2,
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=lambda rect: _drawSettingBar(rect, "Style"),
			click=lambda: None,
			childs=[
				# Bouton Light
				component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - OPTION_WIDTH, 0),
						(OPTION_WIDTH, OPTION_HEIGHT)
					),
					draw=lambda rect: centerTextButton(rect, 'font2', "LIGHT",
						vc.ACCENT if gestionMode.mode == gestionMode.MODE_LIGHT else vc.BACKGROUND3,
						vc.ROUNDING_SMOOTH, vc.ACCENT
					),
					click=lambda: visual_config.change_Background(gestionMode.MODE_LIGHT),
				),

				# Bouton Dark
				component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - OPTION_WIDTH * 2 - vc.PADDING, 0),
						(OPTION_WIDTH, OPTION_HEIGHT)
					),
					draw=lambda rect: centerTextButton(rect, 'font2', "DARK",
						vc.ACCENT if gestionMode.mode == gestionMode.MODE_DARK else vc.BACKGROUND3,
						vc.ROUNDING_SMOOTH, vc.ACCENT
					),
					click=lambda: visual_config.change_Background(gestionMode.MODE_DARK),
				),
			]
		),

		# Bouton Retour 
		component(
			z=5,
			rect=lambda parent: (
				(
					(parent[1][0] - BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (BOUTON_HAUTEUR + vc.PADDING) * 3,
				),
				(BOUTON_LARGEUR, BOUTON_HAUTEUR)
			),
			draw=lambda rect: centerTextButton(rect, 'font2', 'Exit', vc.BACKGROUND, vc.ROUNDING_SMOOTH, vc.ACCENT),
			click=lambda pos: gestionMenu.change_menu(gestionMenu.MENU_INTRO),
		),
	]
)

def drawSettings():
	component_show(settingsMenu)
