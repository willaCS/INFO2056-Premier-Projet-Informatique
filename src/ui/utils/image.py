import pygame

import Window


img_exit = None

def setup():
	global img_exit
	img_exit = pygame.image.load('./assets/close_button.png').convert_alpha(Window.inst)

def draw(image, rect):
	img = pygame.transform.scale(image, rect[1])
	Window.inst.blit(img, rect[0])