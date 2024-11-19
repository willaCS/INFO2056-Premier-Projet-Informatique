import pygame
import Window
from utils.draw import isInRectangle

def button_new(
        z,
        rect,
        drawArg,
        exec = None,
        execOutside = lambda: None
    ):
    return {
        "z": z,
        "rect": rect,
        "drawArg": drawArg,
        "exec": exec,
        "execOutside": execOutside
    }

def button_draw(button):
    r = button["rect"] if not callable(button["rect"]) else button["rect"]()
    button["drawArg"](r)

def button_click(button, pos):
    if button["exec"] is None:
        button["execOutside"]()
        return False
    r = button["rect"] if not callable(button["rect"]) else button["rect"]()
    if isInRectangle(pos, r):
        button["exec"]()
        return True
    else:
        button["execOutside"]()
        return False

def button_clickOutside(button, pos):
    r = button["rect"] if not callable(button["rect"]) else button["rect"]()
    if not isInRectangle(pos, r):
        button["execOutside"]()






def composant_new(z, buttons):
    res = {
        "z": z,
        "buttons": buttons,
        "hidden": True
    }
    composants.append(res)
    return res

def composant_hide(button):
    button["hidden"] = True

def composant_show(button):
    button["hidden"] = False

def composant_draw(button):
    if button["hidden"]:
        return
    button["buttons"].sort(key=lambda c: c['z'])
    for button in button["buttons"]:
        button_draw(button)

def composant_click(button, pos):
    if button["hidden"]:
        return False
    button["buttons"].sort(key=lambda c: c['z'], reverse=True)
    for button in button["buttons"]:
        if button_click(button, pos):
            return True
    return False

def composant_clickOutside(button, pos):
    if button["hidden"]:
        return
    for button in button["buttons"]:
        button_clickOutside(button, pos)





composants = []

def menu_add(composant):
    global composants
    composants.append(composant)

def menu_draw():
    global composants
    composants.sort(key=lambda c: c['z'])
    for composant in composants:
        if not composant["hidden"]:
            composant_draw(composant)

def menu_click(pos):
    has_clicked = False
    composants.sort(key=lambda c: c['z'], reverse=True)
    for composant in composants:
        if composant["hidden"]:
            continue
        if has_clicked:
            composant_clickOutside(composant, pos)
            continue
        if composant_click(composant, pos):
            has_clicked = True
    return has_clicked
