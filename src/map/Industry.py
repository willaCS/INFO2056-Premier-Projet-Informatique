from typing import Dict, List
from map import Goods, Ressource, TerrainTile

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

PLACE_ON_RESSOURCE = 1
PLACE_ON_TERRAIN = 2

industry_type = Dict[str, List[int] | int | List[Dict[str, int]]]

industry: Dict[int, industry_type] = {
	INDUSTRY_FISHINGBOAT: {
		'input': [],
		'output': Goods.GOODS_FISH,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FISH, },
		],
	},
	INDUSTRY_SALTEXTRACTION: {
		'input': [],
		'output': Goods.GOODS_SALT,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_SALT, },
		],
	},
	INDUSTRY_WHEAT_FIELDS: {
		'input': [],
		'output': Goods.GOODS_WHEAT,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FERTILE_LAND, },
		],
	},
	INDUSTRY_POTATO_FIELDS: {
		'input': [],
		'output': Goods.GOODS_POTATO,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FERTILE_LAND, },
		],
	},
	INDUSTRY_COTTON_FIELDS: {
		'input': [],
		'output': Goods.GOODS_COTTON,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FERTILE_LAND, },
		],
	},
	INDUSTRY_RICE_FIELDS: {
		'input': [],
		'output': Goods.GOODS_RICE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_FERTILE_LAND, },
		],
	},
	INDUSTRY_FURHUNTINGGROUNDS: {
		'input': [],
		'output': Goods.GOODS_FUR,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_HUNTING_GROUNDS, },
		],
	},
	INDUSTRY_LUMBERMILL: {
		'input': [],
		'output': Goods.GOODS_WOOD,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_WOOD, },
		],
	},
	INDUSTRY_OILWELL: {
		'input': [],
		'output': Goods.GOODS_OIL,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_OIL, },
		],
	},
	INDUSTRY_STONEQUERY: {
		'input': [],
		'output': Goods.GOODS_STONE,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_STONE, },
		],
	},
	INDUSTRY_SANDQUERY: {
		'input': [],
		'output': Goods.GOODS_SAND,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_SAND, },
		],
	},
	INDUSTRY_COALMINE: {
		'input': [],
		'output': Goods.GOODS_COAL,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_COAL, },
		],
	},
	INDUSTRY_IRONMINE: {
		'input': [],
		'output': Goods.GOODS_IRON,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_IRON, },
		],
	},
	INDUSTRY_COPPERMINE: {
		'input': [],
		'output': Goods.GOODS_COPPER,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_COPPER, },
		],
	},
	INDUSTRY_PRECIOUSMETALMINE: {
		'input': [],
		'output': Goods.GOODS_PRECIOUS_METAL,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_PRECIOUS_METALS, },
		],
	},
	INDUSTRY_RAREMETALMINE: {
		'input': [],
		'output': Goods.GOODS_RARE_METAL,
		'place_on': [
			{ 'type': PLACE_ON_RESSOURCE,	'id': Ressource.RESSOURCE_RARE_METALS, },
		],
	},
	INDUSTRY_BREADFACTORY: {
		'input': [
			Goods.GOODS_WHEAT,
		],
		'output': Goods.GOODS_BREAD,
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

TRANSPORT_ROAD							= 1
TRANSPORT_RAILWAY						= 2

TRANSPORT_HUB_TRUCK						= 1
TRANSPORT_HUB_RAILWAY_STATION			= 2
TRANSPORT_HUB_HARBOR					= 3
