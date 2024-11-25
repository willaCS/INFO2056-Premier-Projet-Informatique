from ui.framework.draw import drawRect
from ui.framework.text import drawText
from ui import visual_config as vc

def centerTextButton(rect, font, message, color_background, rounding, color_hover = None):
	drawRect(rect, color_background, rounding, hover=color_hover)
	drawText(font, (rect[0][0] + rect[1][0] // 2, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "center")