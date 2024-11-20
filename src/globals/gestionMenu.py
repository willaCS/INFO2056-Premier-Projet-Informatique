from ui.utils.ui_array import menu_hide_all


MENU_INTRO = 0
MENU_REGLAGE = 1
MENU_JEU = 2

menu = MENU_INTRO


def change_menu(new_menu):
    global menu

    menu_hide_all()
    menu = new_menu



    