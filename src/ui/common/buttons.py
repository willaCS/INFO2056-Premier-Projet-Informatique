from ui import visual_config as vc
from utils.Window import Window

def centerTextButton(font, message, color_background, rounding, color_hover = None):
	def res(rect, window: Window, is_in: bool):
		window.draw_rect(rect, color_background if not is_in or color_hover == None else color_hover, rounding)
		window.draw_text(font, (rect[0][0] + rect[1][0] // 2, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "center")
	return res

def centerRightTextButton(font, message, color_background, rounding, padding, color_hover = None):
	def res(rect, window: Window, is_in: bool):
		window.draw_rect(rect, color_background if not is_in or color_hover == None else color_hover, rounding)
		window.draw_text(font, (rect[0][0] + rect[1][0] - padding, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "midright")
	return res

def centerLeftTextButton(font, message, color_background, rounding, padding, color_hover = None):
	def res(rect, window: Window, is_in: bool):
		window.draw_rect(rect, color_background if not is_in or color_hover == None else color_hover, rounding)
		window.draw_text(font, (rect[0][0] + padding, rect[0][1] + rect[1][1] // 2), message, vc.TEXT, "midleft")
	return res

def exit_button():
	def res(rect, window: Window):
		window.draw_rect(rect, vc.BACKGROUND3, vc.ROUNDING_HARD, hover=vc.PRIMARY)
		window.draw_image('exit', rect),
	return res

def centerRightText(font, message, padding, color):
	def res(rect, window: Window):
		window.draw_text(font, (rect[0][0] + rect[1][0] - padding, rect[0][1] + rect[1][1] // 2), message, color, "midright")
	return res

def backgroundSubmenu(color_background, color_border, rounding, border_size):
	def res(rect, window: Window):
		window.draw_rect(rect, color_background, rounding) or\
		window.draw_rect(rect, color_border, rounding, border_size),
	return res
