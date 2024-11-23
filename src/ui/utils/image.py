import pygame

import Window

images = {
	'exit':				['./assets/close_button.png',		None],
}

def setup():
	global images

	for key in images:
		images[key][1] = pygame.image.load(images[key][0]).convert_alpha(Window.inst)

def draw(image_key, rect):
	img_inst = images[image_key][1]
	img = pygame.transform.scale(img_inst, rect[1])
	Window.inst.blit(img, rect[0])