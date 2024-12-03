"""
Ce fichier gère l'instance pygame et gère la resolution et les touches du
clavier de façon générique.
"""

import pygame
from signal import signal, SIGINT
from typing import Callable, Dict
from pygame.event import Event
from utils.mytyping import coord_i

DEFAULT_RESOLUTION = (1280, 1024)

__done = False
__tickrate = 60

repeatKeyMap: Dict[int, bool] = {}
__singleKey: Callable[[int], None] = lambda key: None
__repeatKey: Callable[[int], None] = lambda key: None
__handleEvent: Callable[[pygame.event.Event], None] = lambda event: None

inst = 0
__is_fullscreen = False
resolution = DEFAULT_RESOLUTION
half_resolution = (DEFAULT_RESOLUTION[0]/2, DEFAULT_RESOLUTION[1]/2)
__windowed_resolution = DEFAULT_RESOLUTION

__setup: Callable[[], None] = lambda: None
__tick: Callable[[], None] = lambda: None



def init(
	setup:			Callable[[], None]		= lambda: None,
	tick:			Callable[[], None]		= lambda: None,
	handleEvent:	Callable[[Event], None]	= lambda event: None,
	repeatKey:		Callable[[int], None]	= lambda key: None,
	singleKey:		Callable[[int], None]	= lambda key: None,
	tickrate: 		int 					= 60,
):
	"""
	cette fonction initialise l'instance pygame et envoie toutes les lambdas
	fonctions au bonne endroit pour l'execution après.

	Args:
		setup		Callable			: Executée après le début de l'instance
		tick		Callable			: Executée à chaques ticks
		handleEvent	Callable[[Event]]	: Donne les nouveaux events
		repeatKey	Callable[[str]]		: Donne les touches pressées qui sont repetée
		singleKey	Callable[[str]]		: Donne les touches pressées qui sont executée une fois
		tickrate	int					: le nombre de tick par secondes
	"""
	
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



def start():
	"""
	Lance l'instance et possède la boucle principale.
	"""
	global time
	__setup()
	time = pygame.time.Clock()
	while not __done:
		__handle_events()
		__tick()
		pygame.display.flip()
		time.tick(__tickrate)
	pygame.display.quit()
	pygame.quit()



def stop():
	"""
	Termine l'instance
	"""
	global __done
	__done = True



def __handle_events():
	"""
	Prend tout les évenements pygame et fait trois choses :
	- gère et execute la fonction singleKey et repeatKey
	- gère les mises à jours de taille de l'écran
	- gère la fermeture de la fenêtre
	"""
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

			case _:
				pass
						
		__handleEvent(event)

	for (key, is_pressed) in repeatKeyMap.items():
		if not is_pressed:
			continue
		__repeatKey(key)



def __update_resolution(coord: coord_i):
	"""
	Set les variables de résolutions après une mise à jour.
	"""
	global half_resolution, resolution
	resolution = coord
	half_resolution = (
		int(resolution[0] / 2),
		int(resolution[1] / 2),
	)


def __update_window():
	"""
	Crée l'instance Surface pygame en fonction de si c'est en plein écran ou
	en fenêtré.
	"""
	global inst
	if (__is_fullscreen):
		inst = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.NOFRAME)
	else:
		inst = pygame.display.set_mode(resolution, pygame.RESIZABLE)



def toggleFullscreen():
	"""
	active ou désactive le plein écran.
	"""
	global __windowed_resolution, resolution, __is_fullscreen
	if (not __is_fullscreen):
		__windowed_resolution = resolution
	else:
		resolution = __windowed_resolution
	__is_fullscreen = not __is_fullscreen
	__update_window()
