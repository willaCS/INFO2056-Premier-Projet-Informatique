"""
Ce fichier est le fichier principal.
Il comporte la fonction main qui va appelé la window et contient aussi les
fonction tick executé tout les ticks et la fonction setup executé lorsque
pygame est prêt.
"""

import os

# from model.gameTick import game_model_tick
# from model.stat.setup import setup_stats
# from model.terrain.terrain import init_random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from utils.Window import Window
# from model import Speed
# from events import handleEvents
# from input import repeatKey, singleKey
# from ui.drawFrame import drawFrame
# from ui.framework.image import loadImages
# from ui.framework.text import loadFont
# from utils.time_tester import test_tick

# def setup():
	# init_random()

	# setup_stats()

def setup(
	window#type: Window
): 
	# init_random()
	# setup_stats()

	window.load_font('font1', 'monospace', 40)
	window.load_font('font2', 'monospace', 24, True)
	window.load_font('font3', 'monospace', 22, True)
	window.load_font('title', 'monospace', 50, True)
	
	window.load_image('exit'			, './assets/close_button.png')
	window.load_image('arrow'			, './assets/arrow.png')
	window.load_image('plus'			, './assets/plus.png')
	window.load_image('money'			, './assets/coin.png')
	window.load_image('science'			, './assets/science.png')
	window.load_image('background'		, './assets/background/background.jpeg')
	window.load_image('background2'		, './assets/background/communism.jpg')
	window.load_image('background3'		, './assets/background/t2.jpg')

	window.load_image('sand'			, './assets/terrain/suspicious_sand_0.png')
	window.load_image('stone'			, './assets/terrain/stone.png')
	window.load_image('snow'			, './assets/terrain/diorite.png')
	window.load_image('grass'			, './assets/terrain/grass.png')
	window.load_image('wood'			, './assets/terrain/wood.png')
	window.load_image('coal'			, './assets/ressource/coal_ore.png')
	window.load_image('iron'			, './assets/ressource/iron_ore.png')
	window.load_image('iron2'			, './assets/ressource/iron_ore2.png')
	window.load_image('precious'		, './assets/ressource/diamond_ore3.png')
	window.load_image('rare'			, './assets/ressource/emerald_ore3.png')
	window.load_image('copper'			, './assets/ressource/copper_ore.png')
	window.load_image('salt'			, './assets/ressource/salt.png')
	window.load_image('oil'				, './assets/ressource/oil.png')
	window.load_image('fertile_land'	, './assets/ressource/fertile_land.png')

	window.load_image('industry'					, './assets/industry.png')
	window.load_image('good_fish'					, './assets/goods/fish.png')
	window.load_image('good_salt'					, './assets/goods/salt.png')
	window.load_image('good_wheat'					, './assets/goods/wheat.png')
	window.load_image('good_potato'					, './assets/goods/potato.png')
	window.load_image('good_cotton'					, './assets/goods/string.png')
	window.load_image('good_rice'					, './assets/goods/rice.png')
	window.load_image('good_fur'					, './assets/goods/leather.png')
	window.load_image('good_wood'					, './assets/goods/wood.png')
	window.load_image('good_sand'					, './assets/goods/sand.png')
	window.load_image('good_stone'					, './assets/goods/stone.png')
	window.load_image('good_oil'					, './assets/goods/barrel.png')
	window.load_image('good_coal'					, './assets/goods/coal.png')
	window.load_image('good_iron'					, './assets/goods/iron.png')
	window.load_image('good_copper'					, './assets/goods/copper.png')
	window.load_image('good_precious_metal'			, './assets/goods/diamond.png')
	window.load_image('good_rare_metal'				, './assets/goods/emerald.png')
	window.load_image('good_bread'					, './assets/goods/bread.png')
	window.load_image('good_alcohol'				, './assets/goods/beer.png')
	window.load_image('good_sushi'					, './assets/goods/sushi.png')
	window.load_image('good_textile'				, './assets/goods/part_fabric_blue.png')
	window.load_image('good_clothes'				, './assets/goods/clothes.png')
	window.load_image('good_furniture'				, './assets/goods/bookshelf.png')
	window.load_image('good_steel'					, './assets/goods/ingot_superalloy.png')
	window.load_image('good_tools'					, './assets/goods/tool_fancy_iron_hammer.png')
	window.load_image('good_cement'					, './assets/goods/cement.png')
	window.load_image('good_fuel'					, './assets/goods/part_fuelcan_full.png')
	window.load_image('good_plastic'				, './assets/goods/food_dough.png')
	window.load_image('good_glass'					, './assets/goods/glass.png')
	window.load_image('good_electronics_component'	, './assets/goods/part_electronic_chip.png')
	window.load_image('good_radio'					, './assets/goods/radio.png')
	window.load_image('good_computer'				, './assets/goods/computer.png')
	window.load_image('good_guns'					, './assets/goods/gun.png')
	window.load_image('good_engine'					, './assets/goods/engine.png')
	window.load_image('good_car'					, './assets/goods/car.png')
	window.load_image('good_planes'					, './assets/goods/plane.png')
	window.load_image('good_jewelry'				, './assets/goods/ring.png')
	window.load_image('good_phone'					, './assets/goods/phone.png')

def tick():
	pass
	# game_model_tick()
	# drawFrame()
	# test_tick()



def	main():
	window = Window(
		name="Capitalist Island 2",
		resolution=(800, 800),
		framerate=120,
		tick=tick,
		# handleEvent=handleEvents,
		# repeatKey=repeatKey,
		# singleKey=singleKey,
		# handleEvent=handleEvents,
	)
	setup(window)
	window.start()



if __name__ == '__main__':
	main()
