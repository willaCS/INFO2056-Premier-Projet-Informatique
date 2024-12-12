import math
import random
import signal
from typing import Any, Callable, Dict, List, Tuple

import pygame

model_market_goods_GOODS_FISH					= 1
model_market_goods_GOODS_SALT					= 2
model_market_goods_GOODS_WHEAT					= 3
model_market_goods_GOODS_POTATO				= 4
model_market_goods_GOODS_COTTON				= 5
model_market_goods_GOODS_RICE					= 6
model_market_goods_GOODS_FUR					= 7
model_market_goods_GOODS_WOOD					= 8
model_market_goods_GOODS_OIL					= 9
model_market_goods_GOODS_COAL					= 10
model_market_goods_GOODS_IRON					= 11
model_market_goods_GOODS_COPPER				= 12
model_market_goods_GOODS_PRECIOUS_METAL		= 13
model_market_goods_GOODS_RARE_METAL			= 14
model_market_goods_GOODS_BREAD					= 15
model_market_goods_GOODS_ALCOHOL				= 16
model_market_goods_GOODS_SUSHI					= 17
model_market_goods_GOODS_TEXTILE				= 18
model_market_goods_GOODS_CLOTHES				= 19
model_market_goods_GOODS_FURNITURE				= 20
model_market_goods_GOODS_STEEL					= 21
model_market_goods_GOODS_TOOLS					= 22
model_market_goods_GOODS_CEMENT				= 23
model_market_goods_GOODS_FUEL					= 24
model_market_goods_GOODS_PLASTIC				= 25
model_market_goods_GOODS_GLASS					= 26
model_market_goods_GOODS_ELECTRONICS_COMPONENT	= 27
model_market_goods_GOODS_RADIO					= 28
model_market_goods_GOODS_COMPUTER				= 29
model_market_goods_GOODS_GUNS					= 30
model_market_goods_GOODS_ENGINE				= 31
model_market_goods_GOODS_CAR					= 32
model_market_goods_GOODS_PLANES				= 33
model_market_goods_GOODS_JEWELRY				= 34
model_market_goods_GOODS_PHONE					= 35
model_market_goods_GOODS_STONE					= 36
model_market_goods_GOODS_SAND					= 37


model_terrain_ressource_RESSOURCE_FISH				= 1
model_terrain_ressource_RESSOURCE_SALT				= 2
model_terrain_ressource_RESSOURCE_FERTILE_LAND		= 3
model_terrain_ressource_RESSOURCE_HUNTING_GROUNDS	= 4
model_terrain_ressource_RESSOURCE_WOOD				= 5
model_terrain_ressource_RESSOURCE_OIL				= 6
model_terrain_ressource_RESSOURCE_COAL				= 7
model_terrain_ressource_RESSOURCE_IRON				= 8
model_terrain_ressource_RESSOURCE_COPPER			= 9
model_terrain_ressource_RESSOURCE_PRECIOUS_METALS	= 10
model_terrain_ressource_RESSOURCE_RARE_METALS		= 11
model_terrain_ressource_RESSOURCE_SAND				= 12
model_terrain_ressource_RESSOURCE_STONE				= 13



model_terrain_terrainTile_TERRAINTILETYPE_DEEPSEA			= 1
model_terrain_terrainTile_TERRAINTILETYPE_SEA				= 2
model_terrain_terrainTile_TERRAINTILETYPE_BEACH			= 3
model_terrain_terrainTile_TERRAINTILETYPE_PLAIN			= 4
model_terrain_terrainTile_TERRAINTILETYPE_FOREST			= 5
model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE	= 6
model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_TOP	= 7




SCREENMODE_MAIN				= 1
SCREENMODE_ECONOMY_SUPPLY	= 2
SCREENMODE_ECONOMY_DEMAND	= 3
SCREENMODE_TRANSPORT		= 4

SCREENSUBMODE_NONE			= 0
SCREENSUBMODE_CONSTRUCTION	= 1

utils_myTyping_coord_f = Tuple[float, float]
utils_myTyping_coord_i = Tuple[int, int]

utils_myTyping_mut_coord_f = List[float]
utils_myTyping_mut_coord_i = List[int]

utils_myTyping_Color = Tuple[int, int, int]

model_Plant_coord = Tuple[int, int]
model_Plant_types = Dict[str, int | model_Plant_coord]




model_terrain_ressource_types = Dict[str, int | str]
model_terrain_terrainTile_coord = Tuple[int, int]
model_terrain_terrainTile_types = Dict[str, int | model_terrain_terrainTile_coord | model_terrain_ressource_types | None]





VC_DARK_TEXT		    = (228, 231, 234)
VC_DARK_BACKGROUND	    = (9, 13, 17)
VC_DARK_BACKGROUND2	= (20, 24, 28)
VC_DARK_BACKGROUND3	= (47, 56, 66)
VC_DARK_PRIMARY		= (29, 74, 128)
VC_DARK_SECONDARY	    = (38, 47, 58)
VC_DARK_ACCENT	        = (27, 119, 230)


VC_LIGHT_TEXT		    = (14, 17, 22)
VC_LIGHT_BACKGROUND	= (228, 235, 241)
VC_LIGHT_BACKGROUND2	= (217, 224, 230)
VC_LIGHT_BACKGROUND3	= (191, 201, 211)
VC_LIGHT_PRIMARY		= (43, 65, 90)
VC_LIGHT_SECONDARY	    = (134, 168, 203)
VC_LIGHT_ACCENT	    = (62, 111, 163)

VC_TEXT		= VC_LIGHT_TEXT		
VC_BACKGROUND	= VC_LIGHT_BACKGROUND	
VC_BACKGROUND2	= VC_LIGHT_BACKGROUND2	
VC_BACKGROUND3	= VC_LIGHT_BACKGROUND3	
VC_PRIMARY		= VC_LIGHT_PRIMARY		
VC_SECONDARY	= VC_LIGHT_SECONDARY	
VC_ACCENT		= VC_LIGHT_ACCENT		



VC_ROUNDING_SMOOTH = 5
VC_ROUNDING_HARD = 10
VC_MENU_BORDER_WIDTH = 5

VC_PADDING = 5

VC_TOP_BAR_HEIGHT = 60
VC_LARGEUR_SIDEMENU = 470



def utils_cache_add_cache(arg_func: Callable[[utils_myTyping_coord_i], Any]) -> Callable[[utils_myTyping_coord_i], Any]:
	cache: Dict[utils_myTyping_coord_i, int] = {}
	
	def wrapper(coord: utils_myTyping_coord_i, refresh: bool = False):
		if refresh or cache.get(coord) == None:
			cache[coord] = arg_func(coord)
		return cache.get(coord)
	return wrapper



	

DEFAULT_RESOLUTION = (1200, 800)

Window__done = False
Window__tickrate = 60

Window_mouse_position = (0, 0)
Window_repeatKeyMap: Dict[int, bool] = {}
Window__singleKey: Callable[[int], None] = lambda key: None
Window__repeatKey: Callable[[int], None] = lambda key: None
Window__handleEvent: Callable[[pygame.event.Event], None] = lambda event: None

Window_inst = 0
Window__is_fullscreen = False
Window_resolution = DEFAULT_RESOLUTION
Window_half_resolution = (DEFAULT_RESOLUTION[0]/2, DEFAULT_RESOLUTION[1]/2)
Window__windowed_resolution = DEFAULT_RESOLUTION

Window__setup: Callable[[], None] = lambda: None
Window__tick: Callable[[], None] = lambda: None



def Window_init(
	setup:			Callable[[], None]		= lambda: None,
	tick:			Callable[[], None]		= lambda: None,
	handleEvent:	Callable[[], None]	= lambda event: None,
	repeatKey:		Callable[[int], None]	= lambda key: None,
	singleKey:		Callable[[int], None]	= lambda key: None,
	tickrate: 		int 					= 60,
):
	"""
	cette fonction initialise l'instance pygame et envoie toutes les lambdas
	fonctions au bonne endroit pour l'execution après.

	Args:
		setup		Callable			: Executée après le début de l'instance
		tick		Callable			: Executée à chaques ticks
		handleEvent	Callable[[Event]]	: Donne les nouveaux events
		repeatKey	Callable[[str]]		: Donne les touches pressées qui sont repetée
		singleKey	Callable[[str]]		: Donne les touches pressées qui sont executée une fois
		tickrate	int					: le nombre de tick par secondes
	"""
	
	global Window__tickrate, Window__singleKey, Window__repeatKey, Window__handleEvent, Window__setup, Window__tick
	if (not callable(setup) or not callable(tick)):
		raise ValueError("setup or tick is not callable")
	Window__tickrate = tickrate
	Window__singleKey = singleKey
	Window__repeatKey = repeatKey
	Window__handleEvent = handleEvent
	Window__setup = setup
	Window__tick = tick

	pygame.init()

	signal.signal(signal.SIGINT, lambda signal, frame: Window_stop())

	Window__update_window()



def Window_start():
	"""
	Lance l'instance et possède la boucle principale.
	"""
	global Window_time
	Window__setup()
	Window_time = pygame.time.Clock()
	while not Window__done:
		Window__handle_events()
		Window__tick()
		pygame.display.flip()
		Window_time.tick(Window__tickrate)
	pygame.display.quit()
	pygame.quit()



def Window_stop():
	"""
	Termine l'instance
	"""
	global Window__done
	Window__done = True



def Window__handle_events():
	"""
	Prend tout les évenements pygame et fait trois choses :
	- gère et execute la fonction singleKey et repeatKey
	- gère les mises à jours de taille de l'écran
	- gère la fermeture de la fenêtre
	"""
	global Window_repeatKeyMap, Window_mouse_position

	for event in pygame.event.get():
		match event.type:
			case pygame.QUIT:
				Window_stop()

			case pygame.KEYDOWN:
				Window__singleKey(event.key)
				Window_repeatKeyMap[event.key] = True
			
			case pygame.KEYUP:
				Window_repeatKeyMap[event.key] = False

			case pygame.MOUSEMOTION:
				Window_mouse_position = event.pos

			case pygame.WINDOWRESIZED:
				Window__update_resolution((event.x, event.y))
				
			case pygame.WINDOWSIZECHANGED:
				Window__update_resolution((event.x, event.y))

			case _:
				pass
						
		Window__handleEvent(event)

	for (key, is_pressed) in Window_repeatKeyMap.items():
		if not is_pressed:
			continue
		Window__repeatKey(key)



def Window__update_resolution(coord):
	"""
	Set les variables de résolutions après une mise à jour.
	"""
	global Window_half_resolution, Window_resolution
	Window_resolution = coord
	Window_half_resolution = (
		int(Window_resolution[0] / 2),
		int(Window_resolution[1] / 2),
	)


def Window__update_window():
	"""
	Crée l'instance Surface pygame en fonction de si c'est en plein écran ou
	en fenêtré.
	"""
	global Window_inst
	if (Window__is_fullscreen):
		Window_inst = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.NOFRAME)
	else:
		Window_inst = pygame.display.set_mode(Window_resolution, pygame.RESIZABLE)



def Window_toggleFullscreen():
	"""
	active ou désactive le plein écran.
	"""
	global Window__windowed_resolution, Window_resolution, Window__is_fullscreen
	if (not Window__is_fullscreen):
		Window__windowed_resolution = Window_resolution
	else:
		Window_resolution = Window__windowed_resolution
	Window__is_fullscreen = not Window__is_fullscreen
	Window__update_window()

 

 		



def model_Plant_init(type: int, position: model_Plant_coord) -> model_Plant_types:
	return {
		"type": type,
		"position": position,
		"xp": 0,
		"generated": 0
	}

def model_Plant_type(tile: model_Plant_types) -> int:
	return tile["type"]

def model_Plant_position(tile: model_Plant_types) -> model_Plant_coord:
	return tile["position"]

def model_Plant_xp(tile: model_Plant_types) -> int:
	return tile["xp"]

def model_Plant_generated(tile: model_Plant_types) -> int:
	return tile["generated"]

def model_plants_init() -> Dict[utils_myTyping_coord_i, model_Plant_types]:
	return {}

def model_plants_get(coord: utils_myTyping_coord_i) -> model_Plant_types | None:
	global model_plants_map
	return model_plants_map.get(coord)

def model_plants_add(tile: model_Plant_types):
	global model_plants_map
	if model_plants_get(model_Plant_position(tile)):
		raise ValueError('Cannot add two tile on the same space')
	model_plants_map[model_Plant_position(tile)] = tile

# action by the player to remove an industry from the map
def model_plants_remove(coord: utils_myTyping_coord_i):
	global model_plants_map
	model_plants_map.pop(coord)

def model_plants_tile_is_empty(coord: utils_myTyping_coord_i):
	tile = model_plants_get(coord)
	if not tile:
		return True
	return model_Plant_type(tile) == model_technologies_INDUSTRY_NONE

def model_plants__can_place_on_terrain(terrain, technology):
	for can_place in technology['place_on']: 
		can_place_id: int = can_place['id']
		match can_place['type']:
			case 2:
				if model_terrain_terrainTile_type(terrain) == can_place_id:
					return True
			case 1:
				ressource = model_terrain_terrainTile_ressource(terrain)
				if not ressource:
					continue
				can_place = can_place_id
				if model_terrain_ressource_type(ressource) == can_place_id:
					return True
			case _:
				raise 'Invalid Technology'
	return False

# action by the player to place a new industry on the map
def model_plants_place(industry_id, position):
	if not position or model_plants_get(position) != None:
		return
	
	terrain = model_terrain_terrain_get_terrain_tile(position)
	technology = model_technologies_get_data(industry_id)

	if model_plants__can_place_on_terrain(terrain, technology)\
		and model_market_wallet_has_money(technology['price']):
		model_market_wallet_buy2(technology['price'])
		model_plants_add(model_Plant_init(industry_id, position))

def plant_add_experience(tile, amount):
	tile['xp'] += 1
	tile['generated'] += amount

model_plants_map = model_plants_init()


model_technologies_INDUSTRY_NONE 							= 0
model_technologies_INDUSTRY_FISHINGBOAT						= 1
model_technologies_INDUSTRY_SALTEXTRACTION					= 2
model_technologies_INDUSTRY_WHEAT_FIELDS					= 3
model_technologies_INDUSTRY_POTATO_FIELDS					= 4
model_technologies_INDUSTRY_COTTON_FIELDS					= 5
model_technologies_INDUSTRY_RICE_FIELDS						= 6
model_technologies_INDUSTRY_FURHUNTINGGROUNDS				= 7
model_technologies_INDUSTRY_LUMBERMILL						= 8
model_technologies_INDUSTRY_OILWELL							= 9
model_technologies_INDUSTRY_COALMINE						= 10
model_technologies_INDUSTRY_IRONMINE						= 11
model_technologies_INDUSTRY_COPPERMINE						= 12
model_technologies_INDUSTRY_PRECIOUSMETALMINE				= 13
model_technologies_INDUSTRY_RAREMETALMINE					= 14
model_technologies_INDUSTRY_BREADFACTORY					= 15
model_technologies_INDUSTRY_ALCOHOLFACTORY					= 16
model_technologies_INDUSTRY_SUSHIFACTORY					= 17
model_technologies_INDUSTRY_TEXTILEFACTORY					= 18
model_technologies_INDUSTRY_CLOTHESFACTORY					= 19
model_technologies_INDUSTRY_FURNITUREFACTORY				= 20
model_technologies_INDUSTRY_STEELMILL						= 21
model_technologies_INDUSTRY_TOOLINGFACTORY					= 22
model_technologies_INDUSTRY_CEMENTFACTORY					= 23
model_technologies_INDUSTRY_REFINARY						= 24
model_technologies_INDUSTRY_PLASTICFACTORY					= 25
model_technologies_INDUSTRY_GLASSFACTORY					= 26
model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	= 27
model_technologies_INDUSTRY_RADIOFACTORY					= 28
model_technologies_INDUSTRY_COMPUTERFACTORY					= 29
model_technologies_INDUSTRY_GUNFACTORY						= 30
model_technologies_INDUSTRY_ENGINEFACTORY					= 31
model_technologies_INDUSTRY_CARFACTORY						= 32
model_technologies_INDUSTRY_PLANESFACTORY					= 33
model_technologies_INDUSTRY_JEWELRYWORKSHOP					= 34
model_technologies_INDUSTRY_PHONEFACTORY					= 35
model_technologies_INDUSTRY_STONEQUERY						= 36
model_technologies_INDUSTRY_SANDQUERY						= 37

model_technologies_INDUSTRY_FISHINGBOAT_PRICE					= 10
model_technologies_INDUSTRY_SALTEXTRACTION_PRICE				= 60
model_technologies_INDUSTRY_WHEAT_FIELDS_PRICE					= 10
model_technologies_INDUSTRY_POTATO_FIELDS_PRICE					= 40
model_technologies_INDUSTRY_COTTON_FIELDS_PRICE					= 40
model_technologies_INDUSTRY_RICE_FIELDS_PRICE					= 60
model_technologies_INDUSTRY_FURHUNTINGGROUNDS_PRICE				= 1000
model_technologies_INDUSTRY_LUMBERMILL_PRICE					= 10
model_technologies_INDUSTRY_STONEQUERY_PRICE					= 20
model_technologies_INDUSTRY_SANDQUERY_PRICE						= 40
model_technologies_INDUSTRY_OILWELL_PRICE						= 110
model_technologies_INDUSTRY_COALMINE_PRICE						= 50
model_technologies_INDUSTRY_IRONMINE_PRICE						= 70
model_technologies_INDUSTRY_COPPERMINE_PRICE					= 70
model_technologies_INDUSTRY_PRECIOUSMETALMINE_PRICE				= 3000
model_technologies_INDUSTRY_RAREMETALMINE_PRICE					= 2500
model_technologies_INDUSTRY_BREADFACTORY_PRICE					= 50
model_technologies_INDUSTRY_ALCOHOLFACTORY_PRICE				= 100
model_technologies_INDUSTRY_SUSHIFACTORY_PRICE					= 110
model_technologies_INDUSTRY_TEXTILEFACTORY_PRICE				= 60
model_technologies_INDUSTRY_CLOTHESFACTORY_PRICE				= 80
model_technologies_INDUSTRY_FURNITUREFACTORY_PRICE				= 80
model_technologies_INDUSTRY_STEELMILL_PRICE						= 100
model_technologies_INDUSTRY_TOOLINGFACTORY_PRICE				= 1000
model_technologies_INDUSTRY_CEMENTFACTORY_PRICE					= 70
model_technologies_INDUSTRY_REFINARY_PRICE						= 1000
model_technologies_INDUSTRY_PLASTICFACTORY_PRICE				= 10000
model_technologies_INDUSTRY_GLASSFACTORY_PRICE					= 70
model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY_PRICE	= 30000
model_technologies_INDUSTRY_RADIOFACTORY_PRICE					= 1500
model_technologies_INDUSTRY_COMPUTERFACTORY_PRICE				= 150000
model_technologies_INDUSTRY_GUNFACTORY_PRICE					= 20000
model_technologies_INDUSTRY_ENGINEFACTORY_PRICE					= 30000
model_technologies_INDUSTRY_CARFACTORY_PRICE					= 50000
model_technologies_INDUSTRY_PLANESFACTORY_PRICE					= 500000
model_technologies_INDUSTRY_JEWELRYWORKSHOP_PRICE				= 5000
model_technologies_INDUSTRY_PHONEFACTORY_PRICE					= 300000

