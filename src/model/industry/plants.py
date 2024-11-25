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

from model.terrain import Ressource, TerrainTile
from model.terrain.terrain import get_terrain_tile
from model.industry import Plant, technologies
from utils.mytyping import coord_i

def init() -> Dict[coord_i, Plant.types]:
	return {}

def get(coord: coord_i) -> Plant.types | None:
	global map
	return map.get(coord)

def add(tile: Plant.types):
	global map
	if get(Plant.position(tile)):
		raise ValueError('Cannot add two tile on the same space')
	map[Plant.position(tile)] = tile

# action by the player to remove an industry from the map
def remove(coord: coord_i):
	global map
	map.pop(coord)

def tile_is_empty(coord: coord_i):
	tile = get(coord)
	if not tile:
		return True
	return Plant.type(tile) == technologies.INDUSTRY_NONE

# action by the player to place a new industry on the map
def place(tile: Plant.types) -> bool:
	if get(Plant.position(tile)) != None:
		return False
	terrain = get_terrain_tile(Plant.position(tile))
	tileProtect = technologies.get_data(Plant.type(tile))
	place_on: List[Dict[str, int]] = tileProtect['place_on']
	for can_place in place_on: 
		can_place_id: int = can_place['id']
		match can_place['type']:
			case technologies.PLACE_ON_TERRAIN:
				if TerrainTile.type(terrain) == can_place_id:
					add(tile)
					return True
			case technologies.PLACE_ON_RESSOURCE:
				ressource = TerrainTile.ressource(terrain)
				if not ressource:
					continue
				can_place = can_place_id
				if Ressource.type(ressource) == can_place_id:
					add(tile)
					return True
			case _:
				pass
	return False

def plant_add_experience(tile, amount):
	if not 'xp' in tile:
		tile['xp'] = 0
	if not 'generated' in tile:
		tile['generated'] = 0
	
	tile['xp'] += 1
	tile['generated'] += amount

map = init()