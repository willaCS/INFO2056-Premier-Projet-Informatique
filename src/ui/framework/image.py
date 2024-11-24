import pygame

import Window

images_loaded = {}

def loadImages(images):
	for key in images:
		images_loaded[key] = pygame.image.load(images[key]).convert_alpha(Window.inst)

def drawImage(image_key, rect):
	img_inst = images_loaded[image_key]
	img = pygame.transform.scale(img_inst, rect[1])
	Window.inst.blit(img, rect[0])