model_technologies_PLACE_ON_RESSOURCE = 1
model_technologies_PLACE_ON_TERRAIN = 2

model_technologies_industry_type = Dict[str, List[int] | int | List[Dict[str, int]]]

model_technologies_industry: Dict[int, model_technologies_industry_type] = {
	model_technologies_INDUSTRY_FISHINGBOAT: {
		'input': [],
		'output': model_market_goods_GOODS_FISH,
		'price': model_technologies_INDUSTRY_FISHINGBOAT_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_FISH, },
		],
	},
	model_technologies_INDUSTRY_SALTEXTRACTION: {
		'input': [],
		'output': model_market_goods_GOODS_SALT,
		'price': model_technologies_INDUSTRY_SALTEXTRACTION_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_SALT, },
		],
	},
	model_technologies_INDUSTRY_WHEAT_FIELDS: {
		'input': [],
		'output': model_market_goods_GOODS_WHEAT,
		'price': model_technologies_INDUSTRY_WHEAT_FIELDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_FERTILE_LAND, },
		],
	},
	model_technologies_INDUSTRY_POTATO_FIELDS: {
		'input': [],
		'output': model_market_goods_GOODS_POTATO,
		'price': model_technologies_INDUSTRY_POTATO_FIELDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_FERTILE_LAND, },
		],
	},
	model_technologies_INDUSTRY_COTTON_FIELDS: {
		'input': [],
		'output': model_market_goods_GOODS_COTTON,
		'price': model_technologies_INDUSTRY_COTTON_FIELDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_FERTILE_LAND, },
		],
	},
	model_technologies_INDUSTRY_RICE_FIELDS: {
		'input': [],
		'output': model_market_goods_GOODS_RICE,
		'price': model_technologies_INDUSTRY_RICE_FIELDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_FERTILE_LAND, },
		],
	},
	model_technologies_INDUSTRY_FURHUNTINGGROUNDS: {
		'input': [],
		'output': model_market_goods_GOODS_FUR,
		'price': model_technologies_INDUSTRY_FURHUNTINGGROUNDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_HUNTING_GROUNDS, },
		],
	},
	model_technologies_INDUSTRY_LUMBERMILL: {
		'input': [],
		'output': model_market_goods_GOODS_WOOD,
		'price': model_technologies_INDUSTRY_LUMBERMILL_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_WOOD, },
		],
	},
	model_technologies_INDUSTRY_OILWELL: {
		'input': [],
		'output': model_market_goods_GOODS_OIL,
		'price': model_technologies_INDUSTRY_OILWELL_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_OIL, },
		],
	},
	model_technologies_INDUSTRY_STONEQUERY: {
		'input': [],
		'output': model_market_goods_GOODS_STONE,
		'price': model_technologies_INDUSTRY_STONEQUERY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_STONE, },
		],
	},
	model_technologies_INDUSTRY_SANDQUERY: {
		'input': [],
		'output': model_market_goods_GOODS_SAND,
		'price': model_technologies_INDUSTRY_SANDQUERY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_SAND, },
		],
	},
	model_technologies_INDUSTRY_COALMINE: {
		'input': [],
		'output': model_market_goods_GOODS_COAL,
		'price': model_technologies_INDUSTRY_COALMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_COAL, },
		],
	},
	model_technologies_INDUSTRY_IRONMINE: {
		'input': [],
		'output': model_market_goods_GOODS_IRON,
		'price': model_technologies_INDUSTRY_IRONMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_IRON, },
		],
	},
	model_technologies_INDUSTRY_COPPERMINE: {
		'input': [],
		'output': model_market_goods_GOODS_COPPER,
		'price': model_technologies_INDUSTRY_COPPERMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_COPPER, },
		],
	},
	model_technologies_INDUSTRY_PRECIOUSMETALMINE: {
		'input': [],
		'output': model_market_goods_GOODS_PRECIOUS_METAL,
		'price': model_technologies_INDUSTRY_PRECIOUSMETALMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_PRECIOUS_METALS, },
		],
	},
	model_technologies_INDUSTRY_RAREMETALMINE: {
		'input': [],
		'output': model_market_goods_GOODS_RARE_METAL,
		'price': model_technologies_INDUSTRY_RAREMETALMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': model_terrain_ressource_RESSOURCE_RARE_METALS, },
		],
	},
	model_technologies_INDUSTRY_BREADFACTORY: {
		'input': [
			model_market_goods_GOODS_WHEAT,
		],
		'output': model_market_goods_GOODS_BREAD,
		'price': model_technologies_INDUSTRY_BREADFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_ALCOHOLFACTORY: {
		'input': [
			model_market_goods_GOODS_POTATO,
		],
		'output': model_market_goods_GOODS_ALCOHOL,
		'price': model_technologies_INDUSTRY_ALCOHOLFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_SUSHIFACTORY: {
		'input': [
			model_market_goods_GOODS_RICE,
			model_market_goods_GOODS_SALT,
			model_market_goods_GOODS_FISH,
		],
		'output': model_market_goods_GOODS_SUSHI,
		'price': model_technologies_INDUSTRY_SUSHIFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_TEXTILEFACTORY: {
		'input': [
			model_market_goods_GOODS_COTTON,
		],
		'output': model_market_goods_GOODS_TEXTILE,
		'price': model_technologies_INDUSTRY_TEXTILEFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_CLOTHESFACTORY: {
		'input': [
			model_market_goods_GOODS_TEXTILE,
		],
		'output': model_market_goods_GOODS_CLOTHES,
		'price': model_technologies_INDUSTRY_CLOTHESFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_FURNITUREFACTORY: {
		'input': [
			model_market_goods_GOODS_WOOD,
			model_market_goods_GOODS_IRON,
		],
		'output': model_market_goods_GOODS_FURNITURE,
		'price': model_technologies_INDUSTRY_FURNITUREFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_STEELMILL: {
		'input': [
			model_market_goods_GOODS_COAL,
			model_market_goods_GOODS_IRON,
		],
		'output': model_market_goods_GOODS_STEEL,
		'price': model_technologies_INDUSTRY_STEELMILL_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_TOOLINGFACTORY: {
		'input': [
			model_market_goods_GOODS_STEEL,
			model_market_goods_GOODS_WOOD,
		],
		'output': model_market_goods_GOODS_TOOLS,
		'price': model_technologies_INDUSTRY_TOOLINGFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_CEMENTFACTORY: {
		'input': [
			model_market_goods_GOODS_STONE,
			model_market_goods_GOODS_SAND,
		],
		'output': model_market_goods_GOODS_CEMENT,
		'price': model_technologies_INDUSTRY_CEMENTFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_REFINARY: {
		'input': [
			model_market_goods_GOODS_OIL,
		],
		'output': model_market_goods_GOODS_FUEL,
		'price': model_technologies_INDUSTRY_REFINARY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_PLASTICFACTORY: {
		'input': [
			model_market_goods_GOODS_FUEL,
		],
		'output': model_market_goods_GOODS_PLASTIC,
		'price': model_technologies_INDUSTRY_PLASTICFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_GLASSFACTORY: {
		'input': [
			model_market_goods_GOODS_SAND,
		],
		'output': model_market_goods_GOODS_GLASS,
		'price': model_technologies_INDUSTRY_GLASSFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY: {
		'input': [
			model_market_goods_GOODS_COPPER,
			model_market_goods_GOODS_RARE_METAL,
		],
		'output': model_market_goods_GOODS_ELECTRONICS_COMPONENT,
		'price': model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_RADIOFACTORY: {
		'input': [
			model_market_goods_GOODS_COPPER,
			model_market_goods_GOODS_STEEL,
		],
		'output': model_market_goods_GOODS_RADIO,
		'price': model_technologies_INDUSTRY_RADIOFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_COMPUTERFACTORY: {
		'input': [
			model_market_goods_GOODS_ELECTRONICS_COMPONENT,
			model_market_goods_GOODS_STEEL,
		],
		'output': model_market_goods_GOODS_COMPUTER,
		'price': model_technologies_INDUSTRY_COMPUTERFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_GUNFACTORY: {
		'input': [
			model_market_goods_GOODS_STEEL,
		],
		'output': model_market_goods_GOODS_GUNS,
		'price': model_technologies_INDUSTRY_GUNFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_ENGINEFACTORY: {
		'input': [
			model_market_goods_GOODS_STEEL,
			model_market_goods_GOODS_FUEL,
		],
		'output': model_market_goods_GOODS_ENGINE,
		'price': model_technologies_INDUSTRY_ENGINEFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_CARFACTORY: {
		'input': [
			model_market_goods_GOODS_ENGINE,
			model_market_goods_GOODS_STEEL,
			model_market_goods_GOODS_GLASS
		],
		'output': model_market_goods_GOODS_CAR,
		'price': model_technologies_INDUSTRY_CARFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_PLANESFACTORY: {
		'input': [
			model_market_goods_GOODS_RADIO,
			model_market_goods_GOODS_STEEL,
			model_market_goods_GOODS_GLASS,
			model_market_goods_GOODS_ENGINE,
		],
		'output': model_market_goods_GOODS_PLANES,
		'price': model_technologies_INDUSTRY_PLANESFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_JEWELRYWORKSHOP: {
		'input': [
			model_market_goods_GOODS_PRECIOUS_METAL
		],
		'output': model_market_goods_GOODS_JEWELRY,
		'price': model_technologies_INDUSTRY_JEWELRYWORKSHOP_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_PHONEFACTORY: {
		'input': [
			model_market_goods_GOODS_COMPUTER,
			model_market_goods_GOODS_PLASTIC,
			model_market_goods_GOODS_GLASS,
		],
		'output': model_market_goods_GOODS_PHONE,
		'price': model_technologies_INDUSTRY_PHONEFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
}

def model_technologies_get_data(type: int) -> model_technologies_industry_type:
	return model_technologies_industry[type]

model_technologyTree_default_unlocked = [
	model_technologies_INDUSTRY_WHEAT_FIELDS,
	model_technologies_INDUSTRY_FISHINGBOAT,
	model_technologies_INDUSTRY_LUMBERMILL,
	model_technologies_INDUSTRY_STONEQUERY,
]

model_technologyTree_techTree = techTree = [
	{
		"name": "Food",
		"techs": [
			{
				"name": "Food 1",
				"cost": 100,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_POTATO_FIELDS,
					model_technologies_INDUSTRY_BREADFACTORY,
				]
			},
			{
				"name": "Food 2",
				"cost": 250,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_SALTEXTRACTION,
					model_technologies_INDUSTRY_RICE_FIELDS,
				]
			},
			{
				"name": "Food 3",
				"cost": 750,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_SUSHIFACTORY,
					model_technologies_INDUSTRY_ALCOHOLFACTORY,
				]
			},
		]
	},
	{
		"name": "Process",
		"techs": [
			{
				"name": "Process 1",
				"cost": 100,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_COTTON_FIELDS,
					model_technologies_INDUSTRY_SANDQUERY,
				]
			},
			{
				"name": "Process 2",
				"cost": 250,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_TEXTILEFACTORY,
					model_technologies_INDUSTRY_FURNITUREFACTORY,
					model_technologies_INDUSTRY_CEMENTFACTORY,
				]
			},
			{
				"name": "Process 3",
				"cost": 500,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_CLOTHESFACTORY,
					model_technologies_INDUSTRY_GLASSFACTORY,
				]
			},
		]
	},
	{
		"name": "Metalurgy",
		"techs": [
			{
				"name": "Metalurgy 1",
				"cost": 150,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_COALMINE,
				]
			},
			{
				"name": "Metalurgy 2",
				"cost": 500,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_IRONMINE,
					model_technologies_INDUSTRY_COPPERMINE,
				]
			},
			{
				"name": "Metalurgy 3",
				"cost": 5000,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_PRECIOUSMETALMINE,
					model_technologies_INDUSTRY_RAREMETALMINE,
					model_technologies_INDUSTRY_JEWELRYWORKSHOP,
				]
			},
		]
	},
	{
		"name": "Advanced",
		"techs": [
			{
				"name": "Advanced 1",
				"cost": 750,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_STEELMILL,
				]
			},
			{
				"name": "Advanced 2",
				"cost": 1000,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_OILWELL,
				]
			},
			{
				"name": "Advanced 3",
				"cost": 3000,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_REFINARY,
					model_technologies_INDUSTRY_RADIOFACTORY,
				]
			},
			{
				"name": "Advanced 4",
				"cost": 10000,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_PLASTICFACTORY,
					model_technologies_INDUSTRY_GUNFACTORY,
				]
			},
			{
				"name": "Advanced 5",
				"cost": 50000,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY,
					model_technologies_INDUSTRY_ENGINEFACTORY,
					model_technologies_INDUSTRY_CARFACTORY,
				]
			},
			{
				"name": "Advanced 6",
				"cost": 100000,
				"unlocked": False,
				"unlocks": [
					model_technologies_INDUSTRY_COMPUTERFACTORY,
					model_technologies_INDUSTRY_PLANESFACTORY,
					model_technologies_INDUSTRY_PHONEFACTORY,
				]
			},
		]
	},
]

# action by player to unlock a technology
def model_technologyTree_add_tech(i, j):
	global model_market_wallet_science
	# TODO add check if player has enough science points
	j = j if i < len(model_technologyTree_techTree) else j + 3
	i = i if i < len(model_technologyTree_techTree) else len(model_technologyTree_techTree) - 1
	tech = model_technologyTree_techTree[i]['techs'][j]
	if tech['unlocked']:
		return
	if model_market_wallet_science < tech['cost']:
		return
	if j != 0 and not model_technologyTree_techTree[i]['techs'][j - 1]['unlocked']:
		return
	model_market_wallet_science -= tech['cost']
	tech['unlocked'] = True

def model_technologyTree_get_unlocked_techs():
	return [
		tech
			for tree in model_technologyTree_techTree
			for tech in tree['techs'] if tech['unlocked']
	]

def model_technologyTree_get_unlocked_buildings():
	return [
		*model_technologyTree_default_unlocked,
		*(unlock
			for tree in model_technologyTree_techTree
			for tech in tree['techs'] if tech['unlocked']
			for unlock in tech['unlocks']
		)
	]

def model_technologyTree_get_tech_for_draw(i, j):
	j = j if i < len(model_technologyTree_techTree) else j + 3
	i = i if i < len(model_technologyTree_techTree) else len(model_technologyTree_techTree) - 1
	return model_technologyTree_techTree[i]['techs'][j]


def model_technologyTree_get_placable_on(coord):
	if not coord:
		return []
	unlocked = model_technologyTree_get_unlocked_buildings()
	terrain = model_terrain_terrain_get_terrain_tile(coord)
	ressource = model_terrain_terrainTile_ressource(terrain)
	
	res = []
	for indus in model_technologies_industry:
		if not indus in unlocked:
			continue
		test_ind = model_technologies_industry[indus]
		for place_on in test_ind['place_on']:
			if place_on['type'] == model_technologies_PLACE_ON_RESSOURCE:
				if ressource and place_on['id'] == model_terrain_ressource_type(ressource):
					res.append(indus)
			elif place_on['type'] == model_technologies_PLACE_ON_TERRAIN:
				if place_on['id'] == model_terrain_terrainTile_type(terrain):
					res.append(indus)
	return res

def model_market_goods_print_goods(type):
	if type == model_market_goods_GOODS_FISH:
		return 'fish'
	elif type == model_market_goods_GOODS_SALT:
		return 'salt'
	elif type == model_market_goods_GOODS_WHEAT:
		return 'wheat'
	elif type == model_market_goods_GOODS_POTATO:
		return 'potato'
	elif type == model_market_goods_GOODS_COTTON:
		return 'cotton'
	elif type == model_market_goods_GOODS_RICE:
		return 'rice'
	elif type == model_market_goods_GOODS_FUR:
		return 'fur'
	elif type == model_market_goods_GOODS_WOOD:
		return 'wood'
	elif type == model_market_goods_GOODS_OIL:
		return 'oil'
	elif type == model_market_goods_GOODS_COAL:
		return 'coal'
	elif type == model_market_goods_GOODS_IRON:
		return 'iron'
	elif type == model_market_goods_GOODS_COPPER:
		return 'copper'
	elif type == model_market_goods_GOODS_PRECIOUS_METAL:
		return 'precious metal'
	elif type == model_market_goods_GOODS_RARE_METAL:
		return 'rare metal'
	elif type == model_market_goods_GOODS_BREAD:
		return 'bread'
	elif type == model_market_goods_GOODS_ALCOHOL:
		return 'alcohol'
	elif type == model_market_goods_GOODS_SUSHI:
		return 'sushi'
	elif type == model_market_goods_GOODS_TEXTILE:
		return 'textile'
	elif type == model_market_goods_GOODS_CLOTHES:
		return 'clothes'
	elif type == model_market_goods_GOODS_FURNITURE:
		return 'furniture'
	elif type == model_market_goods_GOODS_STEEL:
		return 'steel'
	elif type == model_market_goods_GOODS_TOOLS:
		return 'tools'
	elif type == model_market_goods_GOODS_CEMENT:
		return 'cement'
	elif type == model_market_goods_GOODS_FUEL:
		return 'fuel'
	elif type == model_market_goods_GOODS_PLASTIC:
		return 'plastic'
	elif type == model_market_goods_GOODS_GLASS:
		return 'glass'
	elif type == model_market_goods_GOODS_ELECTRONICS_COMPONENT:
		return 'electronics component'
	elif type == model_market_goods_GOODS_RADIO:
		return 'radio'
	elif type == model_market_goods_GOODS_COMPUTER:
		return 'computer'
	elif type == model_market_goods_GOODS_GUNS:
		return 'guns'
	elif type == model_market_goods_GOODS_ENGINE:
		return 'engine'
	elif type == model_market_goods_GOODS_CAR:
		return 'car'
	elif type == model_market_goods_GOODS_PLANES:
		return 'planes'
	elif type == model_market_goods_GOODS_JEWELRY:
		return 'jewelry'
	elif type == model_market_goods_GOODS_PHONE:
		return 'phone'
	elif type == model_market_goods_GOODS_STONE:
		return 'stone'
	elif type == model_market_goods_GOODS_SAND:
		return 'sand'
	else:
		return 'unknown'
	
def model_market_tick_market_tick():
	for plant in sorted(model_plants_map.values(), key=lambda item: model_Plant_type(item)):
		model_market_tick_industry_tick(plant)
	model_market_stockpile_sell_stock_to_market()

def model_market_tick_industry_tick(tile):
	model_market_tick_generate_goods(tile)

def model_market_tick_generate_goods(tile, amount = 1):
	global model_market_wallet_science
	techno = model_technologies_industry[model_Plant_type(tile)]

	for input in techno['input']:
		model_market_stockpile_buy_stock(input, amount)
	model_market_stockpile_add_stock(techno['output'], amount)

	tile['generated'] += amount

	if tile['generated'] % 100 == 0:
		model_market_wallet_science += 1

model_market_market_TAXE = 0.9

model_market_market_market = {
	# name								   price		lot_size
	model_market_goods_GOODS_FISH					: (1,			60),
	model_market_goods_GOODS_SALT					: (4,			20),
	model_market_goods_GOODS_WHEAT					: (1,			60),
	model_market_goods_GOODS_POTATO					: (2,			28),
	model_market_goods_GOODS_COTTON					: (2,			30),
	model_market_goods_GOODS_RICE					: (2,			15),
	model_market_goods_GOODS_FUR						: (3,			100),
	model_market_goods_GOODS_WOOD					: (1,			60),
	model_market_goods_GOODS_STONE					: (1,			26),
	model_market_goods_GOODS_SAND					: (2,			30),
	model_market_goods_GOODS_OIL						: (7,			100),
	model_market_goods_GOODS_COAL					: (4,			20),
	model_market_goods_GOODS_IRON					: (22,			20),
	model_market_goods_GOODS_COPPER					: (25,			20),
	model_market_goods_GOODS_PRECIOUS_METAL			: (2700,		20),
	model_market_goods_GOODS_RARE_METAL				: (130,			20),
	model_market_goods_GOODS_BREAD					: (2,			15),
	model_market_goods_GOODS_ALCOHOL					: (35,			20),
	model_market_goods_GOODS_SUSHI					: (30,			20),
	model_market_goods_GOODS_TEXTILE					: (4,			30),
	model_market_goods_GOODS_CLOTHES					: (8,			100),
	model_market_goods_GOODS_FURNITURE				: (9,			100),
	model_market_goods_GOODS_STEEL					: (13,			100),
	model_market_goods_GOODS_TOOLS					: (15,			100),
	model_market_goods_GOODS_CEMENT					: (4,			100),
	model_market_goods_GOODS_FUEL					: (9,			100),
	model_market_goods_GOODS_PLASTIC					: (11,			100),
	model_market_goods_GOODS_GLASS					: (3,			100),
	model_market_goods_GOODS_ELECTRONICS_COMPONENT	: (22,			100),
	model_market_goods_GOODS_RADIO					: (21,			100),
	model_market_goods_GOODS_COMPUTER				: (37,			100),
	model_market_goods_GOODS_GUNS					: (15,			100),
	model_market_goods_GOODS_ENGINE					: (2000,		100),
	model_market_goods_GOODS_CAR						: (10000,		100),
	model_market_goods_GOODS_PLANES					: (100000,		10),
	model_market_goods_GOODS_JEWELRY					: (10000,		100),
	model_market_goods_GOODS_PHONE					: (20000,		1),
}

def model_market_market_get_price(goods_type):
	return model_market_market_market[goods_type][0]

def model_market_market_get_bundle_size(goods_type):
	return model_market_market_market[goods_type][1]

def model_market_market_sell_market(goods_type, amounts):
	# print('sell', amounts, 'de', model_market_goods_print_goods(goods_type), 'au prix de', int(model_market_market_get_price(goods_type) * model_market_market_TAXE))
	model_market_wallet_sell(int(model_market_market_get_price(goods_type) * model_market_market_TAXE * amounts + 1))

def model_market_market_buy_market(goods_type, amounts):
	# print('buy', amounts, 'de', model_market_goods_print_goods(goods_type), 'au prix de', model_market_market_market[goods_type])
	model_market_wallet_buy(int(model_market_market_get_price(goods_type) * amounts))

model_market_wallet_money = 10
model_market_wallet_money_incr = 0
model_market_wallet_science = 0
model_market_wallet_science_incr = 0

def model_market_wallet_has_money(price):
	return model_market_wallet_money >= price

def model_market_wallet_buy(price):
	global model_market_wallet_money, model_market_wallet_money_incr
	model_market_wallet_money -= price
	model_market_wallet_money_incr -= price

def model_market_wallet_buy2(price):
	global model_market_wallet_money
	model_market_wallet_money -= price

def model_market_wallet_sell(price):
	global model_market_wallet_money, model_market_wallet_money_incr
	model_market_wallet_money += price	
	model_market_wallet_money_incr += price

model_market_stockpile_stock = {}

def model_market_stockpile_get_stock(ressource_type):
	return model_market_stockpile_stock.get(
		ressource_type,
		0
	)

def model_market_stockpile_add_stock(ressource_type, amount):
	global model_market_stockpile_stock
	if not ressource_type in model_market_stockpile_stock:
		model_market_stockpile_stock[ressource_type] = 0
	model_market_stockpile_stock[ressource_type] += amount

def model_market_stockpile_buy_stock(ressource_type, amount):
	global model_market_stockpile_stock
	if not ressource_type in model_market_stockpile_stock:
		model_market_stockpile_stock[ressource_type] = 0
	model_market_stockpile_stock[ressource_type] -= amount

original_money = model_market_wallet_money

def model_market_stockpile_sell_stock_to_market():
	global original_money, model_market_wallet_money_incr

	for s in model_market_stockpile_stock:
		if model_market_stockpile_stock[s] == 0:
			continue
		elif model_market_stockpile_stock[s] > 0:
			bundle_size = model_market_market_get_bundle_size(s)
			if model_market_stockpile_stock[s] // bundle_size > 0:
				num_bundle = model_market_stockpile_stock[s] // bundle_size
				model_market_stockpile_stock[s] = model_market_stockpile_stock[s] % bundle_size
				model_market_market_sell_market(s, num_bundle)
		else:
			model_market_market_buy_market(s, -model_market_stockpile_stock[s])
			model_market_stockpile_stock[s] = 0
	model_market_wallet_money_incr = model_market_wallet_money - original_money
	original_money = model_market_wallet_money

def model_stat_setup_get_money():
	global model_market_wallet_money_incr, model_market_wallet_money_incr
	res = model_market_wallet_money_incr
	model_market_wallet_money_incr = 0
	return res

def model_stat_setup_get_science():
	global model_market_wallet_science_incr, model_market_wallet_science_incr
	res = model_market_wallet_science_incr
	model_market_wallet_science_incr = 0
	return res

def model_stat_setup_average(data):
	if len(data) <= 0:
		return 0
	res = 0
	for elem in data:
		res += elem
	return res / len(data)

def model_stat_setup_setup_stats():
	model_stat_setup_add_stat(
		'money',
		model_stat_setup_get_money,
		lambda data: model_stat_setup_average(data)
	)
	model_stat_setup_add_stat(
		'science',
		model_stat_setup_get_science,
		lambda data: model_stat_setup_average(data)
	)


model_stat_setup_stats = {}

model_stat_setup_DELAY = 1000
model_stat_setup_STAT_RESET = 10

def model_stat_setup_add_stat(key, add, get):
	model_stat_setup_stats[key] = {
		"data": [],
		"add": add,
		"get": get,
	}


model_stat_setup_prev_time = 0
def model_stat_setup_stat_tick():
	global model_stat_setup_prev_time
	time = pygame.time.get_ticks()
	if model_stat_setup_prev_time + model_stat_setup_DELAY > time:
		return
	model_stat_setup_prev_time = time
	for key, elem in model_stat_setup_stats.items():
		if len(elem["data"]) >= model_stat_setup_STAT_RESET:
			elem["data"].remove(elem["data"][0])
		x = elem["add"]()
		elem["data"].append(x)


def model_stat_setup_get_stat(key):
	if key not in model_stat_setup_stats:
		return 0
	return model_stat_setup_stats[key]["get"](model_stat_setup_stats[key]["data"])


def model_terrain_ressource_init(type: int, richness: int, height: int) -> model_terrain_ressource_types:
	return {
		"type": type,
		"richness": 0,
		"height": height,
	}

def model_terrain_ressource_type(tile: model_terrain_ressource_types) -> int:
	return tile["type"] # type: ignore

def model_terrain_ressource_richness(tile: model_terrain_ressource_types) -> int:
	return tile["richness"] # type: ignore

def model_terrain_ressource_height(tile: model_terrain_ressource_types) -> int:
	return tile["height"] # type: ignore


model_terrain_seed_ITER = 100
model_terrain_seed_random_list: List[List[int | float]] = []
model_terrain_seed_prev_random_val = 0

def model_terrain_seed_get_seed():
	global model_terrain_seed_prev_random_val
	model_terrain_seed_prev_random_val = random.randint(0, 0x7fffffff)
	return model_terrain_seed_prev_random_val

def model_terrain_seed_load_seed():
	global model_terrain_seed_random_list

	model_terrain_seed_random_list = []
	for i in range(0, model_terrain_seed_ITER): # type: ignore
		model_terrain_seed_random_list.append([
			int(model_terrain_seed_random_lcg() * 7 + 1), # height
			1/int(model_terrain_seed_random_lcg() * 200 + 500), # width_x
			1/int(model_terrain_seed_random_lcg() * 200 + 500), # width_y
			int(model_terrain_seed_random_lcg() * 2 + 1), # height_around
			1/int(model_terrain_seed_random_lcg() * 20000 + 10000), # width_x_around
			1/int(model_terrain_seed_random_lcg() * 20000 + 10000), # width_y_around
			int(model_terrain_seed_random_lcg() * 400 - 200), # offset_x
			int(model_terrain_seed_random_lcg() * 400 - 200), # offset_y
		])

def model_terrain_seed__gausse(height: int, width_x: float, width_y: float, offset_x: int, offset_y: int, coordinates: utils_myTyping_coord_i):
	return height * math.pow(2, width_x * -math.pow(coordinates[0] + offset_x, 2) - width_y * math.pow(coordinates[1] + offset_y, 2))

def model_terrain_seed__gausse2d(coordinates: utils_myTyping_coord_i, random: List[int | float]):
	return model_terrain_seed__gausse(random[0], random[1], random[2], random[6], random[7], coordinates)\
		+ model_terrain_seed__gausse(random[3], random[4], random[5], random[6], random[7], coordinates)


def model_terrain_seed_get_height(coord: utils_myTyping_coord_i):
	global model_terrain_seed_random_list

	if coord[0] > 500 or coord[1] > 500 or coord[0] < -500 or coord[1] < -500:
		return -31

	res = 0
	for ran in model_terrain_seed_random_list:
		res += model_terrain_seed__gausse2d(coord, ran)
	res -= 32
	return int(res)


# Park & Miller constants for random number generator
model_terrain_seed_M = 0x7fffffff
model_terrain_seed_A = 48271

model_terrain_seed_NB_ITERATIONS = 10


# Type of linear congruential generator presented by D. H. lehmer
def model_terrain_seed_random_lcg():
	global model_terrain_seed_prev_random_val
	n = model_terrain_seed_prev_random_val % (model_terrain_seed_M - 1) + 1

	# Iteration with only x
	iteration = model_terrain_seed_NB_ITERATIONS
	while (iteration > 0):
		n = n * model_terrain_seed_A % model_terrain_seed_M
		iteration -= 1

	model_terrain_seed_prev_random_val = n
	return n / model_terrain_seed_M	


# Type of linear congruential generator presented by D. H. lehmer
# We use the x as the seed (x_0) for the first batch of
# iterations. After that, we use that result in combination with a XOR of it
# and y to be the seed of our second set of iterations.
# Thanks to Prof. Boigelot for the suggestion
def model_terrain_seed_random_lcg_coord(coord: utils_myTyping_coord_i):
    # Send all number to the interval ]0, M[
	x_val = coord[0] % (model_terrain_seed_M - 1) + 1
	
	# Iteration with only x
	iteration = model_terrain_seed_NB_ITERATIONS
	while (iteration > 0):
		x_val = x_val * model_terrain_seed_A % model_terrain_seed_M
		iteration -= 1
	
	y_val = x_val ^ coord[1]

	# Iteration with y
	iteration = model_terrain_seed_NB_ITERATIONS
	while (iteration > 0):
		y_val = y_val * model_terrain_seed_A % model_terrain_seed_M
		iteration -= 1

	# Return value between 0 and 1
	return y_val / model_terrain_seed_M



def model_terrain_terrain_init_random():
	random.seed()

	seed = model_terrain_seed_get_seed()
	# print(seed)
	model_terrain_seed_load_seed()

	# for i in range(-500 + 0, 500 + 0, 2):
	# 	for j in range(-500 + 0, 500 + 0, 2):
	# 		# print(i, j)
	# 		get_terrain_tile((i, j))
	# 	print(i)

@utils_cache_add_cache
def model_terrain_terrain_get_terrain_tile(coord: utils_myTyping_coord_i) -> model_terrain_terrainTile_types:
	height = model_terrain_seed_get_height(coord)
	
	if (height < -5):
		res = model_terrain_terrainTile_init(model_terrain_terrainTile_TERRAINTILETYPE_DEEPSEA, coord, height)
	elif (height < 0):
		res = model_terrain_terrainTile_init(model_terrain_terrainTile_TERRAINTILETYPE_SEA, coord, height)
	elif (height < 1):
		res = model_terrain_terrainTile_init(model_terrain_terrainTile_TERRAINTILETYPE_BEACH, coord, height)
	elif (height < 15):
		res = model_terrain_terrainTile_init(model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, coord, height)
	elif (height < 25):
		res = model_terrain_terrainTile_init(model_terrain_terrainTile_TERRAINTILETYPE_FOREST, coord, height)
	elif (height < 35):
		res = model_terrain_terrainTile_init(model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, coord, height)
	elif (height >= 35):
		res = model_terrain_terrainTile_init(model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_TOP, coord, height)
	else:
		raise ValueError("Terrain tile has height not possible")
	
	ressource = int(model_terrain_seed_random_lcg_coord(model_terrain_terrainTile_position(res)) * 100)
	richness = int(model_terrain_seed_random_lcg_coord(model_terrain_terrainTile_position(res)) * 100)
	res["ressource"] = model_terrain_terrain_generate_ressource(res, ressource, richness, height)
	return res	

def model_terrain_terrain_generate_ressource(tile: model_terrain_terrainTile_types, ressource: int, richness: int, height: int) -> model_terrain_ressource_types | None:
	match(model_terrain_terrainTile_type(tile)):
		case 1:
			match ressource:
				case 90:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_FISH, richness, height)
				case 95 | 96 | 97:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_FISH, richness, height)
				case _:
					pass
		case 2:
			match ressource:
				case 90 | 91 | 92 | 93 | 94:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_FISH, richness, height)
				case _:
					pass
		case 3:
			match ressource:
				case 1:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_SALT, richness, height)
				case 0:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_OIL, richness, height)
				case _:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_SAND, 1, height)
		case 4:
			if height == 9 or height == 10:
				return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_FERTILE_LAND, richness, height)
		case 5:
			return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_WOOD, richness % 5, height)
		case 6:
			match ressource:
				case 0:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_COAL, richness, height)
				case 1:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_IRON, richness, height)
				case 2:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_COPPER, richness, height)
				case _:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_STONE, richness % 5, height)
		case  7:
			match ressource:
				case 0:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_IRON, richness, height)
				case 1:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_PRECIOUS_METALS, richness, height)
				case 2:
					return model_terrain_ressource_init(model_terrain_ressource_RESSOURCE_RARE_METALS, richness, height)
				case _:
					pass
		case _:
			pass
	return None



