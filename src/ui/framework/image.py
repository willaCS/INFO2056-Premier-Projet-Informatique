import pygame

import Window

ui_framework_image_images_loaded = {}

def ui_framework_image_loadImages(images):
	for key in images:
		ui_framework_image_images_loaded[key] = pygame.image.load(images[key]).convert_alpha(Window.Window_inst)

def ui_framework_image_drawImage(image_key, rect):
	img_inst = ui_framework_image_images_loaded[image_key]
	img = pygame.transform.scale(img_inst, rect[1])
	Window.Window_inst.blit(img, rect[0])