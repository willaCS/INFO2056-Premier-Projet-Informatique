from ui.framework import drawRect, drawImage, drawText
from ui import visual_config as vc

def centerTextButton(rect, font, message, color_background, rounding, color_hover = None):
	drawRect(rect, color_background, rounding, hover=color_hover)
	drawText(font, (rect[0][0] + rect[1][0] // 2, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "center")

def centerRightTextButton(rect, font, message, color_background, rounding, padding, color_hover = None):
	drawRect(rect, color_background, rounding, hover=color_hover)
	drawText(font, (rect[0][0] + rect[1][0] - padding, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "midright")

def exit_button(rect):
	drawRect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD, hover=vc.PRIMARY)
	drawImage('exit', rect),