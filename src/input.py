"""
Ce fichier gère les touches du claviers.
Il gère séparément les touches qui sont executés chaques tick et celle qui ne
s'execute qu'une seule fois
"""

import pygame

import window
from globals import cursor, selectedTile, screenmode, speed, zoom
from map import map, tile

def repeatKey(key):
	match key:
		case pygame.K_c:
			cursor.reset()
		case pygame.K_w:
			cursor.move_up()
		case pygame.K_a:
			cursor.move_left()
		case pygame.K_s:
			cursor.move_down()
		case pygame.K_d:
			cursor.move_right()
		case pygame.K_r:
			zoom.decrement()
		case pygame.K_f:
			zoom.increment()
		

def singleKey(key):
	match key:
		case pygame.K_ESCAPE:
			window.stop()
		case pygame.K_F11:
			window.toggleFullscreen()
		case pygame.K_1:
			screenmode.select(screenmode.SCREENMODE_MAIN)
		case pygame.K_2:
			screenmode.select(screenmode.SCREENMODE_ECONOMY_SUPPLY)
		case pygame.K_3:
			screenmode.select(screenmode.SCREENMODE_ECONOMY_DEMAND)
		case pygame.K_4:
			screenmode.select(screenmode.SCREENMODE_TRANSPORT)
		case pygame.K_t:
			speed.increment()
		case pygame.K_g:
			speed.decrement()
		case pygame.K_SPACE:
			speed.pause()
		case pygame.K_KP1:
			speed.set(1)
		case pygame.K_KP2:
			speed.set(2)
		case pygame.K_KP3:
			speed.set(3)
		case pygame.K_KP4:
			speed.set(4)
		case pygame.K_KP5:
			speed.set(5)
		case pygame.K_BACKSPACE:
			if selectedTile.val:
				if not map.tile_is_empty(selectedTile.val):
					map.remove(selectedTile.val)
				selectedTile.clear()
		case pygame.K_z:
			if selectedTile.val:
				if map.tile_is_empty(selectedTile.val):
					map.add(tile.init(tile.TILETYPE_TRANSPORT, selectedTile.val))
				selectedTile.clear()
