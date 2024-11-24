import pygame

import Window

images = {
	'exit':				['./assets/close_button.png',				None],
	'sand':				['./assets/terrain/suspicious_sand_0.png',	None],
	'stone':			['./assets/terrain/stone.png',				None],
	'snow':				['./assets/terrain/diorite.png',			None],
	'grass':			['./assets/terrain/grass.png',				None],
	'wood':				['./assets/terrain/wood.png',				None],
	'coal':				['./assets/ressource/coal_ore.png',			None],
	'iron':				['./assets/ressource/iron_ore.png',			None],
	'iron2':			['./assets/ressource/iron_ore2.png',		None],
	'precious':			['./assets/ressource/diamond_ore3.png',		None],
	'rare':				['./assets/ressource/emerald_ore3.png',		None],
	'copper':			['./assets/ressource/copper_ore.png',		None],
	'salt':				['./assets/ressource/salt.png',				None],
	'oil':				['./assets/ressource/oil.png',				None],
	'fertile_land':		['./assets/ressource/fertile_land.png',		None],
}

def setup():
	global images

	for key in images:
		images[key][1] = pygame.image.load(images[key][0]).convert_alpha(Window.inst)

def draw(image_key, rect):
	img_inst = images[image_key][1]
	img = pygame.transform.scale(img_inst, rect[1])
	Window.inst.blit(img, rect[0])