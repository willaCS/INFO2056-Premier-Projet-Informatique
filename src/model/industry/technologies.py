from typing import Dict, List

from model.terrain import Ressource, TerrainTile
from model.market import Goods

INDUSTRY_NONE 							= 0
INDUSTRY_FISHINGBOAT					= 1
INDUSTRY_SALTEXTRACTION					= 2
INDUSTRY_WHEAT_FIELDS					= 3
INDUSTRY_POTATO_FIELDS					= 4
INDUSTRY_COTTON_FIELDS					= 5
INDUSTRY_RICE_FIELDS					= 6
INDUSTRY_FURHUNTINGGROUNDS				= 7
INDUSTRY_LUMBERMILL						= 8
INDUSTRY_OILWELL						= 9
INDUSTRY_COALMINE						= 10
INDUSTRY_IRONMINE						= 11
INDUSTRY_COPPERMINE						= 12
INDUSTRY_PRECIOUSMETALMINE				= 13
INDUSTRY_RAREMETALMINE					= 14
INDUSTRY_BREADFACTORY					= 15
INDUSTRY_ALCOHOLFACTORY					= 16
INDUSTRY_SUSHIFACTORY					= 17
INDUSTRY_TEXTILEFACTORY					= 18
INDUSTRY_CLOTHESFACTORY					= 19
INDUSTRY_FURNITUREFACTORY				= 20
INDUSTRY_STEELMILL						= 21
INDUSTRY_TOOLINGFACTORY					= 22
INDUSTRY_CEMENTFACTORY					= 23
INDUSTRY_REFINARY						= 24
INDUSTRY_PLASTICFACTORY					= 25
INDUSTRY_GLASSFACTORY					= 26
INDUSTRY_ELECTRONICCOMPONENTSFACTORY	= 27
INDUSTRY_RADIOFACTORY					= 28
INDUSTRY_COMPUTERFACTORY				= 29
INDUSTRY_GUNFACTORY						= 30
INDUSTRY_ENGINEFACTORY					= 31
INDUSTRY_CARFACTORY						= 32
INDUSTRY_PLANESFACTORY					= 33
INDUSTRY_JEWELRYWORKSHOP				= 34
INDUSTRY_PHONEFACTORY					= 35
INDUSTRY_STONEQUERY						= 36
INDUSTRY_SANDQUERY						= 37

INDUSTRY_WHEAT_FIELDS_PRICE					= 50
INDUSTRY_POTATO_FIELDS_PRICE				= 600
INDUSTRY_SANDQUERY_PRICE					= 800
INDUSTRY_FISHINGBOAT_PRICE					=  2200
INDUSTRY_COTTON_FIELDS_PRICE				= 8500
INDUSTRY_RICE_FIELDS_PRICE					= 15000
INDUSTRY_BREADFACTORY_PRICE					=  25000
INDUSTRY_ALCOHOLFACTORY_PRICE				= 50000
INDUSTRY_SUSHIFACTORY_PRICE					= 100000
INDUSTRY_TEXTILEFACTORY_PRICE				= 500000
INDUSTRY_CLOTHESFACTORY_PRICE				= 800000
INDUSTRY_FURNITUREFACTORY_PRICE				= 1200000
INDUSTRY_STEELMILL_PRICE					= 3000000
INDUSTRY_CEMENTFACTORY_PRICE				= 7500000
INDUSTRY_REFINARY_PRICE						= 15000000
INDUSTRY_PLASTICFACTORY_PRICE				= 3000000
INDUSTRY_GLASSFACTORY_PRICE					= 7500000
INDUSTRY_ELECTRONICCOMPONENTSFACTORY_PRICE	= 15000000
INDUSTRY_RADIOFACTORY_PRICE					= 25000000
INDUSTRY_COMPUTERFACTORY_PRICE				= 50000000
INDUSTRY_GUNFACTORY_PRICE					= 100000000
INDUSTRY_ENGINEFACTORY_PRICE				= 500000000
INDUSTRY_CARFACTORY_PRICE					= 800000000
INDUSTRY_PLANESFACTORY_PRICE				= 180000000
INDUSTRY_PHONEFACTORY_PRICE					= 2000000000000
INDUSTRY_SALTEXTRACTION_PRICE				=  1

