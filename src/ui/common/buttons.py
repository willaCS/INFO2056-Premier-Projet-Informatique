from ui import visual_config as vc
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.image import ui_framework_image_drawImage
from ui.framework.text import ui_framework_text_drawText

def ui_common_centerTextButton(rect, font, message, color_background, rounding, color_hover = None):
	ui_framework_draw_drawRect(rect, color_background, rounding, hover=color_hover)
	ui_framework_text_drawText(font, (rect[0][0] + rect[1][0] // 2, rect[0][1] + rect[1][1] // 2), message, vc.VC_TEXT, "center")

def ui_common_centerRightTextButton(rect, font, message, color_background, rounding, padding, color_hover = None):
	ui_framework_draw_drawRect(rect, color_background, rounding, hover=color_hover)
	ui_framework_text_drawText(font, (rect[0][0] + rect[1][0] - padding, rect[0][1] + rect[1][1] // 2), message, vc.VC_TEXT, "midright")

def ui_common_centerLeftTextButton(rect, font, message, color_background, rounding, padding, color_hover = None):
	ui_framework_draw_drawRect(rect, color_background, rounding, hover=color_hover)
	ui_framework_text_drawText(font, (rect[0][0] + padding, rect[0][1] + rect[1][1] // 2), message, vc.VC_TEXT, "midleft")

def ui_common_exit_button(rect):
	ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND3, vc.VC_ROUNDING_HARD, hover=vc.VC_PRIMARY)
	ui_framework_image_drawImage('exit', rect),

def ui_common_centerRightText(rect, font, message, padding, color):
	ui_framework_text_drawText(font, (rect[0][0] + rect[1][0] - padding, rect[0][1] + rect[1][1] // 2), message, color, "midright")