def model_terrain_terrainTile_init(type: int, position: model_terrain_terrainTile_coord, height: int) -> model_terrain_terrainTile_types:
	return {
		"type": type,
		"position": position,
		"height": height,
		"ressource": None,
	}

def model_terrain_terrainTile_type(tile: model_terrain_terrainTile_types) -> int:
	return tile["type"]

def model_terrain_terrainTile_position(tile: model_terrain_terrainTile_types) -> model_terrain_terrainTile_coord:
	return tile["position"]

def model_terrain_terrainTile_height(tile: model_terrain_terrainTile_types) -> int:
	return tile["height"]

def model_terrain_terrainTile_ressource(tile: model_terrain_terrainTile_types) -> model_terrain_ressource_types | None:
	return tile["ressource"]

def model_gameTick_game_model_tick():
	if model_speed_can_execute_simulation():
		model_market_tick_market_tick()
		model_stat_setup_stat_tick()


__prev_val = 3
val = 3
tick_index = 0
_delta_tick_simation = 10

# action by the player to increase the speed of the simulation
def model_speed_increment():
	global val
	if val < 5:
		val += 1
		model_speed__update_tick_simulation()

# action by the player to decrease the speed of the simulation
def model_speed_decrement():
	global val
	if val > 1:
		val -= 1
		model_speed__update_tick_simulation()

# action by the player to set the speed of the simulation
def model_speed_set(new_speed: int):
	global val
	val = new_speed
	model_speed__update_tick_simulation()

# action by the player to pause the simulation
def model_speed_pause():
	global val, __prev_val
	if (val != 0):
		__prev_val = val
		val = 0
	else:
		val = __prev_val
	model_speed__update_tick_simulation()

def model_speed_can_execute_simulation():
	global tick_index
	tick_index += 1
	if (tick_index > _delta_tick_simation and menu == GestionMenu_MENU_JEU):
		tick_index = 0
		return True
	return False

