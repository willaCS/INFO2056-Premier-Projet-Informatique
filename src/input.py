"""
Ce fichier gère les touches du claviers.
Il gère séparément les touches qui sont executés chaques tick et celle qui ne
s'execute qu'une seule fois
"""

import pygame

import Window
from globals import Cursor, Screenmode, SelectedTile, Speed, Zoom
from map import Map, Tile

def repeatKey(key):
	match key:
		case pygame.K_c:
			Cursor.reset()
		case pygame.K_w:
			Cursor.move_up()
		case pygame.K_a:
			Cursor.move_left()
		case pygame.K_s:
			Cursor.move_down()
		case pygame.K_d:
			Cursor.move_right()
		case pygame.K_r:
			Zoom.decrement()
		case pygame.K_f:
			Zoom.increment()
		

def singleKey(key):
	match key:
		case pygame.K_ESCAPE:
			Window.stop()
		case pygame.K_F11:
			Window.toggleFullscreen()
		case pygame.K_1:
			Screenmode.select(Screenmode.SCREENMODE_MAIN)
		case pygame.K_2:
			Screenmode.select(Screenmode.SCREENMODE_ECONOMY_SUPPLY)
		case pygame.K_3:
			Screenmode.select(Screenmode.SCREENMODE_ECONOMY_DEMAND)
		case pygame.K_4:
			Screenmode.select(Screenmode.SCREENMODE_TRANSPORT)
		case pygame.K_t:
			Speed.increment()
		case pygame.K_g:
			Speed.decrement()
		case pygame.K_SPACE:
			Speed.pause()
		case pygame.K_KP1:
			Speed.set(1)
		case pygame.K_KP2:
			Speed.set(2)
		case pygame.K_KP3:
			Speed.set(3)
		case pygame.K_KP4:
			Speed.set(4)
		case pygame.K_KP5:
			Speed.set(5)
		case pygame.K_BACKSPACE:
			if SelectedTile.val:
				if not Map.tile_is_empty(SelectedTile.val):
					Map.remove(SelectedTile.val)
				SelectedTile.clear()
		case pygame.K_z:
			if SelectedTile.val:
				if Map.tile_is_empty(SelectedTile.val):
					Map.add(Tile.init(Tile.TILETYPE_TRANSPORT, SelectedTile.val))
				SelectedTile.clear()
