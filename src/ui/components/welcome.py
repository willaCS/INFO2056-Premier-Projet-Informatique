import Window
from ui import gestionMenu, gestionMode
from ui import visual_config as vc
from ui.common.buttons import ui_common_centerTextButton
from ui.framework.framework import ui_framework_framework_component, ui_framework_framework_component_show, ui_framework_framework_component_hide
from ui.framework.image import ui_framework_image_drawImage
from ui.framework.text import ui_framework_text_drawText

ui_component_welcome_BOUTON_LARGEUR = 300
ui_component_welcome_BOUTON_HAUTEUR = 40
ui_component_welcome_BOUTON_ESPACE = 5

ui_component_welcome_easterEgg = 0

def ui_component_welcome_toggleEasterEgg(mode=0):
	global ui_component_welcome_easterEgg
	if ui_component_welcome_easterEgg == mode:
		ui_component_welcome_easterEgg = 0
	else:
		ui_component_welcome_easterEgg = mode

def ui_component_welcome_getEasterEgg(mode):
	match mode:
		case 0:
			return ('Capitalism Island 2', 'background')
		case 1:
			return ('Communism Island 2', 'background2')
		case 2:
			return ('Colonisalism Island 2', 'background3')

def ui_component_welcome__drawBackground(rect):
	xxx = ui_component_welcome_getEasterEgg(ui_component_welcome_easterEgg)
	ui_framework_image_drawImage(xxx[1], rect)
	# drawRect(rect, vc.SECONDARY)
	ui_framework_text_drawText('title', (rect[1][0] // 2, rect[1][1] // 2), xxx[0], (255, 255, 255), "center")

		


ui_component_welcome_welcomeMenu = ui_framework_framework_component(
	z=0,
	rect=lambda parent: parent,
	draw=ui_component_welcome__drawBackground,
	childs=[
		# Bouton Play
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_welcome_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_welcome_BOUTON_HAUTEUR + ui_component_welcome_BOUTON_ESPACE)
				),
				(ui_component_welcome_BOUTON_LARGEUR, ui_component_welcome_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "Play", vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT),
			click=lambda: gestionMenu.change_menu(gestionMenu.GestionMenu_MENU_JEU),
		),

		# # Bouton Settings 
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_welcome_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_welcome_BOUTON_HAUTEUR + ui_component_welcome_BOUTON_ESPACE) * 2
				),
				(ui_component_welcome_BOUTON_LARGEUR, ui_component_welcome_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "Settings", vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT),
			click=lambda: gestionMenu.change_menu(gestionMenu.GestionMenu_MENU_REGLAGE),
		),

		# Bouton Exit 
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_welcome_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_welcome_BOUTON_HAUTEUR + ui_component_welcome_BOUTON_ESPACE) * 3
				),
				(ui_component_welcome_BOUTON_LARGEUR, ui_component_welcome_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "Exit", vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT),
			click=Window.Window_stop,
		),

		# Bouton Easter Egg 
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(0, 0),
				(100, 100)
			),
			draw=lambda rect: None,
			click=lambda: ui_component_welcome_toggleEasterEgg(1),
		),

		# Bouton Easter Egg 
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(parent[1][0] - 100, 0),
				(100, 100)
			),
			draw=lambda rect: None,
			click=lambda: ui_component_welcome_toggleEasterEgg(2),
		),
	]
)

def ui_component_welcome_drawWelcome():
	ui_framework_framework_component_show(ui_component_welcome_welcomeMenu)