def model_speed__update_tick_simulation():
	global _delta_tick_simation
	match val:
		case 0:
			_delta_tick_simation = math.inf
		case 1:
			_delta_tick_simation = 32
		case 2:
			_delta_tick_simation = 16
		case 3:
			_delta_tick_simation = 4
		case 4:
			_delta_tick_simation = 2
		case 5:
			_delta_tick_simation = 1
		case _:
			pass


emptyLambda = lambda: None

def ui_framework_framework_component(
	rect,
	margin=0,
	padding=0,
	z=0,
	draw=emptyLambda,
	click=emptyLambda,
	clickOutside=emptyLambda,
	childs=[]
):
	res = {
		'_rect': rect,
		'margin': margin,
		'padding': padding,
		'z': z,

		'_draw': draw,
		'_click': click,
		'_clickOutside': clickOutside,

		'_hidden': False,
		'_temp': False,

		'_parent': None,
		'_childs': childs,
	}

	for child in res['_childs']:
		ui_framework_framework_component_add_parent(child, res)
	return res
	
def ui_framework_framework_component_show(component):
	component['_hidden'] = False

def ui_framework_framework_component_hide(component):
	component['_hidden'] = True





def ui_framework_framework__component_baseRect(component, parent_rect):
	if callable(component['_rect']):
		if component['_parent'] and component['_rect'].__code__.co_argcount >= 1:
			return component['_rect'](parent_rect)
		else:
			return component['_rect']()
	else:
		return component['_rect']


def ui_framework_framework_component_rect(component):
	parent = ui_framework_framework_component_child_rect(component['_parent']) if component['_parent'] else ((0, 0), (0, 0))
	base = ui_framework_framework__component_baseRect(component, parent)
	# print('base',base, component)
	return (
		(
			parent[0][0] + base[0][0] + component['margin'],
			parent[0][1] + base[0][1] + component['margin'],
		),
		(
			base[1][0] - 2 * component['margin'],
			base[1][1] - 2 * component['margin'],
		),
	)

def ui_framework_framework_component_child_rect(component):
	parent = ui_framework_framework_component_child_rect(component['_parent']) if component['_parent'] else ((0, 0), (0, 0))
	base = ui_framework_framework__component_baseRect(component, parent)
	return (
		(
			parent[0][0] + base[0][0] + component['margin'] + component['padding'],
			parent[0][1] + base[0][1] + component['margin'] + component['padding'],
		),
		(
			base[1][0] - 2 * (component['padding'] + component['margin']),
			base[1][1] - 2 * (component['padding'] + component['margin']),
		),
	)
	






def ui_framework_framework_component_draw(component, mouse_position):
	if component['_hidden']:
		return	
	rect = ui_framework_framework_component_rect(component)
	if component['_draw'].__code__.co_argcount >= 2:
		component['_draw'](rect, ui_framework_framework_component_is_in(component, mouse_position))
	else:
		component['_draw'](rect)
	component['_childs'].sort(key=lambda c: c['z'])
	for child in component['_childs']:
		ui_framework_framework_component_draw(child, mouse_position)

def ui_framework_framework_component_is_in(component, pos):
	rect = ui_framework_framework_component_rect(component)
	return rect[0][0] <= pos[0] <= rect[0][0] + rect[1][0]\
		and rect[0][1] <= pos[1] <= rect[0][1] + rect[1][1]

def ui_framework_framework_component_click(component, pos, has_already_clicked=False):
	if component['_hidden']:
		return False
	component['_childs'].sort(key=lambda c: c['z'], reverse=True)
	for child in component['_childs']:
		if ui_framework_framework_component_click(child, pos, has_already_clicked):
			has_already_clicked = True
	if component['_click'] is not None and ui_framework_framework_component_is_in(component, pos):
		if has_already_clicked:
			return has_already_clicked
		has_already_clicked = True
		if component['_click'].__code__.co_argcount >= 1:
			component['_click'](pos)
		else:
			component['_click']()
	else:
		if component['_clickOutside'].__code__.co_argcount >= 1:
			component['_clickOutside'](pos)
		else:
			component['_clickOutside']()
	return has_already_clicked

def ui_framework_framework_component_add_parent(component, parent):
	component['_parent'] = parent






def ui_framework_framework_component_add_temp(component, new_childs):
	for child in new_childs:
		if not child:
			continue
		child['_temp'] = True
		component['_childs'].append(child)
		ui_framework_framework_component_add_parent(child, component)

def ui_framework_framework_component_temp_remove(component):
    component['_childs'] = [child for child in component['_childs'] if not child['_temp']]


ui_framework_draw_hover_cursor = (0, 0)

def ui_framework_draw_updateHoverCursor(pos):
	global ui_framework_draw_hover_cursor
	ui_framework_draw_hover_cursor = pos

def ui_framework_draw_drawRect(rect, color, rounding = 0, outline = 0, hover = None):
	global ui_framework_draw_hover_cursor
	if hover is not None and pygame.Rect(rect).collidepoint(ui_framework_draw_hover_cursor):
		color = hover
	else:
		color = color
	pygame.draw.rect(Window_inst, color, rect, outline, rounding)

def ui_framework_draw_drawCircle(center, radius, color, outline = 0):
	pygame.draw.circle(Window_inst, color, center, radius, outline)


def ui_common_centerTextButton(rect, font, message, color_background, rounding, color_hover = None):
	ui_framework_draw_drawRect(rect, color_background, rounding, hover=color_hover)
	ui_framework_text_drawText(font, (rect[0][0] + rect[1][0] // 2, rect[0][1] + rect[1][1] // 2), message, VC_TEXT, "center")

def ui_common_centerRightTextButton(rect, font, message, color_background, rounding, padding, color_hover = None):
	ui_framework_draw_drawRect(rect, color_background, rounding, hover=color_hover)
	ui_framework_text_drawText(font, (rect[0][0] + rect[1][0] - padding, rect[0][1] + rect[1][1] // 2), message, VC_TEXT, "midright")

def ui_common_centerLeftTextButton(rect, font, message, color_background, rounding, padding, color_hover = None):
	ui_framework_draw_drawRect(rect, color_background, rounding, hover=color_hover)
	ui_framework_text_drawText(font, (rect[0][0] + padding, rect[0][1] + rect[1][1] // 2), message, VC_TEXT, "midleft")

def ui_common_exit_button(rect):
	ui_framework_draw_drawRect(rect, VC_BACKGROUND3, VC_ROUNDING_HARD, hover=VC_PRIMARY)
	ui_framework_image_drawImage('exit', rect),

def ui_common_centerRightText(rect, font, message, padding, color):
	ui_framework_text_drawText(font, (rect[0][0] + rect[1][0] - padding, rect[0][1] + rect[1][1] // 2), message, color, "midright")




ui_map_goods_goodsMap = {
	model_market_goods_GOODS_FISH					: ('Fish'						, lambda rect: ui_framework_image_drawImage('good_fish', rect)),
	model_market_goods_GOODS_SALT					: ('Salt'						, lambda rect: ui_framework_image_drawImage('good_salt', rect)),
	model_market_goods_GOODS_WHEAT					: ('Wheat'						, lambda rect: ui_framework_image_drawImage('good_wheat', rect)),
	model_market_goods_GOODS_POTATO					: ('Potato'						, lambda rect: ui_framework_image_drawImage('good_potato', rect)),
	model_market_goods_GOODS_COTTON					: ('Cotton'						, lambda rect: ui_framework_image_drawImage('good_cotton', rect)),
	model_market_goods_GOODS_RICE					: ('Rice'						, lambda rect: ui_framework_image_drawImage('good_rice', rect)),
	model_market_goods_GOODS_FUR					: ('Fur'						, lambda rect: ui_framework_image_drawImage('good_fur', rect)),
	model_market_goods_GOODS_WOOD					: ('Wood'						, lambda rect: ui_framework_image_drawImage('good_wood', rect)),
	model_market_goods_GOODS_OIL					: ('Oil'						, lambda rect: ui_framework_image_drawImage('good_oil', rect)),
	model_market_goods_GOODS_COAL					: ('Coal'						, lambda rect: ui_framework_image_drawImage('good_coal', rect)),
	model_market_goods_GOODS_IRON					: ('Iron'						, lambda rect: ui_framework_image_drawImage('good_iron', rect)),
	model_market_goods_GOODS_COPPER					: ('Copper'						, lambda rect: ui_framework_image_drawImage('good_copper', rect)),
	model_market_goods_GOODS_PRECIOUS_METAL			: ('Precious Metal'				, lambda rect: ui_framework_image_drawImage('good_precious_metal', rect)),
	model_market_goods_GOODS_RARE_METAL				: ('Rare Metal'					, lambda rect: ui_framework_image_drawImage('good_rare_metal', rect)),
	model_market_goods_GOODS_BREAD					: ('Bread'						, lambda rect: ui_framework_image_drawImage('good_bread', rect)),
	model_market_goods_GOODS_ALCOHOL				: ('Alcohol'					, lambda rect: ui_framework_image_drawImage('good_alcohol', rect)),
	model_market_goods_GOODS_SUSHI					: ('Sushi'						, lambda rect: ui_framework_image_drawImage('good_sushi', rect)),
	model_market_goods_GOODS_TEXTILE				: ('Textile'					, lambda rect: ui_framework_image_drawImage('good_textile', rect)),
	model_market_goods_GOODS_CLOTHES				: ('Clothes'					, lambda rect: ui_framework_image_drawImage('good_clothes', rect)),
	model_market_goods_GOODS_FURNITURE				: ('Furniture'					, lambda rect: ui_framework_image_drawImage('good_furniture', rect)),
	model_market_goods_GOODS_STEEL					: ('Steel'						, lambda rect: ui_framework_image_drawImage('good_steel', rect)),
	model_market_goods_GOODS_TOOLS					: ('Tools'						, lambda rect: ui_framework_image_drawImage('good_tools', rect)),
	model_market_goods_GOODS_CEMENT					: ('Cement'						, lambda rect: ui_framework_image_drawImage('good_cement', rect)),	
	model_market_goods_GOODS_FUEL					: ('Fuel'						, lambda rect: ui_framework_image_drawImage('good_fuel', rect)),
	model_market_goods_GOODS_PLASTIC				: ('Plastic'					, lambda rect: ui_framework_image_drawImage('good_plastic', rect)),
	model_market_goods_GOODS_GLASS					: ('Glass'						, lambda rect: ui_framework_image_drawImage('good_glass', rect)),
	model_market_goods_GOODS_ELECTRONICS_COMPONENT	: ('Electronic Components'		, lambda rect: ui_framework_image_drawImage('good_electronics_component', rect)),
	model_market_goods_GOODS_RADIO					: ('Radio'						, lambda rect: ui_framework_image_drawImage('good_radio', rect)),
	model_market_goods_GOODS_COMPUTER				: ('Computer'					, lambda rect: ui_framework_image_drawImage('good_computer', rect)),
	model_market_goods_GOODS_GUNS					: ('Guns'						, lambda rect: ui_framework_image_drawImage('good_guns', rect)),
	model_market_goods_GOODS_ENGINE					: ('Engine'						, lambda rect: ui_framework_image_drawImage('good_engine', rect)),
	model_market_goods_GOODS_CAR					: ('Car'						, lambda rect: ui_framework_image_drawImage('good_car', rect)),
	model_market_goods_GOODS_PLANES					: ('Planes'						, lambda rect: ui_framework_image_drawImage('good_planes', rect)),
	model_market_goods_GOODS_JEWELRY				: ('Jewelry'					, lambda rect: ui_framework_image_drawImage('good_jewelry', rect)),
	model_market_goods_GOODS_PHONE					: ('Phone'						, lambda rect: ui_framework_image_drawImage('good_phone', rect)),
	model_market_goods_GOODS_STONE					: ('Stone'						, lambda rect: ui_framework_image_drawImage('good_stone', rect)),
	model_market_goods_GOODS_SAND					: ('Sand'						, lambda rect: ui_framework_image_drawImage('good_sand', rect)),
}

ui_map_goods_ressources_to_goods_map = {
	model_terrain_ressource_RESSOURCE_FISH           : [model_market_goods_GOODS_FISH],
	model_terrain_ressource_RESSOURCE_SALT           : [model_market_goods_GOODS_SALT],
	model_terrain_ressource_RESSOURCE_FERTILE_LAND   : [model_market_goods_GOODS_WHEAT, model_market_goods_GOODS_POTATO, model_market_goods_GOODS_COTTON, model_market_goods_GOODS_RICE],
	model_terrain_ressource_RESSOURCE_HUNTING_GROUNDS: [model_market_goods_GOODS_FUR],
	model_terrain_ressource_RESSOURCE_WOOD           : [model_market_goods_GOODS_WOOD],
	model_terrain_ressource_RESSOURCE_OIL            : [model_market_goods_GOODS_OIL],
	model_terrain_ressource_RESSOURCE_COAL           : [model_market_goods_GOODS_COAL],
	model_terrain_ressource_RESSOURCE_IRON           : [model_market_goods_GOODS_IRON],
	model_terrain_ressource_RESSOURCE_COPPER         : [model_market_goods_GOODS_COPPER],
	model_terrain_ressource_RESSOURCE_PRECIOUS_METALS: [model_market_goods_GOODS_PRECIOUS_METAL],
	model_terrain_ressource_RESSOURCE_RARE_METALS    : [model_market_goods_GOODS_RARE_METAL],
	model_terrain_ressource_RESSOURCE_SAND           : [model_market_goods_GOODS_SAND],
	model_terrain_ressource_RESSOURCE_STONE          : [model_market_goods_GOODS_STONE],
}
def ui_map_goods_ressources_to_goods(ressource_type):
	return ui_map_goods_ressources_to_goods_map.get(
		ressource_type,
		[]
	)

def ui_map_goods_print_goods(type):
	return ui_map_goods_goodsMap[type][0]

def ui_map_goods_draw_goods(type):
	return ui_map_goods_goodsMap.get(
		type,
		('', lambda rect: None)
	)[1]



ui_framework_image_images_loaded = {}

def ui_framework_image_loadImages(images):
	for key in images:
		ui_framework_image_images_loaded[key] = pygame.image.load(images[key]).convert_alpha(Window_inst)

def ui_framework_image_drawImage(image_key, rect):
	img_inst = ui_framework_image_images_loaded[image_key]
	img = pygame.transform.scale(img_inst, rect[1])
	Window_inst.blit(img, rect[0])


ui_framework_text_fonts = {}

def ui_framework_text_loadFont(id: str, name: str, size: int, bold: bool = False):
	ui_framework_text_fonts[id] = pygame.font.SysFont(name, size, bold)

def longNumber(number: int) -> str:
	if abs(number / (10 ** 12)) >= 1:
		return str((number // (10 ** (12 - 2))) / 100) + "T"
	elif abs(number / (10 ** 9)) >= 1:
		return str((number // (10 ** (9 - 2))) / 100) + "B"
	elif abs(number / (10 ** 6)) >= 1:
		return str((number // (10 ** (6 - 2))) / 100) + "M"
	elif abs(number / (10 ** 3)) >= 1:
		return str((number // (10 ** (3 - 2))) / 100) + "K"
	else:
		return str(number)

# anchor can be one of the following:
# topleft, bottomleft, topright, bottomright
# midtop, midleft, midbottom, midright
# center, centerx, centery
def ui_framework_text_drawText(
	fontId: str,
	coord,
	text: str,
	color,
	anchor: str = "topleft"
):
	font = ui_framework_text_fonts.get(fontId) # type: pygame.font.Font
	if font is None:
		raise ValueError(f"Font {fontId} not loaded")
	text_prepared = font.render(text, True, color)
	rect = text_prepared.get_rect()
	setattr(rect, anchor, coord)
	Window_inst.blit(text_prepared, rect)


ui_component_welcome_BOUTON_LARGEUR = 300
ui_component_welcome_BOUTON_HAUTEUR = 40
ui_component_welcome_BOUTON_ESPACE = 5

ui_component_welcome_easterEgg = 0

def ui_component_welcome_toggleEasterEgg(mode=0):
	global ui_component_welcome_easterEgg
	if ui_component_welcome_easterEgg == mode:
		ui_component_welcome_easterEgg = 0
	else:
		ui_component_welcome_easterEgg = mode

def ui_component_welcome_getEasterEgg(mode):
	match mode:
		case 0:
			return ('Capitalism Island 2', 'background')
		case 1:
			return ('Communism Island 2', 'background2')
		case 2:
			return ('Colonisalism Island 2', 'background3')

def ui_component_welcome__drawBackground(rect):
	xxx = ui_component_welcome_getEasterEgg(ui_component_welcome_easterEgg)
	ui_framework_image_drawImage(xxx[1], rect)
	ui_framework_text_drawText('title', (rect[1][0] // 2, rect[1][1] // 2), xxx[0], (255, 255, 255), "center")

		


ui_component_welcome_welcomeMenu = ui_framework_framework_component(
	z=0,
	rect=lambda parent: parent,
	draw=ui_component_welcome__drawBackground,
	childs=[
		# Bouton Play
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_welcome_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_welcome_BOUTON_HAUTEUR + ui_component_welcome_BOUTON_ESPACE)
				),
				(ui_component_welcome_BOUTON_LARGEUR, ui_component_welcome_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "Play", VC_BACKGROUND, VC_ROUNDING_SMOOTH, VC_ACCENT),
			click=lambda: change_menu(GestionMenu_MENU_JEU),
		),

		# # Bouton Settings 
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_welcome_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_welcome_BOUTON_HAUTEUR + ui_component_welcome_BOUTON_ESPACE) * 2
				),
				(ui_component_welcome_BOUTON_LARGEUR, ui_component_welcome_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "Settings", VC_BACKGROUND, VC_ROUNDING_SMOOTH, VC_ACCENT),
			click=lambda: change_menu(GestionMenu_MENU_REGLAGE),
		),

		# Bouton Exit 
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_welcome_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_welcome_BOUTON_HAUTEUR + ui_component_welcome_BOUTON_ESPACE) * 3
				),
				(ui_component_welcome_BOUTON_LARGEUR, ui_component_welcome_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "Exit", VC_BACKGROUND, VC_ROUNDING_SMOOTH, VC_ACCENT),
			click=Window_stop,
		),

		# Bouton Easter Egg 
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(0, 0),
				(100, 100)
			),
			draw=lambda rect: None,
			click=lambda: ui_component_welcome_toggleEasterEgg(1),
		),

		# Bouton Easter Egg 
		ui_framework_framework_component(
			z=1,
			rect=lambda parent: (
				(parent[1][0] - 100, 0),
				(100, 100)
			),
			draw=lambda rect: None,
			click=lambda: ui_component_welcome_toggleEasterEgg(2),
		),
	]
)

def ui_component_welcome_drawWelcome():
	ui_framework_framework_component_show(ui_component_welcome_welcomeMenu)


def ui_component_stock_showStockMenu(pos):
	ui_framework_framework_component_show(ui_component_stock_stockMenu)


def ui_component_tech_drawTech():
	ui_framework_framework_component_show(ui_component_tech_techMenu)


ui_component_tobpar_PADDING = 5

ui_component_tobpar_STAT_WIDTH = 300

ui_component_tobpar_COLOR_DARK_RED = (120, 0, 0)
ui_component_tobpar_COLOR_GRAY = (80, 80, 80)

def ui_component_tobpar_drawStat(rect, num, num_incr, image_key):
	longNumber(num)
	message = f"{longNumber(num)}"
	ui_framework_draw_drawRect(rect, VC_BACKGROUND, VC_ROUNDING_SMOOTH, hover=VC_SECONDARY)
	ui_framework_image_drawImage(image_key, (
		rect[0],
		(rect[1][1], rect[1][1])
	))
	ui_framework_text_drawText('font2', (rect[0][0] + rect[1][0] - ui_component_tobpar_PADDING, rect[0][1] + rect[1][1] // 2), message, VC_TEXT, "midright")

ui_component_tobpar_topBar = ui_framework_framework_component(
	z=1,
	padding=VC_PADDING,
	rect=lambda parent: (
		(0, 0),
		(parent[1][0], VC_TOP_BAR_HEIGHT)
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, VC_BACKGROUND3),
	click=lambda pos: None,
	childs=[
		# Mode de la carte
		*(ui_framework_framework_component(
			z=2,
			# margin=PADDING,
			rect=lambda parent, index=index: (
				((parent[1][1] + VC_PADDING) * index, 0),
				(parent[1][1], parent[1][1])
			),
			draw=lambda rect, is_in, value=value: ui_common_centerTextButton(rect, 
				'font1', value[0],
				VC_ACCENT if SCREENMODE_val == value[1] else VC_BACKGROUND,
				VC_ROUNDING_SMOOTH, VC_PRIMARY
			),
			click=lambda pos, value=value: select(value[1])
		) for index, value in enumerate([
			("A", SCREENMODE_MAIN),
			("B", SCREENMODE_ECONOMY_SUPPLY),
		])),

		# Money
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				((parent[1][1] + VC_PADDING) * 2, 0),
				(ui_component_tobpar_STAT_WIDTH, parent[1][1])
			),
			draw=lambda rect: ui_component_tobpar_drawStat(rect, model_market_wallet_money, model_stat_setup_get_stat('money'), 'money'),
			click=ui_component_stock_showStockMenu,
		),

		# Science
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				((parent[1][1] + VC_PADDING) * 2 + (ui_component_tobpar_STAT_WIDTH + VC_PADDING), 0),
				(ui_component_tobpar_STAT_WIDTH, parent[1][1])
			),
			draw=lambda rect: ui_component_tobpar_drawStat(rect, model_market_wallet_science, model_stat_setup_get_stat('science'), 'science'),
			click=ui_component_tech_drawTech,
		),
		
		# Vitesse de la simulation
		*(ui_framework_framework_component(
			z=2,
			rect=lambda parent, i=i: (
				(parent[1][0] - (7-i) * (parent[1][1] + VC_PADDING) + VC_PADDING, 0),
				(parent[1][1], parent[1][1])
			),
			draw=lambda rect, hover, i=i: ui_common_centerTextButton(rect, 
				'font1', f"{i}",
				VC_PRIMARY if val == 0 else VC_ACCENT if val >= i else VC_BACKGROUND,
				VC_ROUNDING_SMOOTH, VC_PRIMARY
			),
			click=lambda pos, i=i: model_speed_set(i),
		) for i in range(1, 6)),

		#exit
		ui_framework_framework_component(
			z=2, 
			rect=lambda parent: (
				(parent[1][0] - (parent[1][1]), 0),
				(parent[1][1], parent[1][1])
			), 
			draw=ui_common_exit_button, 
			click=lambda: change_menu(GestionMenu_MENU_INTRO)
		)
	]
)


def ui_component_tobpar_showTopBar():
	ui_framework_framework_component_show(ui_component_tobpar_topBar) 


ui_component_tech_tech_selected = None

ui_component_tech_NB_TECH_BRANCH = 5
ui_component_tech_TECH_PER_BRANCH = 3

ui_component_tech_TECH_MENU_SIZE = (500, 300)

ui_component_tech_HEADER_HEIGHT=75
ui_component_tech_TECH_HEIGHT=75
ui_component_tech_TECH_COST_WIDTH=150

def ui_component_tech_closeTech(pos):
	ui_framework_framework_component_hide(ui_component_tech_techMenu)

def ui_component_tech__selectTech(i, j):
	global ui_component_tech_tech_selected
	ui_component_tech_tech_selected = (i, j)



def ui_component_tech__drawTech(rect, i, j):
	global ui_component_tech_tech_selected
	tech = model_technologyTree_get_tech_for_draw(i, j)
	color = VC_PRIMARY if ui_component_tech_tech_selected == (i, j) else VC_SECONDARY if tech['unlocked'] else VC_BACKGROUND3
	ui_common_centerTextButton(rect, 'font2', tech['name'], color, VC_ROUNDING_SMOOTH, VC_ACCENT if not ui_component_tech_tech_selected == (i, j) else None)

def ui_component_tech__drawTechInfo(rect):
	ui_framework_draw_drawRect(rect, VC_BACKGROUND3, VC_ROUNDING_HARD)
	if ui_component_tech_tech_selected is None:
		return
	tech = model_technologyTree_get_tech_for_draw(ui_component_tech_tech_selected[0], ui_component_tech_tech_selected[1])
	for i in range(len(tech['unlocks'])):
		message = "Unlocks {}".format(ui_map_industry_print_industry(tech['unlocks'][i]))
		ui_framework_text_drawText('font2', (rect[0][0] + VC_PADDING + VC_MENU_BORDER_WIDTH, rect[0][1] + VC_PADDING + VC_MENU_BORDER_WIDTH + 30 * i), message, VC_TEXT)

ui_component_tech_techMenu = ui_framework_framework_component(
	z=10,
	padding=VC_PADDING + VC_MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(
			parent[1][0] // 2 - ui_component_tech_TECH_MENU_SIZE[0],
			parent[1][1] // 2 - ui_component_tech_TECH_MENU_SIZE[1]
		),
		(
			ui_component_tech_TECH_MENU_SIZE[0] * 2,
			ui_component_tech_TECH_MENU_SIZE[1] * 2
		),
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, VC_BACKGROUND2, VC_ROUNDING_HARD) or\
					  ui_framework_draw_drawRect(rect, VC_PRIMARY, VC_ROUNDING_HARD, VC_MENU_BORDER_WIDTH),
	click=lambda pos: None,
	clickOutside=lambda pos: ui_framework_framework_component_hide(ui_component_tech_techMenu),
	childs=[
		# Header
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(0, 0),
				(
					parent[1][0] - ui_component_tech_HEADER_HEIGHT - VC_PADDING,
					ui_component_tech_HEADER_HEIGHT,
				)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', 'Technologies', VC_BACKGROUND3, VC_ROUNDING_HARD),
			click=lambda pos: None,
		),

		# Close button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - ui_component_tech_HEADER_HEIGHT, 0),
				(ui_component_tech_HEADER_HEIGHT, ui_component_tech_HEADER_HEIGHT)
			),
			draw=ui_common_exit_button,
			click=ui_component_tech_closeTech,
		),

		# Techs
		*[(ui_framework_framework_component(
			z=2,
			rect=lambda parent, x=x, y=y: (
				(
					(((parent[1][0] - ui_component_tech_NB_TECH_BRANCH * VC_PADDING) // ui_component_tech_NB_TECH_BRANCH) + VC_PADDING) * x,
					(ui_component_tech_TECH_HEIGHT + VC_PADDING) * y + ui_component_tech_HEADER_HEIGHT + VC_PADDING,
				),
				(
					((parent[1][0] - ui_component_tech_NB_TECH_BRANCH * VC_PADDING) // ui_component_tech_NB_TECH_BRANCH),
					ui_component_tech_TECH_HEIGHT
				),
			),
			draw=lambda rect, is_in, x=x, y=y: ui_component_tech__drawTech(rect, x, y),
			click=lambda pos, x=x, y=y: ui_component_tech__selectTech(x, y),
		)) for x in range(ui_component_tech_NB_TECH_BRANCH) for y in range(ui_component_tech_TECH_PER_BRANCH)],

		# Selected Tech Info
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(
					0,
					(ui_component_tech_TECH_HEIGHT + VC_PADDING) * ui_component_tech_TECH_PER_BRANCH + ui_component_tech_HEADER_HEIGHT + VC_PADDING,
				),
				(
					parent[1][0] - ui_component_tech_TECH_COST_WIDTH - VC_PADDING,
					parent[1][1] - (ui_component_tech_TECH_HEIGHT + VC_PADDING) * (ui_component_tech_TECH_PER_BRANCH) - (ui_component_tech_HEADER_HEIGHT + VC_PADDING),
				),
			),
			draw=ui_component_tech__drawTechInfo,
			click=lambda pos: None,
		),

		# Add Tech Cost
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(
					parent[1][0] - ui_component_tech_TECH_COST_WIDTH,
					(ui_component_tech_TECH_HEIGHT + VC_PADDING) * ui_component_tech_TECH_PER_BRANCH + ui_component_tech_HEADER_HEIGHT + VC_PADDING,
				),
				(
					ui_component_tech_TECH_COST_WIDTH,
					parent[1][1] - (ui_component_tech_TECH_HEIGHT + VC_PADDING) * (ui_component_tech_TECH_PER_BRANCH) - (ui_component_tech_HEADER_HEIGHT + VC_PADDING) - (ui_component_tech_TECH_COST_WIDTH + VC_PADDING),
				),
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 
				'font2', "{}".format(model_technologyTree_get_tech_for_draw(ui_component_tech_tech_selected[0], ui_component_tech_tech_selected[1])['cost']) if ui_component_tech_tech_selected else "",
				VC_BACKGROUND3, VC_ROUNDING_SMOOTH
			),
			click=lambda pos: None,
		),

		# Add Tech Button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(
					parent[1][0] - ui_component_tech_TECH_COST_WIDTH,
					parent[1][1] - ui_component_tech_TECH_COST_WIDTH,
				),
				(ui_component_tech_TECH_COST_WIDTH, ui_component_tech_TECH_COST_WIDTH),
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "Add", VC_BACKGROUND3, VC_ROUNDING_SMOOTH, VC_ACCENT),
			click=lambda pos: model_technologyTree_add_tech(ui_component_tech_tech_selected[0], ui_component_tech_tech_selected[1]),
		),
	]
)


