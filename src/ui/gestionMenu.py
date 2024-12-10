from ui.components import main


GestionMenu_MENU_INTRO = 0
GestionMenu_MENU_REGLAGE = 1
GestionMenu_MENU_JEU = 2

menu = GestionMenu_MENU_INTRO


def change_menu(new_menu):
    global menu

    main.ui_component_main_hide_all()
    menu = new_menu



    