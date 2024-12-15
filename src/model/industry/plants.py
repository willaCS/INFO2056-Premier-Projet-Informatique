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
from model.terrain.TerrainTile import TerrainTile
from model.terrain.terrain import get_terrain_tile
from model.industry.technologies import IndustryType, CanPlaceOn, get_data
from model.industry.Plant import Plant
from utils.mytyping import coord_i

def init() -> Dict[coord_i, Plant]:
	return {}

def get(coord: coord_i) -> Plant | None:
	global map
	return map.get(coord)

def add(tile: Plant):
	global map
	if get(tile.position):
		raise ValueError('Cannot add two tile on the same space')
	map[tile.position] = tile

# action by the player to remove an industry from the map
def remove(coord: coord_i):
	global map
	map.pop(coord)

def tile_is_empty(coord: coord_i):
	tile = get(coord)
	if not tile:
		return True
	return tile.type == IndustryType.NONE

def _can_place_on_terrain(terrain: TerrainTile, technology):
	for can_place in technology['place_on']: 
		can_place_id: int = can_place['id']
		match can_place['type']:
			case CanPlaceOn.TERRAIN:
				if terrain.type == can_place_id:
					return True
			case CanPlaceOn.RESSOURCE:
				ressource = terrain.ressource
				if not ressource:
					continue
				can_place = can_place_id
				if ressource.type == can_place_id:
					return True
			case _:
				raise 'Invalid Technology'
	return False

# action by the player to place a new industry on the map
def place(industry_id, position):
	if not position or get(position) != None:
		return
	
	terrain = get_terrain_tile(position)
	technology = get_data(industry_id)

	if _can_place_on_terrain(terrain, technology)\
		and player_wallet.has_money(technology['price']):
		player_wallet.buy2(technology['price'])
		add(Plant(industry_id, position))

def plant_add_experience(tile: Plant, amount):
	tile.xp += 1
	tile.generated += amount

map = init()
