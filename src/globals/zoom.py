val = 5
__zoom_speed = 1.1
__zoom_max = 1
__zoom_min = 10
tile_size = 0
line_width = 0
outline_width = 0

def __update():
	global tile_size, line_width, outline_width
	tile_size = int(200 / val)
	line_width = int(25 / val)
	outline_width = int(15 / val)

def increment():
	global val
	if val < __zoom_min:
		val *= __zoom_speed
		__update()

def decrement():
	global val
	if val > __zoom_max:
		val /= __zoom_speed
		__update()

__update()