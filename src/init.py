"""
Ce fichier est le fichier principal.
Il comporte la fonction main qui va appelé la window et contient aussi les
fonction tick executé tout les ticks et la fonction setup executé lorsque
pygame est prêt.
"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import Window
from globals import Speed
from events import handleEvents
from input import repeatKey, singleKey
from logic.game import game_simulation_tick
from map.generation.map import init_random
from ui.drawFrame import drawFrame
from ui.utils import image, text
# from utils.time_tester import test_tick

def setup():
	init_random()
	image.setup()
	text.setup()


def tick():
	if Speed.can_execute_simulation():
		game_simulation_tick()
	drawFrame()
	# test_tick()



def	main():
	Window.init(setup, tick, handleEvents, repeatKey, singleKey)
	Window.start()



if __name__ == '__main__':
	main()
