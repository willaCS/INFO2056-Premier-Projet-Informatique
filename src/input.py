"""
Ce fichier gère les touches du claviers.
Il gère séparément les touches qui sont executés chaques tick et celle qui ne
s'execute qu'une seule fois
"""

import pygame

import utils.Window as Window
from model import Speed
from model.industry import Plant, plants
from model.market import player_wallet
from ui import Cursor, Screenmode, SelectedTile, Zoom
from ui.components.tech import drawTech
from ui.map.map import drawTile
from ui import gestionClavier



def repeatKey(key: int):
	if gestionClavier.clavier == gestionClavier.CLAVIER_AZERTY:
		repeatKey_azerty(key)
	else:
		repeatKey_qwerty(key)
		 
def singleKey(key: int):
	if gestionClavier.clavier == gestionClavier.CLAVIER_AZERTY:
		singleKey_azerty(key)
	else:
		singleKey_qwerty(key)

 

def repeatKey_azerty(key: int):
	match key:
		case pygame.K_v:
			Cursor.reset()
		case pygame.K_z | pygame.K_UP:
			Cursor.move_up()
		case pygame.K_q | pygame.K_LEFT:
			Cursor.move_left()
		case pygame.K_s | pygame.K_DOWN:
			Cursor.move_down()
		case pygame.K_d | pygame.K_RIGHT:
			Cursor.move_right()
		case pygame.K_r:
			Zoom.decrement()
		case pygame.K_f:
			Zoom.increment()
		case _:
			pass



def repeatKey_qwerty(key):
	match key:
		case pygame.K_v:
			Cursor.reset()
		case pygame.K_w | pygame.K_UP:
			Cursor.move_up()
		case pygame.K_a | pygame.K_LEFT:
			Cursor.move_left()
		case pygame.K_s | pygame.K_DOWN:
			Cursor.move_down()
		case pygame.K_d | pygame.K_RIGHT:
			Cursor.move_right()
		case pygame.K_r:
			Zoom.decrement()
		case pygame.K_f:
			Zoom.increment()
		case _:
			pass
		

def singleKey_qwerty(key: int):
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
				if not plants.tile_is_empty(SelectedTile.val):
					plants.remove(SelectedTile.val)
					drawTile(SelectedTile.val, True) # Refresh cache for draw
		case pygame.K_o:
			player_wallet.science += 10
		case pygame.K_l:
			player_wallet.money += 100000000
		case pygame.K_p:
			drawTech()
		case _:
			pass

	
def singleKey_azerty(key):
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
				if not plants.tile_is_empty(SelectedTile.val):
					plants.remove(SelectedTile.val)
					drawTile(SelectedTile.val, True) # Refresh cache for draw
		case pygame.K_o:
			player_wallet.science += 10
		case pygame.K_l:
			player_wallet.money += 100000000
		case pygame.K_p:
			drawTech()
		case _:
			pass

	
	




 
