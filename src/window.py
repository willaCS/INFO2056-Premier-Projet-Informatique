import pygame
from signal import signal, SIGINT
from typing import Callable
from pygame.event import Event

__done = False
__tickrate = 60

repeatKeyMap = {}
__singleKey = lambda win, key: None
__repeatKey = lambda win, key: None
__handleEvent = lambda win, event: None

inst = 0
__is_fullscreen = False
resolution = (1200, 800)
half_resolution = (600, 400)
__windowed_resolution = (1200, 800)

__setup = 0
__tick = 0



def init(
	setup: Callable[[], int],
	tick: Callable[[], int],
	handleEvent: Callable[[Event], None] = lambda win, event: None,
	repeatKey: Callable[[str], None] = lambda win, key: None,
	singleKey: Callable[[str], None] = lambda win, key: None,
	tickrate = 60,
):
	global __tickrate, __singleKey, __repeatKey, __handleEvent, __setup, __tick
	if (not callable(setup) or not callable(tick)):
		raise ValueError("setup or tick is not callable")
	__tickrate = tickrate
	__singleKey = singleKey
	__repeatKey = repeatKey
	__handleEvent = handleEvent
	__setup = setup
	__tick = tick

	pygame.init()

	signal(SIGINT, lambda signal, frame: stop())

	__update_window()



def __del__():
	pygame.display.quit()
	pygame.quit()
	return



def start():
	global time
	__setup()
	time = pygame.time.Clock()
	while not __done:
		__handle_input()
		__tick()
		pygame.display.flip()
		time.tick(__tickrate)



def stop():
	global __done
	__done = True



def __handle_input():
	global repeatKeyMap

	for event in pygame.event.get():
		match event.type:
			case pygame.QUIT:
				stop()

			case pygame.KEYDOWN:
				__singleKey(event.key)
				repeatKeyMap[event.key] = True
			
			case pygame.KEYUP:
				repeatKeyMap[event.key] = False

			case pygame.WINDOWRESIZED:
				__update_resolution((event.x, event.y))
				
			case pygame.WINDOWSIZECHANGED:
				__update_resolution((event.x, event.y))
						
		__handleEvent(event)

	for (key, is_pressed) in repeatKeyMap.items():
		if not is_pressed:
			continue
		__repeatKey(key)



def __update_resolution(coord):
	global half_resolution, resolution
	resolution = coord
	half_resolution = (
		int(resolution[0] / 2),
		int(resolution[1] / 2),
	)


def __update_window():
	global inst
	if (__is_fullscreen):
		inst = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.NOFRAME)
	else:
		inst = pygame.display.set_mode(resolution, pygame.RESIZABLE)



def toggleFullscreen():
	global __windowed_resolution, resolution, __is_fullscreen
	if (not __is_fullscreen):
		__windowed_resolution = resolution
	else:
		resolution = __windowed_resolution
	__is_fullscreen = not __is_fullscreen
	__update_window()