ui_component_stock_MENU_MARGIN = 5 #en pixels
ui_component_stock_EXIT_BUTTON_BORDER = 2 #en pixels
ui_component_stock_CLOSE_BUTTON_SIZE = (75, 75)
ui_component_stock_RESOURCE_BUTTON_HEIGHT = (Window_resolution[1]- 2 * (ui_component_stock_MENU_MARGIN + VC_MENU_BORDER_WIDTH + VC_PADDING) - VC_TOP_BAR_HEIGHT - 2 * VC_PADDING- ui_component_stock_CLOSE_BUTTON_SIZE[1]) / 2

ui_component_stock_NUMBER_OF_GOODS = model_market_goods_GOODS_SAND
ui_component_stock_NUMBER_OF_COLUMNS = 3

ui_component_stock_RATIO = (
	ui_component_stock_NUMBER_OF_COLUMNS,
	ui_component_stock_NUMBER_OF_GOODS // ui_component_stock_NUMBER_OF_COLUMNS + 1,
)


def ui_component_stock_closeStockMenu(pos):
	global SelectedTile_val
	global ui_component_stock_stockMenu
	SelectedTile_val = None
	ui_framework_framework_component_hide(ui_component_stock_stockMenu)

def ui_component_stock_drawStock(goods_id):
	good = ui_map_goods_draw_goods(goods_id)
	def res(rect):
		ui_framework_draw_drawRect(rect, VC_BACKGROUND3, VC_ROUNDING_HARD)
		rectangle = ((rect[0][0] + VC_PADDING, rect[0][1] + VC_PADDING), (rect[1][1] - 2 * VC_PADDING, rect[1][1] - 2 * VC_PADDING))
		good(rectangle)
		ui_common_centerRightTextButton((
			(rectangle[0][0] + rectangle[1][0] + VC_PADDING, rectangle[0][1]),
			(rect[1][0] - 2 * VC_PADDING - rectangle[1][0] - VC_PADDING, rect[1][1] - 2 * VC_PADDING)
		), 'font3', '{}'.format(model_market_stockpile_get_stock(goods_id)), VC_BACKGROUND2, VC_ROUNDING_SMOOTH, VC_PADDING)
	return res


ui_component_stock_stockMenu = ui_framework_framework_component(
	z=3,
	margin=VC_PADDING,
	padding=VC_PADDING + VC_MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, VC_TOP_BAR_HEIGHT),
		(VC_LARGEUR_SIDEMENU, parent[1][1] - VC_TOP_BAR_HEIGHT),
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, VC_BACKGROUND, VC_ROUNDING_SMOOTH) or \
					  ui_framework_draw_drawRect(rect, VC_PRIMARY, VC_ROUNDING_SMOOTH, VC_MENU_BORDER_WIDTH),
	click=lambda pos: None,
	clickOutside=ui_component_stock_closeStockMenu,
	childs=[
		# Header
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: 
			(
				(0, 0),
				(
					parent[1][0] - VC_PADDING - ui_component_stock_CLOSE_BUTTON_SIZE[0],
					ui_component_stock_CLOSE_BUTTON_SIZE[1]
				)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, "font2", "Stock", VC_BACKGROUND3, VC_ROUNDING_SMOOTH)
		),

		# Close button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - ui_component_stock_CLOSE_BUTTON_SIZE[0], 0),
				ui_component_stock_CLOSE_BUTTON_SIZE
			),
			draw=ui_common_exit_button,
			click=ui_component_stock_closeStockMenu,
		),

		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(0 - VC_PADDING // 2, ui_component_stock_CLOSE_BUTTON_SIZE[1] + VC_PADDING // 2),
				(parent[1][0] + VC_PADDING, parent[1][1] - ui_component_stock_CLOSE_BUTTON_SIZE[1] + VC_PADDING)
			),
			draw=lambda rect: None,
			childs=[
				*[ui_framework_framework_component(
					z=2,
					margin=VC_PADDING // 2,
					rect=lambda parent, x=(i % ui_component_stock_NUMBER_OF_COLUMNS), y=(i // ui_component_stock_NUMBER_OF_COLUMNS): (
						(
							x * (parent[1][0] // ui_component_stock_RATIO[0]),
							y * (parent[1][1] // ui_component_stock_RATIO[1]),
						),
						(
							parent[1][0] // ui_component_stock_RATIO[0],
							parent[1][1] // ui_component_stock_RATIO[1],
						)
					),
					draw=ui_component_stock_drawStock(i+1)
				) for i in range(model_market_goods_GOODS_SAND)],
			]
		),

	]
)


ui_component_sidemenu_MENU_MARGIN = 5 #en pixels
ui_component_sidemenu_HEADER_HEIGHT = 75
ui_component_sidemenu_CLOSE_BUTTON_SIZE = (75, 75)
ui_component_sidemenu_RESOURCE_CARTE_HEIGHT = (Window_resolution[1] - 2 * (ui_component_sidemenu_MENU_MARGIN + VC_MENU_BORDER_WIDTH + VC_PADDING) - VC_TOP_BAR_HEIGHT - 2 * VC_PADDING - ui_component_sidemenu_CLOSE_BUTTON_SIZE[1]) / 2
ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT = (ui_component_sidemenu_RESOURCE_CARTE_HEIGHT - 6 * VC_PADDING) / 5


def closeSideMenu():
	global sideMenu, SelectedTile_val
	SelectedTile_val = None
	ui_framework_framework_component_hide(sideMenu) 
	ui_framework_framework_component_temp_remove(sideMenu)

def refreshSideMenu():
	global sideMenu
	ui_framework_framework_component_temp_remove(sideMenu)
	createTemp()


def __drawRessourceButton(rect, good):
	ui_framework_draw_drawRect(rect, VC_BACKGROUND2, VC_ROUNDING_SMOOTH)
	position, taille = rect
	draw_func = ui_map_goods_draw_goods(good)
	draw_func(((position[0] + (taille[1] - 50) / 2, position[1] + (taille[1] - 50) / 2), (50, 50)))
	ui_common_centerTextButton(
		(
			(position[0] + 50 + 2 * VC_PADDING, position[1] + VC_PADDING),
			(taille[0] - 2 * VC_PADDING - 50 - VC_PADDING, taille[1] - 2 * VC_PADDING)
		),
		'font3', '{}'.format(ui_map_goods_print_goods(good)),
		VC_BACKGROUND3, VC_ROUNDING_SMOOTH
	)

def __drawBuildingButton(rect, building_id):
	ui_framework_draw_drawRect(rect, VC_BACKGROUND2, VC_ROUNDING_SMOOTH)
	position, taille = rect
	draw_func = ui_map_industry_draw_industry_menu2(building_id)
	draw_func(((position[0] + (taille[1] - 50) / 2, position[1] + (taille[1] - 50) / 2), (50, 50)), False)
	ui_common_centerTextButton(
		(
			(position[0] + 50 + 2 * VC_PADDING, position[1] + VC_PADDING),
			(taille[0] - 2 * VC_PADDING - 50 - VC_PADDING, taille[1] - 2 * VC_PADDING)
		),
		'font3', '{}'.format(ui_map_industry_print_industry(building_id)),
		VC_BACKGROUND2, VC_ROUNDING_SMOOTH
	)


