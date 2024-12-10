import Window
from ui import gestionMenu
from ui import visual_config as vc
from ui.common.buttons import ui_common_centerTextButton
from ui.framework.framework import ui_framework_framework_component, ui_framework_framework_component_show, ui_framework_framework_component_hide
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.image import ui_framework_image_drawImage
from ui import gestionClavier, gestionMode
from ui import visual_config
from ui.framework.text import ui_framework_text_drawText

ui_component_settings_BOUTON_LARGEUR = 400
ui_component_settings_BOUTON_HAUTEUR = 50

ui_component_settings_OPTION_HEIGHT = ui_component_settings_BOUTON_HAUTEUR - 2 * vc.VC_PADDING
ui_component_settings_OPTION_WIDTH = 120


def ui_component_settings__drawBackground(rect):
	ui_framework_draw_drawRect(rect, vc.VC_SECONDARY)

def ui_component_settings__drawSettingBar(rect, message):
	ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH)
	ui_framework_text_drawText('font2', (rect[0][0] + vc.VC_PADDING, rect[0][1] + rect[1][1] // 2), message, vc.VC_TEXT, "midleft")

ui_component_settings_settingsMenu = ui_framework_framework_component(
	z=0,
	rect=lambda: (
		(0, 0),
		Window.Window_resolution
	),
	draw=ui_component_settings__drawBackground,
	click=lambda: None,
	childs=[
		# Keyboard Layout
		ui_framework_framework_component(
			z=1,
			padding=vc.VC_PADDING,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_settings_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_settings_BOUTON_HAUTEUR + vc.VC_PADDING),
				),
				(ui_component_settings_BOUTON_LARGEUR, ui_component_settings_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_component_settings__drawSettingBar(rect, "Layout"),
			click=lambda: None,
			childs=[
				# Bouton Azerty 
				ui_framework_framework_component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - ui_component_settings_OPTION_WIDTH, 0),
						(ui_component_settings_OPTION_WIDTH, ui_component_settings_OPTION_HEIGHT)
					),
					draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "AZERTY",
						vc.VC_ACCENT if gestionClavier.GestionClavider_clavier == gestionClavier.GestionClavider_CLAVIER_AZERTY else vc.VC_BACKGROUND3,
						vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT
					),
					click=lambda: gestionClavier.GestionClavider_change_clavier(gestionClavier.GestionClavider_CLAVIER_AZERTY)
				),

				# Bouton Qwerty 
				ui_framework_framework_component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - ui_component_settings_OPTION_WIDTH * 2 - vc.VC_PADDING, 0),
						(ui_component_settings_OPTION_WIDTH, ui_component_settings_OPTION_HEIGHT)
					),
					draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "QWERTY",
						vc.VC_ACCENT if gestionClavier.GestionClavider_clavier == gestionClavier.GestionClavider_CLAVIER_QWERTY else vc.VC_BACKGROUND3,
						vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT
					),
					click=lambda: gestionClavier.GestionClavider_change_clavier(gestionClavier.GestionClavider_CLAVIER_QWERTY)
				),
			]
		),

		# Style
		ui_framework_framework_component(
			z=1,
			padding=vc.VC_PADDING,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_settings_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_settings_BOUTON_HAUTEUR + vc.VC_PADDING) * 2,
				),
				(ui_component_settings_BOUTON_LARGEUR, ui_component_settings_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_component_settings__drawSettingBar(rect, "Style"),
			click=lambda: None,
			childs=[
				# Bouton Light
				ui_framework_framework_component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - ui_component_settings_OPTION_WIDTH, 0),
						(ui_component_settings_OPTION_WIDTH, ui_component_settings_OPTION_HEIGHT)
					),
					draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "LIGHT",
						vc.VC_ACCENT if gestionMode.GestionMode_mode == gestionMode.GestionMode_MODE_LIGHT else vc.VC_BACKGROUND3,
						vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT
					),
					click=lambda: visual_config.VC_change_Background(gestionMode.GestionMode_MODE_LIGHT),
				),

				# Bouton Dark
				ui_framework_framework_component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - ui_component_settings_OPTION_WIDTH * 2 - vc.VC_PADDING, 0),
						(ui_component_settings_OPTION_WIDTH, ui_component_settings_OPTION_HEIGHT)
					),
					draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "DARK",
						vc.VC_ACCENT if gestionMode.GestionMode_mode == gestionMode.GestionMode_MODE_DARK else vc.VC_BACKGROUND3,
						vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT
					),
					click=lambda: visual_config.VC_change_Background(gestionMode.GestionMode_MODE_DARK),
				),
			]
		),

		# Bouton Retour 
		ui_framework_framework_component(
			z=5,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_settings_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_settings_BOUTON_HAUTEUR + vc.VC_PADDING) * 3,
				),
				(ui_component_settings_BOUTON_LARGEUR, ui_component_settings_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', 'Exit', vc.VC_BACKGROUND, vc.VC_ROUNDING_SMOOTH, vc.VC_ACCENT),
			click=lambda pos: gestionMenu.change_menu(gestionMenu.GestionMenu_MENU_INTRO),
		),
	]
)

def ui_component_settings_drawSettings():
	ui_framework_framework_component_show(ui_component_settings_settingsMenu)
