"""
Ce fichier est le fichier principal.
Il comporte la fonction main qui va appelé la window et contient aussi les
fonction tick executé tout les ticks et la fonction setup executé lorsque
pygame est prêt.
"""

import os

from model.gameTick import game_model_tick
from model.terrain.terrain import init_random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import Window
from model import Speed
from events import handleEvents
from input import repeatKey, singleKey
from ui.drawFrame import drawFrame
from ui.framework.image import loadImages
from ui.framework.text import loadFont
# from utils.time_tester import test_tick

def setup():
	init_random()
	loadFont("font1", "monospace", 40)
	loadFont("font2", "monospace", 24, True)

	loadImages({
		'exit'			: './assets/close_button.png',
		'sand'			: './assets/terrain/suspicious_sand_0.png',
		'stone'			: './assets/terrain/stone.png',
		'snow'			: './assets/terrain/diorite.png',
		'grass'			: './assets/terrain/grass.png',
		'wood'			: './assets/terrain/wood.png',
		'coal'			: './assets/ressource/coal_ore.png',
		'iron'			: './assets/ressource/iron_ore.png',
		'iron2'			: './assets/ressource/iron_ore2.png',
		'precious'		: './assets/ressource/diamond_ore3.png',
		'rare'			: './assets/ressource/emerald_ore3.png',
		'copper'		: './assets/ressource/copper_ore.png',
		'salt'			: './assets/ressource/salt.png',
		'oil'			: './assets/ressource/oil.png',
		'fertile_land'	: './assets/ressource/fertile_land.png',
	})


def tick():
	game_model_tick()
	drawFrame()
	# test_tick()



def	main():
	Window.init(setup, tick, handleEvents, repeatKey, singleKey)
	Window.start()



if __name__ == '__main__':
	main()