sideMenu = ui_framework_framework_component(
	z=2,
	margin=ui_component_sidemenu_MENU_MARGIN,
	padding=VC_PADDING + VC_MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, VC_TOP_BAR_HEIGHT),
		(VC_LARGEUR_SIDEMENU, parent[1][1] - VC_TOP_BAR_HEIGHT),
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, VC_BACKGROUND, VC_ROUNDING_SMOOTH) or\
					  ui_framework_draw_drawRect(rect, VC_PRIMARY, VC_ROUNDING_SMOOTH, VC_MENU_BORDER_WIDTH),
	click=lambda pos: None,
	clickOutside=closeSideMenu,
	childs=[
		# Header
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: 
			(
				(0, 0),
				(
					parent[1][0] - VC_PADDING - ui_component_sidemenu_HEADER_HEIGHT,
					ui_component_sidemenu_HEADER_HEIGHT
				)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, "font2", ui_map_terrainTile_print_terrain_tile(model_terrain_terrain_get_terrain_tile(SelectedTile_val)) if SelectedTile_val else "", VC_BACKGROUND3, VC_ROUNDING_SMOOTH)
		),

		# Close button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - ui_component_sidemenu_CLOSE_BUTTON_SIZE[0], 0),
				(ui_component_sidemenu_HEADER_HEIGHT, ui_component_sidemenu_HEADER_HEIGHT)
			),
			draw=ui_common_exit_button,
			click=closeSideMenu
		),
	]
)

def carteRessource(pos):
	terrain = model_terrain_terrain_get_terrain_tile(SelectedTile_val)
	ressource = model_terrain_terrainTile_ressource(terrain)
	if not ressource:
		return
	goods = ui_map_goods_ressources_to_goods(model_terrain_ressource_type(ressource))
	return ui_framework_framework_component(
		z=2,
		padding=VC_PADDING,
		rect=lambda parent: (
			(
				0,
				ui_component_sidemenu_HEADER_HEIGHT + VC_PADDING + pos * (ui_component_sidemenu_RESOURCE_CARTE_HEIGHT + VC_PADDING),
			),
			(
				parent[1][0],
				ui_component_sidemenu_RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect: ui_framework_draw_drawRect(rect, VC_BACKGROUND3, VC_ROUNDING_SMOOTH),
		childs=[
			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(0, 0),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: ui_common_centerTextButton(rect, "font3", "Ressources", VC_BACKGROUND2, VC_ROUNDING_SMOOTH,),
			),

			*(ui_framework_framework_component(
				z=3,
				rect=lambda parent, y=index: (
					(
						0,
						(y + 1) * (ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + VC_PADDING),
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect, is_in, good=good: __drawRessourceButton(rect, good)
			)
			for index,good in enumerate(goods)
			),
		]
	)


def carteIndustry(pos):
	building = model_plants_get(SelectedTile_val)
	building_id = model_Plant_type(building)
	if not model_plants_get(SelectedTile_val):
		return

	return ui_framework_framework_component(
		z=2,
		padding=VC_PADDING,
		rect=lambda parent: (
			(
				0,
				ui_component_sidemenu_HEADER_HEIGHT + VC_PADDING + pos * (ui_component_sidemenu_RESOURCE_CARTE_HEIGHT + VC_PADDING),
			),
			(
				parent[1][0],
				ui_component_sidemenu_RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect: ui_framework_draw_drawRect(rect, VC_BACKGROUND3, VC_ROUNDING_SMOOTH),
		childs=[
			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(0, 0),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: ui_common_centerTextButton(rect, "font3", "Building", VC_BACKGROUND2, VC_ROUNDING_SMOOTH),
			),

			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + VC_PADDING) * 1,
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect, is_in, building_id=building_id: __drawBuildingButton(rect, building_id)
			),

			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + VC_PADDING) * 2,
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=ui_map_industry_draw_industry_product(building_id),
				childs=[],
			),

			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + VC_PADDING) * 3,
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: None,
				childs=[
					ui_framework_framework_component(
						z=3,
						rect=lambda parent: (
							(
								0,
								0,
							),
							(
								parent[1][0] // 2,
								parent[1][1],
							)
						),
						draw=lambda rect: ui_common_centerLeftTextButton(
							rect,
							'font3', '{}'.format("Generated"),
							VC_BACKGROUND2, VC_ROUNDING_SMOOTH, VC_PADDING
						)
					),
					
					ui_framework_framework_component(
						z=3,
						rect=lambda parent: (
							(
								parent[1][0] // 2 + VC_PADDING,
								0,
							),
							(
								parent[1][0] // 2 - VC_PADDING,
								parent[1][1],
							)
						),
						draw=lambda rect: ui_common_centerRightTextButton(
							rect,
							'font3', longNumber(building['generated']),
							VC_BACKGROUND2, VC_ROUNDING_SMOOTH, VC_PADDING
						)
					),
				],
			),

			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					(
						0,
						(ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT + VC_PADDING) * 4,
					),
					(
						parent[1][0],
						ui_component_sidemenu_RESOURCE_BUTTON_HEIGHT,
					)
				),
				draw=lambda rect: None,
				childs=[
					ui_framework_framework_component(
						z=3,
						rect=lambda parent: (
							(
								0,
								0,
							),
							(
								parent[1][0] // 2,
								parent[1][1],
							)
						),
						draw=lambda rect: ui_common_centerLeftTextButton(
							rect,
							'font3', '{}'.format("Level"),
							VC_BACKGROUND2, VC_ROUNDING_SMOOTH, VC_PADDING
						)
					),
					
					ui_framework_framework_component(
						z=3,
						rect=lambda parent: (
							(
								parent[1][0] // 2 + VC_PADDING,
								0,
							),
							(
								parent[1][0] // 2 - VC_PADDING,
								parent[1][1],
							)
						),
						draw=lambda rect: ui_common_centerRightTextButton(
							rect,
							'font3', longNumber(0),
							VC_BACKGROUND2, VC_ROUNDING_SMOOTH, VC_PADDING
						)
					),
				],
			),

		]
	)

def cartePlus(pos):
	return ui_framework_framework_component(
		z=2,
		padding=VC_PADDING,
		rect=lambda parent: (
			(
				0,
				ui_component_sidemenu_HEADER_HEIGHT + VC_PADDING + pos * (ui_component_sidemenu_RESOURCE_CARTE_HEIGHT + VC_PADDING),
			),
			(
				parent[1][0],
				ui_component_sidemenu_RESOURCE_CARTE_HEIGHT
			)
		),
		draw=lambda rect: ui_framework_draw_drawRect(rect, VC_BACKGROUND3, VC_ROUNDING_SMOOTH, hover=VC_ACCENT),
		click=ui_component_placeBuilding_showplaceBuildingsMenu,
		childs=[
			ui_framework_framework_component(
				z=3,
				rect=lambda parent: (
					((parent[1][0] - parent[1][1]) // 2, 0),
					(
						parent[1][1],
						parent[1][1],
					)
				),
				draw=lambda rect: ui_framework_image_drawImage('plus', rect),
				click=None
			),
		]
	)

def createTemp():
	res = []
	index = 0
	# print(get(val))


	if index < 2 and model_plants_get(SelectedTile_val):
		res.append(carteIndustry(index))
		index += 1

	if index < 2 and model_terrain_terrainTile_ressource(model_terrain_terrain_get_terrain_tile(SelectedTile_val)):
		res.append(carteRessource(index))
		index += 1
	
	if index < 2:
		res.append(cartePlus(index))
		index += 1

	ui_framework_framework_component_add_temp(sideMenu, res)
	ui_framework_framework_component_show(sideMenu)

def showSideMenu():
	if sideMenu['_hidden']:
		createTemp()
ui_component_settings_BOUTON_LARGEUR = 400
ui_component_settings_BOUTON_HAUTEUR = 50

ui_component_settings_OPTION_HEIGHT = ui_component_settings_BOUTON_HAUTEUR - 2 * VC_PADDING
ui_component_settings_OPTION_WIDTH = 120


def ui_component_settings__drawBackground(rect):
	ui_framework_draw_drawRect(rect, VC_SECONDARY)

def ui_component_settings__drawSettingBar(rect, message):
	ui_framework_draw_drawRect(rect, VC_BACKGROUND, VC_ROUNDING_SMOOTH)
	ui_framework_text_drawText('font2', (rect[0][0] + VC_PADDING, rect[0][1] + rect[1][1] // 2), message, VC_TEXT, "midleft")

ui_component_settings_settingsMenu = ui_framework_framework_component(
	z=0,
	rect=lambda: (
		(0, 0),
		Window_resolution
	),
	draw=ui_component_settings__drawBackground,
	click=lambda: None,
	childs=[
		# Keyboard Layout
		ui_framework_framework_component(
			z=1,
			padding=VC_PADDING,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_settings_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_settings_BOUTON_HAUTEUR + VC_PADDING),
				),
				(ui_component_settings_BOUTON_LARGEUR, ui_component_settings_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_component_settings__drawSettingBar(rect, "Layout"),
			click=lambda: None,
			childs=[
				# Bouton Azerty 
				ui_framework_framework_component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - ui_component_settings_OPTION_WIDTH, 0),
						(ui_component_settings_OPTION_WIDTH, ui_component_settings_OPTION_HEIGHT)
					),
					draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "AZERTY",
						VC_ACCENT if GestionClavider_clavier == GestionClavider_CLAVIER_AZERTY else VC_BACKGROUND3,
						VC_ROUNDING_SMOOTH, VC_ACCENT
					),
					click=lambda: GestionClavider_change_clavier(GestionClavider_CLAVIER_AZERTY)
				),

				# Bouton Qwerty 
				ui_framework_framework_component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - ui_component_settings_OPTION_WIDTH * 2 - VC_PADDING, 0),
						(ui_component_settings_OPTION_WIDTH, ui_component_settings_OPTION_HEIGHT)
					),
					draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "QWERTY",
						VC_ACCENT if GestionClavider_clavier == GestionClavider_CLAVIER_QWERTY else VC_BACKGROUND3,
						VC_ROUNDING_SMOOTH, VC_ACCENT
					),
					click=lambda: GestionClavider_change_clavier(GestionClavider_CLAVIER_QWERTY)
				),
			]
		),

		# Style
		ui_framework_framework_component(
			z=1,
			padding=VC_PADDING,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_settings_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_settings_BOUTON_HAUTEUR + VC_PADDING) * 2,
				),
				(ui_component_settings_BOUTON_LARGEUR, ui_component_settings_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_component_settings__drawSettingBar(rect, "Style"),
			click=lambda: None,
			childs=[
				# Bouton Light
				ui_framework_framework_component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - ui_component_settings_OPTION_WIDTH, 0),
						(ui_component_settings_OPTION_WIDTH, ui_component_settings_OPTION_HEIGHT)
					),
					draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "LIGHT",
						VC_ACCENT if GestionMode_mode == GestionMode_MODE_LIGHT else VC_BACKGROUND3,
						VC_ROUNDING_SMOOTH, VC_ACCENT
					),
					click=lambda: VC_change_Background(GestionMode_MODE_LIGHT),
				),

				# Bouton Dark
				ui_framework_framework_component(
					z=2,
					rect=lambda parent: (
						(parent[1][0] - ui_component_settings_OPTION_WIDTH * 2 - VC_PADDING, 0),
						(ui_component_settings_OPTION_WIDTH, ui_component_settings_OPTION_HEIGHT)
					),
					draw=lambda rect: ui_common_centerTextButton(rect, 'font2', "DARK",
						VC_ACCENT if GestionMode_mode == GestionMode_MODE_DARK else VC_BACKGROUND3,
						VC_ROUNDING_SMOOTH, VC_ACCENT
					),
					click=lambda: VC_change_Background(GestionMode_MODE_DARK),
				),
			]
		),

		# Bouton Retour 
		ui_framework_framework_component(
			z=5,
			rect=lambda parent: (
				(
					(parent[1][0] - ui_component_settings_BOUTON_LARGEUR) // 2,
					parent[1][1] // 2 + (ui_component_settings_BOUTON_HAUTEUR + VC_PADDING) * 3,
				),
				(ui_component_settings_BOUTON_LARGEUR, ui_component_settings_BOUTON_HAUTEUR)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, 'font2', 'Exit', VC_BACKGROUND, VC_ROUNDING_SMOOTH, VC_ACCENT),
			click=lambda pos: change_menu(GestionMenu_MENU_INTRO),
		),
	]
)

def ui_component_settings_drawSettings():
	ui_framework_framework_component_show(ui_component_settings_settingsMenu)

ui_component_placeBuilding_EXIT_BUTTON_BORDER = 2 #en pixels
ui_component_placeBuilding_CLOSE_BUTTON_SIZE = (75, 75)
ui_component_placeBuilding_RESOURCE_BUTTON_WIDTH = 250
ui_component_placeBuilding_NOMBRE_DE_COLONNES = 5

def ui_component_placeBuilding_closeplaceBuildingsMenu():
	global ui_component_placeBuilding_placeBuildingsMenu
	# val = None
	ui_framework_framework_component_hide(ui_component_placeBuilding_placeBuildingsMenu)
	ui_framework_framework_component_temp_remove(ui_component_placeBuilding_placeBuildingsMenu)
	refreshSideMenu()

ui_component_placeBuilding_placeBuildingsMenu = ui_framework_framework_component(
	z=4,
	margin=VC_MENU_BORDER_WIDTH,
	padding=VC_PADDING + VC_MENU_BORDER_WIDTH,
	rect=lambda parent: (
		(0, VC_TOP_BAR_HEIGHT),
		(VC_LARGEUR_SIDEMENU, parent[1][1] - VC_TOP_BAR_HEIGHT),
	),
	draw=lambda rect: ui_framework_draw_drawRect(rect, VC_BACKGROUND, VC_ROUNDING_SMOOTH) or\
					  ui_framework_draw_drawRect(rect, VC_PRIMARY, VC_ROUNDING_SMOOTH, VC_MENU_BORDER_WIDTH),
	clickOutside=ui_component_placeBuilding_closeplaceBuildingsMenu,
	childs=[
		# Header
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(0, 0),
				(
					parent[1][0] - (ui_component_placeBuilding_CLOSE_BUTTON_SIZE[0] + VC_PADDING),
					ui_component_placeBuilding_CLOSE_BUTTON_SIZE[1]
				)
			),
			draw=lambda rect: ui_common_centerTextButton(rect, "font2", "Place Building", VC_BACKGROUND3, VC_ROUNDING_SMOOTH),
		),

		# Close button
		ui_framework_framework_component(
			z=2,
			rect=lambda parent: (
				(parent[1][0] - ui_component_placeBuilding_CLOSE_BUTTON_SIZE[0], 0),
				ui_component_placeBuilding_CLOSE_BUTTON_SIZE
			),
			draw=ui_common_exit_button,
			click=ui_component_placeBuilding_closeplaceBuildingsMenu,
		),
	]
)



def ui_component_placeBuilding_showplaceBuildingsMenu():
	if ui_component_placeBuilding_placeBuildingsMenu['_hidden']:
		can_be_build = model_technologyTree_get_placable_on(SelectedTile_val)

		tile_width = ((VC_LARGEUR_SIDEMENU - 2 * (VC_MENU_BORDER_WIDTH + VC_PADDING + VC_MENU_BORDER_WIDTH)) - (ui_component_placeBuilding_NOMBRE_DE_COLONNES - 1) * VC_PADDING) // ui_component_placeBuilding_NOMBRE_DE_COLONNES
		ui_framework_framework_component_add_temp(ui_component_placeBuilding_placeBuildingsMenu, [
			ui_framework_framework_component(
				z=2,
				rect=lambda parent, x=index % ui_component_placeBuilding_NOMBRE_DE_COLONNES, y=index // ui_component_placeBuilding_NOMBRE_DE_COLONNES: (
					(
						x * (tile_width + VC_PADDING),
						y * (tile_width + VC_PADDING) + ui_component_placeBuilding_CLOSE_BUTTON_SIZE[1] + VC_PADDING,
					),
					(
						tile_width,
						tile_width,
					)
				),
				draw=ui_map_industry_draw_industry_menu(building_id),
				click=lambda pos, building_id=building_id: model_plants_place(building_id, SelectedTile_val)\
					or ui_component_placeBuilding_closeplaceBuildingsMenu()
			)
			for index, building_id in enumerate(can_be_build)
		])
		ui_framework_framework_component_show(ui_component_placeBuilding_placeBuildingsMenu)
 

def ui_map_map_drawMap(rect):
	x_min = int(-Window_half_resolution[0] / Zoom_tile_size - Cursor_val[0]) // Zoom_opti_factor - 2
	x_max = int( Window_half_resolution[0] / Zoom_tile_size - Cursor_val[0]) // Zoom_opti_factor + 2
	y_min = int(-Window_half_resolution[1] / Zoom_tile_size - Cursor_val[1]) // Zoom_opti_factor - 2
	y_max = int( Window_half_resolution[1] / Zoom_tile_size - Cursor_val[1]) // Zoom_opti_factor + 2
	
	# Draw Terrain
	for i in range(x_min, x_max):
		for j in range(y_min, y_max):
			coord = (i * Zoom_opti_factor, j * Zoom_opti_factor)
			screen_coord = ui_map_utils_coord_to_px(coord)
			tile_size = int(Zoom_tile_size * Zoom_opti_factor)
			rect = (
				(screen_coord[0], screen_coord[1] - int(Zoom_tile_size)),
				(int(tile_size) + 1, int(tile_size) + 1)
			)
			ui_map_map__drawTerrain(coord)(rect)
	
	# Draw Buildings
	for tile_coord in model_plants_map.keys():
		if x_min * Zoom_opti_factor > tile_coord[0] or tile_coord[0] > x_max * Zoom_opti_factor\
			or y_min * Zoom_opti_factor > tile_coord[1] or tile_coord[1] > y_max * Zoom_opti_factor:
			continue
		screen_coord = ui_map_utils_coord_to_px(tile_coord)
		rect = (
			(screen_coord[0], screen_coord[1] - int(Zoom_tile_size)),
			(int(Zoom_tile_size) + 1, int(Zoom_tile_size) + 1)
		)
		ui_map_map_drawTile(tile_coord)(rect)
	
	# Draw Selected Tile
	if SelectedTile_val:
		ui_map_map__drawTileOutline((255, 255, 255), SelectedTile_val)




ui_component_map_map_component = ui_framework_framework_component(
	z=1,
	rect=lambda: (
		(
			0,
			VC_TOP_BAR_HEIGHT,
		),
		(
			Window_resolution[0],
			Window_resolution[1] - VC_TOP_BAR_HEIGHT
		),
	),
	draw=ui_map_map_drawMap,
	click=lambda pos: SelectedTile_select(pos),
)

def ui_component_map_drawMapComponent():
	ui_framework_framework_component_show(ui_component_map_map_component)

