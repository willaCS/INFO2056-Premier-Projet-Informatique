import pygame

import window
import globals.all
import globals.cursor
import globals.selectedTile
import globals.speed
import globals.zoom
from globals.all import SCREENMODE_ECONOMY_DEMAND, SCREENMODE_ECONOMY_SUPPLY, SCREENMODE_MAIN, SCREENMODE_TRANSPORT
from map.map import map_add, map_remove, tile_is_empty
from map.tile import TILETYPE_TRANSPORT, tile_init

def repeatKey(key):
	match key:
		case pygame.K_c:
			globals.cursor.reset()
		case pygame.K_w:
			globals.cursor.move_up()
		case pygame.K_a:
			globals.cursor.move_left()
		case pygame.K_s:
			globals.cursor.move_down()
		case pygame.K_d:
			globals.cursor.move_right()
		case pygame.K_r:
			globals.zoom.decrement()
		case pygame.K_f:
			globals.zoom.increment()
		

def singleKey(key):
	match key:
		case pygame.K_ESCAPE:
			window.stop()
		case pygame.K_F11:
			window.toggleFullscreen()
		case pygame.K_1:
			globals.all.screen_mode = SCREENMODE_MAIN
		case pygame.K_2:
			globals.all.screen_mode = SCREENMODE_ECONOMY_SUPPLY
		case pygame.K_3:
			globals.all.screen_mode = SCREENMODE_ECONOMY_DEMAND
		case pygame.K_4:
			globals.all.screen_mode = SCREENMODE_TRANSPORT
		case pygame.K_t:
			globals.speed.increment()
		case pygame.K_g:
			globals.speed.decrement()
		case pygame.K_SPACE:
			globals.speed.pause()
		case pygame.K_KP1:
			globals.speed.set(1)
		case pygame.K_KP2:
			globals.speed.set(2)
		case pygame.K_KP3:
			globals.speed.set(3)
		case pygame.K_KP4:
			globals.speed.set(4)
		case pygame.K_KP5:
			globals.speed.set(5)
		case pygame.K_BACKSPACE:
			if globals.selectedTile.val:
				if not tile_is_empty(globals.selectedTile.val):
					map_remove(globals.selectedTile.val)
				globals.selectedTile.clear()
		case pygame.K_z:
			if globals.selectedTile.val:
				if tile_is_empty(globals.selectedTile.val):
					map_add(tile_init(TILETYPE_TRANSPORT, globals.selectedTile.val))
				globals.selectedTile.clear()
