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
	loadFont("font3", "monospace", 22, True)
	loadFont("title", "monospace", 50, True)

	loadImages({
		'exit'			: './assets/close_button.png',
		'arrow'			: './assets/arrow.png',
		'plus'			: './assets/plus.png',
		'money'			: './assets/coin.png',
		'science'		: './assets/science.png',
		'background'	: './assets/background/background.jpeg',
		'background2'	: './assets/background/communism.jpg',
		'background3'	: './assets/background/t2.jpg',

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

		"industry"						: "./assets/industry.png",
		"good_fish"						: "./assets/goods/fish.png",
		"good_salt"						: "./assets/goods/salt.png",
		"good_wheat"					: "./assets/goods/wheat.png",
		"good_potato"					: "./assets/goods/potato.png",
		"good_cotton"					: "./assets/goods/string.png",
		"good_rice"						: "./assets/goods/rice.png",
		"good_fur"						: "./assets/goods/leather.png",
		"good_wood"						: "./assets/goods/wood.png",
		"good_sand"						: "./assets/goods/sand.png",
		"good_stone"					: "./assets/goods/stone.png",
		"good_oil"						: "./assets/goods/barrel.png",
		"good_coal"						: "./assets/goods/coal.png",
		"good_iron"						: "./assets/goods/iron.png",
		"good_copper"					: "./assets/goods/copper.png",
		"good_precious_metal"			: "./assets/goods/diamond.png",
		"good_rare_metal"				: "./assets/goods/emerald.png",
		"good_bread"					: "./assets/goods/bread.png",
		"good_alcohol"					: "./assets/goods/beer.png",
		"good_sushi"					: "./assets/goods/sushi.png",
		"good_textile"					: "./assets/goods/part_fabric_blue.png",
		"good_clothes"					: "./assets/goods/clothes.png",
		"good_furniture"				: "./assets/goods/bookshelf.png",
		"good_steel"					: "./assets/goods/ingot_superalloy.png",
		"good_tools"					: "./assets/goods/tool_fancy_iron_hammer.png",
		"good_cement"					: "./assets/goods/cement.png",
		"good_fuel"						: "./assets/goods/part_fuelcan_full.png",
		"good_plastic"					: "./assets/goods/food_dough.png",
		"good_glass"					: "./assets/goods/glass.png",
		"good_electronics_component"	: "./assets/goods/part_electronic_chip.png",
		"good_radio"					: "./assets/goods/radio.png",
		"good_computer"					: "./assets/goods/computer.png",
		"good_guns"						: "./assets/goods/gun.png",
		"good_engine"					: "./assets/goods/engine.png",
		"good_car"						: "./assets/goods/car.png",
		"good_planes"					: "./assets/goods/plane.png",
		"good_jewelry"					: "./assets/goods/ring.png",
		"good_phone"					: "./assets/goods/phone.png",
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