ui_component_main_main_component = ui_framework_framework_component(
	z=0,
	rect=lambda: (
		(0, 0),
		Window_resolution,
	),
	draw=lambda rect: None,
	childs=[
		ui_component_map_map_component,
		ui_component_placeBuilding_placeBuildingsMenu,
		ui_component_settings_settingsMenu,
		sideMenu,
		ui_component_stock_stockMenu,
		ui_component_tech_techMenu,
		ui_component_tobpar_topBar,
		ui_component_welcome_welcomeMenu,
	]
)

def ui_component_main_draw():
	ui_framework_framework_component_draw(ui_component_main_main_component, Window_mouse_position)

def ui_component_main_click(pos):
	ui_framework_framework_component_click(ui_component_main_main_component, pos)



def ui_component_main_hide_all():
	for child in ui_component_main_main_component['_childs']:
		ui_framework_framework_component_hide(child)

ui_component_main_hide_all()



ui_map_industry_PADDING = 10

def ui_map_industry_drawIndustryMenu(id, key):
	technology = model_technologies_get_data(id)
	def res(rect, x, technology=technology):

		ui_framework_image_drawImage('industry', rect)
		if rect[1][1] - ui_map_industry_PADDING * 2 < 1:
			return
		ui_framework_image_drawImage(key,
			((rect[0][0] + ui_map_industry_PADDING, rect[0][1] + ui_map_industry_PADDING),
			(rect[1][0] - ui_map_industry_PADDING * 2, rect[1][1] - ui_map_industry_PADDING * 2)
		))
		ui_common_centerRightText(
			(
				(
					rect[0][0],
					rect[0][1] + rect[1][1] - 20
				),
				(
					rect[1][0],
					20,
				)
			),
			'font3', '{}'.format(longNumber(technology['price'])), 1, (255, 255, 255)
		)
	return res

def ui_map_industry_drawIndustryMenu2(id, key):
	technology = model_technologies_get_data(id)
	def res(rect, x, technology=technology):

		ui_framework_image_drawImage('industry', rect)
		if rect[1][1] - ui_map_industry_PADDING * 2 < 1:
			return
		ui_framework_image_drawImage(key,
			((rect[0][0] + ui_map_industry_PADDING, rect[0][1] + ui_map_industry_PADDING),
			(rect[1][0] - ui_map_industry_PADDING * 2, rect[1][1] - ui_map_industry_PADDING * 2)
		))
	return res

def ui_map_industry_drawIndustryMap(key):
	def res(rect):
		match SCREENMODE_val:
			case 1:
				ui_framework_image_drawImage('industry', rect)
				padding = Zoom_tile_size // 16
				if rect[1][1] - padding * 2 < 1:
					return
				ui_framework_image_drawImage(key,
					((rect[0][0] + padding, rect[0][1] + padding),
					(rect[1][0] - padding * 2, rect[1][1] - padding * 2)
				))
			case 2:
				ui_framework_draw_drawRect(rect, (255, 255, 0))
			case _:
				ui_framework_draw_drawRect(rect, (0, 0, 0))
	return res

def ui_map_industry_drawIndustryProducts(id, key):
	technology = model_technologies_get_data(id)
	inputs = technology['input']
	output = technology['output']
	drawFuncs = [
		*(ui_map_goods_draw_goods(input) for input in inputs),
		lambda rect: ui_framework_image_drawImage('arrow', rect),
		ui_map_goods_draw_goods(output),
	]
	def res(rect):
		ui_framework_draw_drawRect(rect, VC_BACKGROUND2, VC_ROUNDING_SMOOTH)
		rectangle = (rect[1][1], rect[1][1])
		for index, func in enumerate(drawFuncs):
			func((
				(
					rect[0][0] + (rect[1][1] + VC_PADDING) * index,
					rect[0][1]
				),
				rectangle
			))
		
	return res

ui_map_industry_industryPrintMap = {
model_technologies_INDUSTRY_FISHINGBOAT					: ('Fishing Boat'					, ui_map_industry_drawIndustryMap('good_fish')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_FISHINGBOAT					,'good_fish')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_FISHINGBOAT					,'good_fish')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_FISHINGBOAT					,'good_fish')					),
model_technologies_INDUSTRY_SALTEXTRACTION				: ('Salt Extraction'				, ui_map_industry_drawIndustryMap('good_salt')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_SALTEXTRACTION					,'good_salt')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_SALTEXTRACTION					,'good_salt')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_SALTEXTRACTION				,'good_salt')					),
model_technologies_INDUSTRY_WHEAT_FIELDS					: ('Wheat Fields'					, ui_map_industry_drawIndustryMap('good_wheat')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_WHEAT_FIELDS					,'good_wheat')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_WHEAT_FIELDS					,'good_wheat')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_WHEAT_FIELDS					,'good_wheat')					),
model_technologies_INDUSTRY_POTATO_FIELDS					: ('Potato Fields'					, ui_map_industry_drawIndustryMap('good_potato')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_POTATO_FIELDS					,'good_potato')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_POTATO_FIELDS					,'good_potato')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_POTATO_FIELDS					,'good_potato')					),
model_technologies_INDUSTRY_COTTON_FIELDS					: ('Cotton Fields'					, ui_map_industry_drawIndustryMap('good_cotton')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_COTTON_FIELDS					,'good_cotton')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_COTTON_FIELDS					,'good_cotton')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_COTTON_FIELDS					,'good_cotton')					),
model_technologies_INDUSTRY_RICE_FIELDS					: ('Rice Fields'					, ui_map_industry_drawIndustryMap('good_rice')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_RICE_FIELDS					,'good_rice')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_RICE_FIELDS					,'good_rice')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_RICE_FIELDS					,'good_rice')					),
model_technologies_INDUSTRY_FURHUNTINGGROUNDS				: ('Fur Hunting Grounds'			, ui_map_industry_drawIndustryMap('good_fur')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					),
model_technologies_INDUSTRY_LUMBERMILL					: ('Lumber Mill'					, ui_map_industry_drawIndustryMap('good_wood')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_LUMBERMILL						,'good_wood')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_LUMBERMILL						,'good_wood')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_LUMBERMILL					,'good_wood')					),
model_technologies_INDUSTRY_OILWELL						: ('Oil Well'						, ui_map_industry_drawIndustryMap('good_oil')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_OILWELL						,'good_oil')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_OILWELL						,'good_oil')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_OILWELL						,'good_oil')					),
model_technologies_INDUSTRY_COALMINE						: ('Coal Mine'						, ui_map_industry_drawIndustryMap('good_coal')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_COALMINE						,'good_coal')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_COALMINE						,'good_coal')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_COALMINE						,'good_coal')					),
model_technologies_INDUSTRY_IRONMINE						: ('Iron Mine'						, ui_map_industry_drawIndustryMap('good_iron')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_IRONMINE						,'good_iron')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_IRONMINE						,'good_iron')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_IRONMINE						,'good_iron')					),
model_technologies_INDUSTRY_COPPERMINE					: ('Copper Mine'					, ui_map_industry_drawIndustryMap('good_copper')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_COPPERMINE						,'good_copper')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_COPPERMINE						,'good_copper')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_COPPERMINE					,'good_copper')					),
model_technologies_INDUSTRY_PRECIOUSMETALMINE				: ('Precious Metal Mine'			, ui_map_industry_drawIndustryMap('good_precious_metal')		, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			),
model_technologies_INDUSTRY_RAREMETALMINE					: ('Rare Metal Mine'				, ui_map_industry_drawIndustryMap('good_rare_metal')			, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_RAREMETALMINE					,'good_rare_metal')				, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_RAREMETALMINE					,'good_rare_metal')				, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_RAREMETALMINE					,'good_rare_metal')				),
model_technologies_INDUSTRY_BREADFACTORY					: ('Bread Factory'					, ui_map_industry_drawIndustryMap('good_bread')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_BREADFACTORY					,'good_bread')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_BREADFACTORY					,'good_bread')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_BREADFACTORY					,'good_bread')					),
model_technologies_INDUSTRY_ALCOHOLFACTORY				: ('Alcohol Factory'				, ui_map_industry_drawIndustryMap('good_alcohol')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_ALCOHOLFACTORY					,'good_alcohol')				, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_ALCOHOLFACTORY					,'good_alcohol')				, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_ALCOHOLFACTORY				,'good_alcohol')				),
model_technologies_INDUSTRY_SUSHIFACTORY					: ('Sushi Factory'					, ui_map_industry_drawIndustryMap('good_sushi')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_SUSHIFACTORY					,'good_sushi')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_SUSHIFACTORY					,'good_sushi')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_SUSHIFACTORY					,'good_sushi')					),
model_technologies_INDUSTRY_TEXTILEFACTORY				: ('Textile Factory'				, ui_map_industry_drawIndustryMap('good_textile')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_TEXTILEFACTORY					,'good_textile')				, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_TEXTILEFACTORY					,'good_textile')				, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_TEXTILEFACTORY				,'good_textile')				),
model_technologies_INDUSTRY_CLOTHESFACTORY				: ('Clothes Factory'				, ui_map_industry_drawIndustryMap('good_clothes')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_CLOTHESFACTORY					,'good_clothes')				, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_CLOTHESFACTORY					,'good_clothes')				, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_CLOTHESFACTORY				,'good_clothes')				),
model_technologies_INDUSTRY_FURNITUREFACTORY				: ('Furniture Factory'				, ui_map_industry_drawIndustryMap('good_furniture')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_FURNITUREFACTORY				,'good_furniture')				, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_FURNITUREFACTORY				,'good_furniture')				, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_FURNITUREFACTORY				,'good_furniture')				),
model_technologies_INDUSTRY_STEELMILL						: ('Steel Mill'						, ui_map_industry_drawIndustryMap('good_steel')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_STEELMILL						,'good_steel')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_STEELMILL						,'good_steel')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_STEELMILL						,'good_steel')					),
model_technologies_INDUSTRY_TOOLINGFACTORY				: ('Tooling Factory'				, ui_map_industry_drawIndustryMap('good_tools')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_TOOLINGFACTORY					,'good_tools')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_TOOLINGFACTORY					,'good_tools')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_TOOLINGFACTORY				,'good_tools')					),
model_technologies_INDUSTRY_CEMENTFACTORY					: ('Cement Factory'					, ui_map_industry_drawIndustryMap('good_cement')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_CEMENTFACTORY					,'good_cement')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_CEMENTFACTORY					,'good_cement')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_CEMENTFACTORY					,'good_cement')					),
model_technologies_INDUSTRY_REFINARY						: ('Refinary'						, ui_map_industry_drawIndustryMap('good_fuel')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_REFINARY						,'good_fuel')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_REFINARY						,'good_fuel')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_REFINARY						,'good_fuel')					),
model_technologies_INDUSTRY_PLASTICFACTORY				: ('Plastic Factory'				, ui_map_industry_drawIndustryMap('good_plastic')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_PLASTICFACTORY					,'good_plastic')				, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_PLASTICFACTORY					,'good_plastic')				, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_PLASTICFACTORY				,'good_plastic')				),
model_technologies_INDUSTRY_GLASSFACTORY					: ('Glass Factory'					, ui_map_industry_drawIndustryMap('good_glass')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_GLASSFACTORY					,'good_glass')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_GLASSFACTORY					,'good_glass')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_GLASSFACTORY					,'good_glass')					),
model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	: ('Electronic Components Factory'	, ui_map_industry_drawIndustryMap('good_electronics_component')	, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	),
model_technologies_INDUSTRY_RADIOFACTORY					: ('Radio Factory'					, ui_map_industry_drawIndustryMap('good_radio')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_RADIOFACTORY					,'good_radio')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_RADIOFACTORY					,'good_radio')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_RADIOFACTORY					,'good_radio')					),
model_technologies_INDUSTRY_COMPUTERFACTORY				: ('Computer Factory'				, ui_map_industry_drawIndustryMap('good_computer')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_COMPUTERFACTORY				,'good_computer')				, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_COMPUTERFACTORY				,'good_computer')				, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_COMPUTERFACTORY				,'good_computer')				),
model_technologies_INDUSTRY_GUNFACTORY					: ('Gun Factory'					, ui_map_industry_drawIndustryMap('good_guns')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_GUNFACTORY						,'good_guns')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_GUNFACTORY						,'good_guns')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_GUNFACTORY					,'good_guns')					),
model_technologies_INDUSTRY_ENGINEFACTORY					: ('Engine Factory'					, ui_map_industry_drawIndustryMap('good_engine')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_ENGINEFACTORY					,'good_engine')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_ENGINEFACTORY					,'good_engine')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_ENGINEFACTORY					,'good_engine')					),
model_technologies_INDUSTRY_CARFACTORY					: ('Car Factory'					, ui_map_industry_drawIndustryMap('good_car')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_CARFACTORY						,'good_car')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_CARFACTORY						,'good_car')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_CARFACTORY					,'good_car')					),
model_technologies_INDUSTRY_PLANESFACTORY					: ('Planes Factory'					, ui_map_industry_drawIndustryMap('good_planes')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_PLANESFACTORY					,'good_planes')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_PLANESFACTORY					,'good_planes')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_PLANESFACTORY					,'good_planes')					),
model_technologies_INDUSTRY_JEWELRYWORKSHOP				: ('Jewelry Workshop'				, ui_map_industry_drawIndustryMap('good_jewelry')				, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				),
model_technologies_INDUSTRY_PHONEFACTORY					: ('Phone Factory'					, ui_map_industry_drawIndustryMap('good_phone')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_PHONEFACTORY					,'good_phone')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_PHONEFACTORY					,'good_phone')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_PHONEFACTORY					,'good_phone')					),
model_technologies_INDUSTRY_STONEQUERY					: ('Stone Query'					, ui_map_industry_drawIndustryMap('good_stone')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_STONEQUERY						,'good_stone')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_STONEQUERY						,'good_stone')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_STONEQUERY					,'good_stone')					),
model_technologies_INDUSTRY_SANDQUERY						: ('Sand Query'						, ui_map_industry_drawIndustryMap('good_sand')					, ui_map_industry_drawIndustryMenu(model_technologies_INDUSTRY_SANDQUERY						,'good_sand')					, ui_map_industry_drawIndustryProducts(model_technologies_INDUSTRY_SANDQUERY						,'good_sand')					, ui_map_industry_drawIndustryMenu2(model_technologies_INDUSTRY_SANDQUERY						,'good_sand')					),                 
}

def ui_map_industry_print_industry(industry):
	return ui_map_industry_industryPrintMap[industry][0]

def ui_map_industry_draw_industry_map(industry):
	return ui_map_industry_draw_industry_by_id(model_Plant_type(industry))[1]

def ui_map_industry_draw_industry_menu(industry_id):
	return ui_map_industry_draw_industry_by_id(industry_id)[2]

def ui_map_industry_draw_industry_menu2(industry_id):
	return ui_map_industry_draw_industry_by_id(industry_id)[4]

def ui_map_industry_draw_industry_product(industry_id):
	return ui_map_industry_draw_industry_by_id(industry_id)[3]

def ui_map_industry_draw_industry_by_id(industry_id):
	return ui_map_industry_industryPrintMap.get(
		industry_id,
		('', lambda rect: None)
	)


@utils_cache_add_cache
def ui_map_map__drawTerrain(coord: utils_myTyping_coord_i):
	terrainTile = model_terrain_terrain_get_terrain_tile(coord)
	return ui_map_terrainTile_draw_terrain_tile(terrainTile)

@utils_cache_add_cache
def ui_map_map_drawTile(tile_coord: utils_myTyping_coord_i):
	tile = model_plants_get(tile_coord)
	if not tile: return None

	return ui_map_industry_draw_industry_map(tile)

def ui_map_map__drawTileOutline(color: utils_myTyping_Color, coord: utils_myTyping_coord_i):
	new_coord = ui_map_utils_coord_to_px(coord)
	ui_framework_draw_drawRect((
			(new_coord[0], int(new_coord[1] - Zoom_tile_size)),
			(int(Zoom_tile_size), int(Zoom_tile_size))
		),
		color,
		outline=int(Zoom_outline_width),
	)

ui_map_ressource_ressourceDrawMap = {
	model_terrain_ressource_RESSOURCE_FISH:            ('fish'           , lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 0, 230 + h*4))),
	model_terrain_ressource_RESSOURCE_SALT:            ('salt'           , lambda rect, h, h4: ui_framework_image_drawImage('salt', rect)),
	model_terrain_ressource_RESSOURCE_FERTILE_LAND:    ('fertile land'   , lambda rect, h, h4: ui_framework_image_drawImage('fertile_land', rect)),
	model_terrain_ressource_RESSOURCE_HUNTING_GROUNDS: ('fur'            , lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 82, 0))),
	model_terrain_ressource_RESSOURCE_WOOD:            ('wood'           , lambda rect, h, h4: ui_framework_image_drawImage('wood', rect)),
	model_terrain_ressource_RESSOURCE_OIL:             ('oil'            , lambda rect, h, h4: ui_framework_image_drawImage('oil', rect)),
	model_terrain_ressource_RESSOURCE_COAL:            ('coal'           , lambda rect, h, h4: ui_framework_image_drawImage('coal', rect)),
	model_terrain_ressource_RESSOURCE_IRON:            ('iron'           , lambda rect, h, h4: ui_framework_image_drawImage('iron', rect) if h < 35 else ui_framework_image_drawImage('iron2', rect)),
	model_terrain_ressource_RESSOURCE_COPPER:          ('copper'         , lambda rect, h, h4: ui_framework_image_drawImage('copper', rect)),
	model_terrain_ressource_RESSOURCE_PRECIOUS_METALS: ('precious metals', lambda rect, h, h4: ui_framework_image_drawImage('precious', rect)),
	model_terrain_ressource_RESSOURCE_RARE_METALS:     ('rare metals'    , lambda rect, h, h4: ui_framework_image_drawImage('rare', rect)),
	model_terrain_ressource_RESSOURCE_SAND:            ('sand'           , lambda rect, h, h4: ui_framework_image_drawImage('sand', rect)),
	model_terrain_ressource_RESSOURCE_STONE:           ('stone'          , lambda rect, h, h4: ui_framework_image_drawImage('stone', rect)),							
}

def ui_map_ressource_print_ressource(ressource):
	return ui_map_ressource_ressourceDrawMap[model_terrain_ressource_type(ressource)][0]