INDUSTRY_FURHUNTINGGROUNDS_PRICE			= 1
INDUSTRY_LUMBERMILL_PRICE					= 1
INDUSTRY_STONEQUERY_PRICE					= 1
INDUSTRY_OILWELL_PRICE						= 1
INDUSTRY_COALMINE_PRICE						= 1
INDUSTRY_IRONMINE_PRICE						= 1
INDUSTRY_COPPERMINE_PRICE					= 1
INDUSTRY_PRECIOUSMETALMINE_PRICE			= 1
INDUSTRY_RAREMETALMINE_PRICE				= 1
INDUSTRY_TOOLINGFACTORY_PRICE				= 1
INDUSTRY_JEWELRYWORKSHOP_PRICE				= 2200000000

PLACE_ON_RESSOURCE = 1
PLACE_ON_TERRAIN = 2

industry_type = Dict[str, List[int] | int | List[Dict[str, int]]]

industry: Dict[int, industry_type] = {
	INDUSTRY_FISHINGBOAT: {
		'input': [],
		'output': Goods.GOODS_FISH,
		'price': INDUSTRY_FISHINGBOAT_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FISH, },
		],
	},
	INDUSTRY_SALTEXTRACTION: {
		'input': [],
		'output': Goods.GOODS_SALT,
		'price': INDUSTRY_SALTEXTRACTION_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_SALT, },
		],
	},
	INDUSTRY_WHEAT_FIELDS: {
		'input': [],
		'output': Goods.GOODS_WHEAT,
		'price': INDUSTRY_WHEAT_FIELDS_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FERTILE_LAND, },
		],
	},
	INDUSTRY_POTATO_FIELDS: {
		'input': [],
		'output': Goods.GOODS_POTATO,
		'price': INDUSTRY_POTATO_FIELDS_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FERTILE_LAND, },
		],
	},
	INDUSTRY_COTTON_FIELDS: {
		'input': [],
		'output': Goods.GOODS_COTTON,
		'price': INDUSTRY_COTTON_FIELDS_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FERTILE_LAND, },
		],
	},
	INDUSTRY_RICE_FIELDS: {
		'input': [],
		'output': Goods.GOODS_RICE,
		'price': INDUSTRY_RICE_FIELDS_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FERTILE_LAND, },
		],
	},
	INDUSTRY_FURHUNTINGGROUNDS: {
		'input': [],
		'output': Goods.GOODS_FUR,
		'price': INDUSTRY_FURHUNTINGGROUNDS_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_HUNTING_GROUNDS, },
		],
	},
	INDUSTRY_LUMBERMILL: {
		'input': [],
		'output': Goods.GOODS_WOOD,
		'price': INDUSTRY_LUMBERMILL_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_WOOD, },
		],
	},
	INDUSTRY_OILWELL: {
		'input': [],
		'output': Goods.GOODS_OIL,
		'price': INDUSTRY_OILWELL_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_OIL, },
		],
	},
	INDUSTRY_STONEQUERY: {
		'input': [],
		'output': Goods.GOODS_STONE,
		'price': INDUSTRY_STONEQUERY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_STONE, },
		],
	},
	INDUSTRY_SANDQUERY: {
		'input': [],
		'output': Goods.GOODS_SAND,
		'price': INDUSTRY_SANDQUERY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_SAND, },
		],
	},
	INDUSTRY_COALMINE: {
		'input': [],
		'output': Goods.GOODS_COAL,
		'price': INDUSTRY_COALMINE_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_COAL, },
		],
	},
	INDUSTRY_IRONMINE: {
		'input': [],
		'output': Goods.GOODS_IRON,
		'price': INDUSTRY_IRONMINE_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_IRON, },
		],
	},
	INDUSTRY_COPPERMINE: {
		'input': [],
		'output': Goods.GOODS_COPPER,
		'price': INDUSTRY_COPPERMINE_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_COPPER, },
		],
	},
	INDUSTRY_PRECIOUSMETALMINE: {
		'input': [],
		'output': Goods.GOODS_PRECIOUS_METAL,
		'price': INDUSTRY_PRECIOUSMETALMINE_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_PRECIOUS_METALS, },
		],
	},
	INDUSTRY_RAREMETALMINE: {
		'input': [],
		'output': Goods.GOODS_RARE_METAL,
		'price': INDUSTRY_RAREMETALMINE_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_RARE_METALS, },
		],
	},
	INDUSTRY_BREADFACTORY: {
		'input': [
			Goods.GOODS_WHEAT,
		],
		'output': Goods.GOODS_BREAD,
		'price': INDUSTRY_BREADFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_ALCOHOLFACTORY: {
		'input': [
			Goods.GOODS_POTATO,
		],
		'output': Goods.GOODS_ALCOHOL,
		'price': INDUSTRY_ALCOHOLFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_SUSHIFACTORY: {
		'input': [
			Goods.GOODS_RICE,
			Goods.GOODS_SALT,
			Goods.GOODS_FISH,
		],
		'output': Goods.GOODS_SUSHI,
		'price': INDUSTRY_SUSHIFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_TEXTILEFACTORY: {
		'input': [
			Goods.GOODS_COTTON,
		],
		'output': Goods.GOODS_TEXTILE,
		'price': INDUSTRY_TEXTILEFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_CLOTHESFACTORY: {
		'input': [
			Goods.GOODS_TEXTILE,
		],
		'output': Goods.GOODS_CLOTHES,
		'price': INDUSTRY_CLOTHESFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_FURNITUREFACTORY: {
		'input': [
			Goods.GOODS_WOOD,
			Goods.GOODS_IRON,
		],
		'output': Goods.GOODS_FURNITURE,
		'price': INDUSTRY_FURNITUREFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_STEELMILL: {
		'input': [
			Goods.GOODS_COAL,
			Goods.GOODS_IRON,
		],
		'output': Goods.GOODS_STEEL,
		'price': INDUSTRY_STEELMILL_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_TOOLINGFACTORY: {
		'input': [
			Goods.GOODS_STEEL,
			Goods.GOODS_WOOD,
		],
		'output': Goods.GOODS_TOOLS,
		'price': INDUSTRY_TOOLINGFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_CEMENTFACTORY: {
		'input': [
			Goods.GOODS_STONE,
			Goods.GOODS_SAND,
		],
		'output': Goods.GOODS_CEMENT,
		'price': INDUSTRY_CEMENTFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_REFINARY: {
		'input': [
			Goods.GOODS_OIL,
		],
		'output': Goods.GOODS_FUEL,
		'price': INDUSTRY_REFINARY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_PLASTICFACTORY: {
		'input': [
			Goods.GOODS_FUEL,
		],
		'output': Goods.GOODS_PLASTIC,
		'price': INDUSTRY_PLASTICFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_GLASSFACTORY: {
		'input': [
			Goods.GOODS_SAND,
		],
		'output': Goods.GOODS_GLASS,
		'price': INDUSTRY_GLASSFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_ELECTRONICCOMPONENTSFACTORY: {
		'input': [
			Goods.GOODS_COPPER,
			Goods.GOODS_RARE_METAL,
		],
		'output': Goods.GOODS_ELECTRONICS_COMPONENT,
		'price': INDUSTRY_ELECTRONICCOMPONENTSFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_RADIOFACTORY: {
		'input': [
			Goods.GOODS_COPPER,
			Goods.GOODS_STEEL,
		],
		'output': Goods.GOODS_RADIO,
		'price': INDUSTRY_RADIOFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_COMPUTERFACTORY: {
		'input': [
			Goods.GOODS_ELECTRONICS_COMPONENT,
			Goods.GOODS_STEEL,
		],
		'output': Goods.GOODS_COMPUTER,
		'price': INDUSTRY_COMPUTERFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_GUNFACTORY: {
		'input': [
			Goods.GOODS_STEEL,
		],
		'output': Goods.GOODS_GUNS,
		'price': INDUSTRY_GUNFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_ENGINEFACTORY: {
		'input': [
			Goods.GOODS_STEEL,
			Goods.GOODS_FUEL,
		],
		'output': Goods.GOODS_ENGINE,
		'price': INDUSTRY_ENGINEFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_CARFACTORY: {
		'input': [
			Goods.GOODS_ENGINE,
			Goods.GOODS_STEEL,
			Goods.GOODS_GLASS
		],
		'output': Goods.GOODS_CAR,
		'price': INDUSTRY_CARFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_PLANESFACTORY: {
		'input': [
			Goods.GOODS_RADIO,
			Goods.GOODS_STEEL,
			Goods.GOODS_GLASS,
			Goods.GOODS_ENGINE,
		],
		'output': Goods.GOODS_PLANES,
		'price': INDUSTRY_PLANESFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_JEWELRYWORKSHOP: {
		'input': [
			Goods.GOODS_PRECIOUS_METAL
		],
		'output': Goods.GOODS_JEWELRY,
		'price': INDUSTRY_JEWELRYWORKSHOP_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	INDUSTRY_PHONEFACTORY: {
		'input': [
			Goods.GOODS_COMPUTER,
			Goods.GOODS_PLASTIC,
			Goods.GOODS_GLASS,
		],
		'output': Goods.GOODS_PHONE,
		'price': INDUSTRY_PHONEFACTORY_PRICE,
		'place_on': [
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_BEACH, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_PLAIN, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_FOREST, },
			{ 'type': PLACE_ON_TERRAIN,		'id': TerrainTile.TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
}

def get_data(type: int) -> industry_type:
	return industry[type]

