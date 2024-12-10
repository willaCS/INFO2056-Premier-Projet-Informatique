"""
Ce fichier gère l'instance pygame et gère la resolution et les touches du
clavier de façon générique.
"""

import pygame
from signal import signal, SIGINT
from typing import Callable, Dict
from pygame.event import Event

DEFAULT_RESOLUTION = (1200, 800)

Window__done = False
Window__tickrate = 60

Window_mouse_position = (0, 0)
Window_repeatKeyMap: Dict[int, bool] = {}
Window__singleKey: Callable[[int], None] = lambda key: None
Window__repeatKey: Callable[[int], None] = lambda key: None
Window__handleEvent: Callable[[pygame.event.Event], None] = lambda event: None

Window_inst = 0
Window__is_fullscreen = False
Window_resolution = DEFAULT_RESOLUTION
Window_half_resolution = (DEFAULT_RESOLUTION[0]/2, DEFAULT_RESOLUTION[1]/2)
Window__windowed_resolution = DEFAULT_RESOLUTION

Window__setup: Callable[[], None] = lambda: None
Window__tick: Callable[[], None] = lambda: None



def Window_init(
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
	
	global Window__tickrate, Window__singleKey, Window__repeatKey, Window__handleEvent, Window__setup, Window__tick
	if (not callable(setup) or not callable(tick)):
		raise ValueError("setup or tick is not callable")
	Window__tickrate = tickrate
	Window__singleKey = singleKey
	Window__repeatKey = repeatKey
	Window__handleEvent = handleEvent
	Window__setup = setup
	Window__tick = tick

	pygame.init()

	signal(SIGINT, lambda signal, frame: Window_stop())

	Window__update_window()



def Window_start():
	"""
	Lance l'instance et possède la boucle principale.
	"""
	global Window_time
	Window__setup()
	Window_time = pygame.time.Clock()
	while not Window__done:
		Window__handle_events()
		Window__tick()
		pygame.display.flip()
		Window_time.tick(Window__tickrate)
	pygame.display.quit()
	pygame.quit()



def Window_stop():
	"""
	Termine l'instance
	"""
	global Window__done
	Window__done = True



def Window__handle_events():
	"""
	Prend tout les évenements pygame et fait trois choses :
	- gère et execute la fonction singleKey et repeatKey
	- gère les mises à jours de taille de l'écran
	- gère la fermeture de la fenêtre
	"""
	global Window_repeatKeyMap, Window_mouse_position

	for event in pygame.event.get():
		match event.type:
			case pygame.QUIT:
				Window_stop()

			case pygame.KEYDOWN:
				Window__singleKey(event.key)
				Window_repeatKeyMap[event.key] = True
			
			case pygame.KEYUP:
				Window_repeatKeyMap[event.key] = False

			case pygame.MOUSEMOTION:
				Window_mouse_position = event.pos

			case pygame.WINDOWRESIZED:
				Window__update_resolution((event.x, event.y))
				
			case pygame.WINDOWSIZECHANGED:
				Window__update_resolution((event.x, event.y))

			case _:
				pass
						
		Window__handleEvent(event)

	for (key, is_pressed) in Window_repeatKeyMap.items():
		if not is_pressed:
			continue
		Window__repeatKey(key)



def Window__update_resolution(coord):
	"""
	Set les variables de résolutions après une mise à jour.
	"""
	global Window_half_resolution, Window_resolution
	Window_resolution = coord
	Window_half_resolution = (
		int(Window_resolution[0] / 2),
		int(Window_resolution[1] / 2),
	)


def Window__update_window():
	"""
	Crée l'instance Surface pygame en fonction de si c'est en plein écran ou
	en fenêtré.
	"""
	global Window_inst
	if (Window__is_fullscreen):
		Window_inst = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.NOFRAME)
	else:
		Window_inst = pygame.display.set_mode(Window_resolution, pygame.RESIZABLE)



def Window_toggleFullscreen():
	"""
	active ou désactive le plein écran.
	"""
	global Window__windowed_resolution, Window_resolution, Window__is_fullscreen
	if (not Window__is_fullscreen):
		Window__windowed_resolution = Window_resolution
	else:
		Window_resolution = Window__windowed_resolution
	Window__is_fullscreen = not Window__is_fullscreen
	Window__update_window()