def ui_map_ressource_draw_ressource(tile):
	func = ui_map_ressource_ressourceDrawMap.get(
		model_terrain_ressource_type(tile),
		('', lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 0, 0)))
	)[1]
	h = model_terrain_ressource_height(tile)
	return lambda rect, h=h, h4=h % 4 * 16: func(rect, h, h4)


ui_map_terrainTile_drawTerrainTileMap = {
	model_terrain_terrainTile_TERRAINTILETYPE_DEEPSEA			: ('Deep sea',		lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 0, 255 + h * 4))),
	model_terrain_terrainTile_TERRAINTILETYPE_SEA				: ('Sea',			lambda rect, h, h4: ui_framework_draw_drawRect(rect, (0, 0, 255 + h * 4))),
	model_terrain_terrainTile_TERRAINTILETYPE_BEACH			: ('Beach',			lambda rect, h, h4: ui_framework_image_drawImage('sand', rect)),
	model_terrain_terrainTile_TERRAINTILETYPE_PLAIN			: ('Plain',			lambda rect, h, h4: ui_framework_image_drawImage('grass', rect)),
	model_terrain_terrainTile_TERRAINTILETYPE_FOREST			: ('Forest',		lambda rect, h, h4: ui_framework_image_drawImage('wood', rect)),
	model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE	: ('Moutain Side',	lambda rect, h, h4: ui_framework_image_drawImage('stone', rect)),
	model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_TOP	: ('Montain Top',	lambda rect, h, h4: ui_framework_image_drawImage('snow', rect)),
}

def ui_map_terrainTile_print_terrain_tile(tile: model_terrain_terrainTile_types):
	return ui_map_terrainTile_drawTerrainTileMap.get(
		model_terrain_terrainTile_type(tile),
		lambda rect, h, h4: ('', ui_framework_draw_drawRect(rect, (0, 0, 0)))
	)[0]

def ui_map_terrainTile_draw_terrain(tile: model_terrain_terrainTile_types):
	func = ui_map_terrainTile_drawTerrainTileMap.get(
		model_terrain_terrainTile_type(tile),
		lambda rect, h, h4: ('', ui_framework_draw_drawRect(rect, (0, 0, 0)))
	)[1]
	h = model_terrain_terrainTile_height(tile)
	h4 = h % 4 * 16
	if model_terrain_terrainTile_ressource(tile) != None:
		ressource_func = ui_map_ressource_draw_ressource(model_terrain_terrainTile_ressource(tile))

		def res(rect, h=h, h4=h4):
			if Zoom_opti_factor <= 1:
				ressource_func(rect)
			else:
				func(rect, h, h4)
		return res
	else:
		return lambda rect, h=h, h4=h4: func(rect, h, h4)

def ui_map_terrainTile_draw_background_stat(tile: model_terrain_terrainTile_types):
	h = model_terrain_terrainTile_height(tile)
	h4 = h % 8 * 8
	if (h < 0):
		return lambda rect, h=h, h4=h4: ui_framework_draw_drawRect(rect, (0, 0, 180 + h * 4))
	else:
		return lambda rect, h=h, h4=h4: ui_framework_draw_drawRect(rect, (80 - h4, 80 - h4, 80 - h4))

def ui_map_terrainTile__draw_terrain_tile(rect, terrain, color):
	match SCREENMODE_val:
		case 1:
			return terrain(rect)
		case 2\
			| 3\
			| 4:
			return color(rect)
		case _:
			return None

def ui_map_terrainTile_draw_terrain_tile(tile: model_terrain_terrainTile_types):
	terrain = ui_map_terrainTile_draw_terrain(tile)
	color = ui_map_terrainTile_draw_background_stat(tile)
	return lambda rect, terrain=terrain, color=color: ui_map_terrainTile__draw_terrain_tile(rect, terrain, color)


def ui_map_utils_coord_to_px(coord: utils_myTyping_coord_f) -> utils_myTyping_coord_i:
	return (
		int(Window_half_resolution[0] + int(Cursor_val[0] * Zoom_tile_size) + (coord[0]) * Zoom_tile_size),
		int(Window_half_resolution[1] - int(Cursor_val[1] * Zoom_tile_size) - (coord[1]) * Zoom_tile_size),
	)

def ui_map_utils_px_to_coord(coord: utils_myTyping_coord_i) -> utils_myTyping_coord_f:
	return (
		(coord[0] - Window_half_resolution[0]) / Zoom_tile_size - Cursor_val[0],
		-((coord[1] - Window_half_resolution[1]) / Zoom_tile_size + Cursor_val[1]),
	)

Cursor_val: utils_myTyping_mut_coord_f = [0, 0]
Cursor_cursor_speed = 0.1

def Cursor_reset():
	global Cursor_val
	Cursor_val = [0, 0]

def Cursor_move_right():
	Cursor_val[0] -= Cursor_cursor_speed * Zoom_val

def Cursor_move_left():
	Cursor_val[0] += Cursor_cursor_speed * Zoom_val

def Cursor_move_up():
	Cursor_val[1] -= Cursor_cursor_speed * Zoom_val

def Cursor_move_down():
	Cursor_val[1] += Cursor_cursor_speed * Zoom_val


def ui_drawFrame_drawFrame():
	match menu:
		case 0:
			ui_component_welcome_drawWelcome()
			
		case 1:
			ui_component_settings_drawSettings()
			
		case 2:
			if SelectedTile_val:
				showSideMenu()
				# ui.components.placeBuildings.showplaceBuildingsMenu()
			ui_component_map_drawMapComponent()
			ui_component_tobpar_showTopBar()
	ui_component_main_draw()





GestionClavider_CLAVIER_AZERTY = 0
GestionClavider_CLAVIER_QWERTY = 1

GestionClavider_clavier = GestionClavider_CLAVIER_QWERTY


def GestionClavider_change_clavier(new_clavier):
    global GestionClavider_clavier
    GestionClavider_clavier = new_clavier




GestionMenu_MENU_INTRO = 0
GestionMenu_MENU_REGLAGE = 1
GestionMenu_MENU_JEU = 2

menu = GestionMenu_MENU_INTRO


def change_menu(new_menu):
    global menu

    ui_component_main_hide_all()
    menu = new_menu




GestionMode_MODE_LIGHT = 0
GestionMode_MODE_DARK = 1
 
GestionMode_mode = GestionMode_MODE_LIGHT


def GestionMode_change_mode(new_mode):
	global GestionMode_mode
	GestionMode_mode = new_mode




SCREENMODE_val = SCREENMODE_MAIN
SCREENMODE_sub = SCREENSUBMODE_NONE

def select(new_mode: int):
	global SCREENMODE_val
	SCREENMODE_val = new_mode

SelectedTile_val: utils_myTyping_coord_i | None = None

def SelectedTile_select(screen_coord: utils_myTyping_coord_i):
	global SelectedTile_val

	coord = ui_map_utils_px_to_coord(screen_coord)
	SelectedTile_val = (
		int(coord[0]) if coord[0] > 0 else int(coord[0]) - 1,
		int(coord[1]) if coord[1] > 0 else int(coord[1]) - 1
	)

def SelectedTile_clear():
	global SelectedTile_val
	SelectedTile_val = None



def VC_change_Background(mode):
	global VC_TEXT, VC_BACKGROUND, VC_BACKGROUND2, VC_BACKGROUND3, VC_PRIMARY, VC_SECONDARY, VC_ACCENT		


	if mode == GestionMode_MODE_LIGHT:
		VC_TEXT = VC_LIGHT_TEXT
		VC_BACKGROUND = VC_LIGHT_BACKGROUND
		VC_BACKGROUND2 = VC_LIGHT_BACKGROUND2
		VC_BACKGROUND3 = VC_LIGHT_BACKGROUND3
		VC_PRIMARY = VC_LIGHT_PRIMARY
		VC_SECONDARY = VC_LIGHT_SECONDARY
		VC_ACCENT = VC_LIGHT_ACCENT
		GestionMode_change_mode(GestionMode_MODE_LIGHT)
			
	
	
	else:
		VC_TEXT = VC_DARK_TEXT
		VC_BACKGROUND = VC_DARK_BACKGROUND
		VC_BACKGROUND2 = VC_DARK_BACKGROUND2
		VC_BACKGROUND3 = VC_DARK_BACKGROUND3
		VC_PRIMARY = VC_DARK_PRIMARY
		VC_SECONDARY = VC_DARK_SECONDARY
		VC_ACCENT = VC_DARK_ACCENT
		GestionMode_change_mode(GestionMode_MODE_DARK)

		

Zoom_val = 100
Zoom__zoom_speed = 1.05
Zoom__zoom_min = 1
Zoom__zoom_max = 1000
Zoom_tile_size = 0
Zoom_line_width = 0
Zoom_outline_width = 0
Zoom_opti_factor = 2

def Zoom__update():
	global Zoom_tile_size, Zoom_line_width, Zoom_outline_width,Zoom_opti_factor
	Zoom_tile_size = 200 / Zoom_val
	Zoom_line_width = 25 / Zoom_val
	Zoom_outline_width = 15 / Zoom_val
	Zoom_opti_factor = max(2 ** int(math.log2(Zoom_val / 10)), 1)

def Zoom_increment():
	global Zoom_val
	if Zoom_val < Zoom__zoom_max:
		Zoom_val *= Zoom__zoom_speed
		Zoom__update()

def Zoom_decrement():
	global Zoom_val
	if Zoom_val > Zoom__zoom_min:
		Zoom_val /= Zoom__zoom_speed
		Zoom__update()

Zoom__update()








def events_handleEvents(event: pygame.event.Event):
	match event.type: # type: ignore
		case pygame.MOUSEWHEEL:
			if (event.y >= 0):
				Zoom_decrement()
			else:
				Zoom_increment()
		case pygame.MOUSEBUTTONUP:
			if (event.button == 1):
				ui_component_main_click(event.pos)
		case pygame.MOUSEMOTION:
			ui_framework_draw_updateHoverCursor(event.pos)
		# case _:
		# 	print(event)




	


def input_repeatKey(key: int):
	if GestionClavider_clavier == GestionClavider_CLAVIER_AZERTY:
		input_repeatKey_azerty(key)
	else:
		input_repeatKey_qwerty(key)
		 
def input_singleKey(key: int):
	if GestionClavider_clavier == GestionClavider_CLAVIER_AZERTY:
		input_singleKey_azerty(key)
	else:
		input_singleKey_qwerty(key)

 

def input_repeatKey_azerty(key: int):
	match key:
		case pygame.K_v:
			Cursor_reset()
		case pygame.K_z | pygame.K_UP:
			Cursor_move_up()
		case pygame.K_q | pygame.K_LEFT:
			Cursor_move_left()
		case pygame.K_s | pygame.K_DOWN:
			Cursor_move_down()
		case pygame.K_d | pygame.K_RIGHT:
			Cursor_move_right()
		case pygame.K_r:
			Zoom_decrement()
		case pygame.K_f:
			Zoom_increment()
		case _:
			pass



def input_repeatKey_qwerty(key):
	match key:
		case pygame.K_v:
			Cursor_reset()
		case pygame.K_w | pygame.K_UP:
			Cursor_move_up()
		case pygame.K_a | pygame.K_LEFT:
			Cursor_move_left()
		case pygame.K_s | pygame.K_DOWN:
			Cursor_move_down()
		case pygame.K_d | pygame.K_RIGHT:
			Cursor_move_right()
		case pygame.K_r:
			Zoom_decrement()
		case pygame.K_f:
			Zoom_increment()
		case _:
			pass
		

def input_singleKey_qwerty(key: int):
	global model_market_wallet_science, model_market_wallet_money
	match key:
		case pygame.K_F11:
			Window_toggleFullscreen()
		case pygame.K_1:
			select(SCREENMODE_MAIN)
		case pygame.K_2:
			select(SCREENMODE_ECONOMY_SUPPLY)
		case pygame.K_3:
			select(SCREENMODE_ECONOMY_DEMAND)
		case pygame.K_4:
			select(SCREENMODE_TRANSPORT)
		case pygame.K_t:
			model_speed_increment()
		case pygame.K_g:
			model_speed_decrement()
		case pygame.K_SPACE:
			model_speed_pause()
		case pygame.K_KP1:
			model_speed_set(1)
		case pygame.K_KP2:
			model_speed_set(2)
		case pygame.K_KP3:
			model_speed_set(3)
		case pygame.K_KP4:
			model_speed_set(4)
		case pygame.K_KP5:
			model_speed_set(5)
		case pygame.K_BACKSPACE:
			if SelectedTile_val:
				if not model_plants_tile_is_empty(SelectedTile_val):
					model_plants_remove(SelectedTile_val)
					ui_map_map_drawTile(SelectedTile_val, True) # Refresh cache for draw
		case pygame.K_o:
			model_market_wallet_science += 10
		case pygame.K_l:
			model_market_wallet_money += 100000000
		case pygame.K_p:
			ui_component_tech_drawTech()
		case _:
			pass

	
def input_singleKey_azerty(key):
	match key:
		case pygame.K_ESCAPE:
			Window_stop()
		case pygame.K_F11:
			Window_toggleFullscreen()
		case pygame.K_1:
			select(SCREENMODE_MAIN)
		case pygame.K_2:
			select(SCREENMODE_ECONOMY_SUPPLY)
		case pygame.K_3:
			select(SCREENMODE_ECONOMY_DEMAND)
		case pygame.K_4:
			select(SCREENMODE_TRANSPORT)
		case pygame.K_t:
			model_speed_increment()
		case pygame.K_g:
			model_speed_decrement()
		case pygame.K_SPACE:
			model_speed_pause()
		case pygame.K_KP1:
			model_speed_set(1)
		case pygame.K_KP2:
			model_speed_set(2)
		case pygame.K_KP3:
			model_speed_set(3)
		case pygame.K_KP4:
			model_speed_set(4)
		case pygame.K_KP5:
			model_speed_set(5)
		case pygame.K_BACKSPACE:
			if SelectedTile_val:
				if not model_plants_tile_is_empty(SelectedTile_val):
					model_plants_remove(SelectedTile_val)
					ui_map_map_drawTile(SelectedTile_val, True) # Refresh cache for draw
		case pygame.K_o:
			model_market_wallet_science += 10
		case pygame.K_l:
			model_market_wallet_money += 100000000
		case pygame.K_p:
			ui_component_tech_drawTech()
		case _:
			pass

	
	




 

		
	
	
	

	



def init_setup():
	model_terrain_terrain_init_random()
	ui_framework_text_loadFont("font1", "monospace", 40)
	ui_framework_text_loadFont("font2", "monospace", 24, True)
	ui_framework_text_loadFont("font3", "monospace", 22, True)
	ui_framework_text_loadFont("title", "monospace", 50, True)

	model_stat_setup_setup_stats()

	ui_framework_image_loadImages({
		'exit'			: './assets/close_button.png',
		'arrow'			: './assets/arrow.png',
		'plus'			: './assets/plus.png',
		'money'			: './assets/coin.png',
		'science'		: './assets/science.png',
		'background'	: './assets/background/background.jpeg',
		'background2'	: './assets/background/communism.jpg',
		'background3'	: './assets/background/t2.jpg',

		'sand'			: './assets/terrain/suspicious_sand_0.png',
		'stone'			: './assets/terrain/stone.png',
		'snow'			: './assets/terrain/diorite.png',
		'grass'			: './assets/terrain/grass.png',
		'wood'			: './assets/terrain/wood.png',
		'coal'			: './assets/ressource/coal_ore.png',
		'iron'			: './assets/ressource/iron_ore.png',
		'iron2'			: './assets/ressource/iron_ore2.png',
		'precious'		: './assets/ressource/diamond_ore3.png',
		'rare'			: './assets/ressource/emerald_ore3.png',
		'copper'		: './assets/ressource/copper_ore.png',
		'salt'			: './assets/ressource/salt.png',
		'oil'			: './assets/ressource/oil.png',
		'fertile_land'	: './assets/ressource/fertile_land.png',

		"industry"						: "./assets/industry.png",
		"good_fish"						: "./assets/goods/fish.png",
		"good_salt"						: "./assets/goods/salt.png",
		"good_wheat"					: "./assets/goods/wheat.png",
		"good_potato"					: "./assets/goods/potato.png",
		"good_cotton"					: "./assets/goods/string.png",
		"good_rice"						: "./assets/goods/rice.png",
		"good_fur"						: "./assets/goods/leather.png",
		"good_wood"						: "./assets/goods/wood.png",
		"good_sand"						: "./assets/goods/sand.png",
		"good_stone"					: "./assets/goods/stone.png",
		"good_oil"						: "./assets/goods/barrel.png",
		"good_coal"						: "./assets/goods/coal.png",
		"good_iron"						: "./assets/goods/iron.png",
		"good_copper"					: "./assets/goods/copper.png",
		"good_precious_metal"			: "./assets/goods/diamond.png",
		"good_rare_metal"				: "./assets/goods/emerald.png",
		"good_bread"					: "./assets/goods/bread.png",
		"good_alcohol"					: "./assets/goods/beer.png",
		"good_sushi"					: "./assets/goods/sushi.png",
		"good_textile"					: "./assets/goods/part_fabric_blue.png",
		"good_clothes"					: "./assets/goods/clothes.png",
		"good_furniture"				: "./assets/goods/bookshelf.png",
		"good_steel"					: "./assets/goods/ingot_superalloy.png",
		"good_tools"					: "./assets/goods/tool_fancy_iron_hammer.png",
		"good_cement"					: "./assets/goods/cement.png",
		"good_fuel"						: "./assets/goods/part_fuelcan_full.png",
		"good_plastic"					: "./assets/goods/food_dough.png",
		"good_glass"					: "./assets/goods/glass.png",
		"good_electronics_component"	: "./assets/goods/part_electronic_chip.png",
		"good_radio"					: "./assets/goods/radio.png",
		"good_computer"					: "./assets/goods/computer.png",
		"good_guns"						: "./assets/goods/gun.png",
		"good_engine"					: "./assets/goods/engine.png",
		"good_car"						: "./assets/goods/car.png",
		"good_planes"					: "./assets/goods/plane.png",
		"good_jewelry"					: "./assets/goods/ring.png",
		"good_phone"					: "./assets/goods/phone.png",
	})


def init_tick():
	model_gameTick_game_model_tick()
	ui_drawFrame_drawFrame()
	# test_tick()



def	init_main():
	Window_init(init_setup, init_tick, events_handleEvents, input_repeatKey, input_singleKey)
	Window_start()



if __name__ == '__main__':
	init_main()
