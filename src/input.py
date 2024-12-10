"""
Ce fichier gère les touches du claviers.
Il gère séparément les touches qui sont executés chaques tick et celle qui ne
s'execute qu'une seule fois
"""

import pygame

import Window
from model import Speed
from model.industry import plants
from model.market import player_wallet
from ui import Cursor, Screenmode, SelectedTile, Zoom
from ui.components.tech import ui_component_tech_drawTech
from ui.map.map import ui_map_map_drawTile
from ui import gestionClavier



def input_repeatKey(key: int):
	if gestionClavier.GestionClavider_clavier == gestionClavier.GestionClavider_CLAVIER_AZERTY:
		input_repeatKey_azerty(key)
	else:
		input_repeatKey_qwerty(key)
		 
def input_singleKey(key: int):
	if gestionClavier.GestionClavider_clavier == gestionClavier.GestionClavider_CLAVIER_AZERTY:
		input_singleKey_azerty(key)
	else:
		input_singleKey_qwerty(key)

 

def input_repeatKey_azerty(key: int):
	match key:
		case pygame.K_v:
			Cursor.Cursor_reset()
		case pygame.K_z | pygame.K_UP:
			Cursor.Cursor_move_up()
		case pygame.K_q | pygame.K_LEFT:
			Cursor.Cursor_move_left()
		case pygame.K_s | pygame.K_DOWN:
			Cursor.Cursor_move_down()
		case pygame.K_d | pygame.K_RIGHT:
			Cursor.Cursor_move_right()
		case pygame.K_r:
			Zoom.Zoom_decrement()
		case pygame.K_f:
			Zoom.Zoom_increment()
		case _:
			pass



def input_repeatKey_qwerty(key):
	match key:
		case pygame.K_v:
			Cursor.Cursor_reset()
		case pygame.K_w | pygame.K_UP:
			Cursor.Cursor_move_up()
		case pygame.K_a | pygame.K_LEFT:
			Cursor.Cursor_move_left()
		case pygame.K_s | pygame.K_DOWN:
			Cursor.Cursor_move_down()
		case pygame.K_d | pygame.K_RIGHT:
			Cursor.Cursor_move_right()
		case pygame.K_r:
			Zoom.Zoom_decrement()
		case pygame.K_f:
			Zoom.Zoom_increment()
		case _:
			pass
		

def input_singleKey_qwerty(key: int):
	match key:
		case pygame.K_ESCAPE:
			Window.Window_stop()
		case pygame.K_F11:
			Window.Window_toggleFullscreen()
		case pygame.K_1:
			Screenmode.select(Screenmode.SCREENMODE_MAIN)
		case pygame.K_2:
			Screenmode.select(Screenmode.SCREENMODE_ECONOMY_SUPPLY)
		case pygame.K_3:
			Screenmode.select(Screenmode.SCREENMODE_ECONOMY_DEMAND)
		case pygame.K_4:
			Screenmode.select(Screenmode.SCREENMODE_TRANSPORT)
		case pygame.K_t:
			Speed.model_speed_increment()
		case pygame.K_g:
			Speed.model_speed_decrement()
		case pygame.K_SPACE:
			Speed.model_speed_pause()
		case pygame.K_KP1:
			Speed.model_speed_set(1)
		case pygame.K_KP2:
			Speed.model_speed_set(2)
		case pygame.K_KP3:
			Speed.model_speed_set(3)
		case pygame.K_KP4:
			Speed.model_speed_set(4)
		case pygame.K_KP5:
			Speed.model_speed_set(5)
		case pygame.K_BACKSPACE:
			if SelectedTile.SelectedTile_val:
				if not plants.model_plants_tile_is_empty(SelectedTile.SelectedTile_val):
					plants.model_plants_remove(SelectedTile.SelectedTile_val)
					ui_map_map_drawTile(SelectedTile.SelectedTile_val, True) # Refresh cache for draw
		case pygame.K_o:
			player_wallet.model_market_wallet_science += 10
		case pygame.K_l:
			player_wallet.model_market_wallet_money += 100000000
		case pygame.K_p:
			ui_component_tech_drawTech()
		case _:
			pass

	
def input_singleKey_azerty(key):
	match key:
		case pygame.K_ESCAPE:
			Window.Window_stop()
		case pygame.K_F11:
			Window.Window_toggleFullscreen()
		case pygame.K_1:
			Screenmode.select(Screenmode.SCREENMODE_MAIN)
		case pygame.K_2:
			Screenmode.select(Screenmode.SCREENMODE_ECONOMY_SUPPLY)
		case pygame.K_3:
			Screenmode.select(Screenmode.SCREENMODE_ECONOMY_DEMAND)
		case pygame.K_4:
			Screenmode.select(Screenmode.SCREENMODE_TRANSPORT)
		case pygame.K_t:
			Speed.model_speed_increment()
		case pygame.K_g:
			Speed.model_speed_decrement()
		case pygame.K_SPACE:
			Speed.model_speed_pause()
		case pygame.K_KP1:
			Speed.model_speed_set(1)
		case pygame.K_KP2:
			Speed.model_speed_set(2)
		case pygame.K_KP3:
			Speed.model_speed_set(3)
		case pygame.K_KP4:
			Speed.model_speed_set(4)
		case pygame.K_KP5:
			Speed.model_speed_set(5)
		case pygame.K_BACKSPACE:
			if SelectedTile.SelectedTile_val:
				if not plants.model_plants_tile_is_empty(SelectedTile.SelectedTile_val):
					plants.model_plants_remove(SelectedTile.SelectedTile_val)
					ui_map_map_drawTile(SelectedTile.SelectedTile_val, True) # Refresh cache for draw
		case pygame.K_o:
			player_wallet.model_market_wallet_science += 10
		case pygame.K_l:
			player_wallet.model_market_wallet_money += 100000000
		case pygame.K_p:
			ui_component_tech_drawTech()
		case _:
			pass

	
	




 
