"""
Ce fichier gère la carte du jeu.
La carte est faite du dictionaire de coordonnées par la structure case (Tile).
Ce fichier permet de faire :
- obtenir un case avec ses coordonnées
- ajouter une nouvelle case
- supprimer une case
- checker si la case est vide
"""

from typing import Dict, List

from model.market import player_wallet
from model.terrain import Ressource, TerrainTile
from model.terrain.terrain import model_terrain_terrain_get_terrain_tile
from model.industry import Plant, technologies
from utils.mytyping import utils_myTyping_coord_i

def model_plants_init() -> Dict[utils_myTyping_coord_i, Plant.model_Plant_types]:
	return {}

def model_plants_get(coord: utils_myTyping_coord_i) -> Plant.model_Plant_types | None:
	global model_plants_map
	return model_plants_map.get(coord)

def model_plants_add(tile: Plant.model_Plant_types):
	global model_plants_map
	if model_plants_get(Plant.model_Plant_position(tile)):
		raise ValueError('Cannot add two tile on the same space')
	model_plants_map[Plant.model_Plant_position(tile)] = tile

# action by the player to remove an industry from the map
def model_plants_remove(coord: utils_myTyping_coord_i):
	global model_plants_map
	model_plants_map.pop(coord)

def model_plants_tile_is_empty(coord: utils_myTyping_coord_i):
	tile = model_plants_get(coord)
	if not tile:
		return True
	return Plant.model_Plant_type(tile) == technologies.model_technologies_INDUSTRY_NONE

def model_plants__can_place_on_terrain(terrain, technology):
	for can_place in technology['place_on']: 
		can_place_id: int = can_place['id']
		match can_place['type']:
			case technologies.model_technologies_PLACE_ON_TERRAIN:
				if TerrainTile.model_terrain_terrainTile_type(terrain) == can_place_id:
					return True
			case technologies.model_technologies_PLACE_ON_RESSOURCE:
				ressource = TerrainTile.model_terrain_terrainTile_ressource(terrain)
				if not ressource:
					continue
				can_place = can_place_id
				if Ressource.model_terrain_ressource_type(ressource) == can_place_id:
					return True
			case _:
				raise 'Invalid Technology'
	return False

# action by the player to place a new industry on the map
def model_plants_place(industry_id, position):
	if not position or model_plants_get(position) != None:
		return
	
	terrain = model_terrain_terrain_get_terrain_tile(position)
	technology = technologies.model_technologies_get_data(industry_id)

	if model_plants__can_place_on_terrain(terrain, technology)\
		and player_wallet.model_market_wallet_has_money(technology['price']):
		player_wallet.model_market_wallet_buy2(technology['price'])
		model_plants_add(Plant.model_Plant_init(industry_id, position))

def plant_add_experience(tile, amount):
	tile['xp'] += 1
	tile['generated'] += amount

model_plants_map = model_plants_init()
