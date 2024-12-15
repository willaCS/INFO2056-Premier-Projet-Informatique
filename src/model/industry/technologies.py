from enum import Enum
from typing import Dict, List

from model.market.Goods import GoodsType
from model.terrain.Ressource import RessourceType
from model.terrain.TerrainTile import TerrainTileType

class IndustryType(Enum):
	NONE 						= 0
	FISHINGBOAT					= 1
	SALTEXTRACTION				= 2
	WHEAT_FIELDS				= 3
	POTATO_FIELDS				= 4
	COTTON_FIELDS				= 5
	RICE_FIELDS					= 6
	FURHUNTINGGROUNDS			= 7
	LUMBERMILL					= 8
	OILWELL						= 9
	COALMINE					= 10
	IRONMINE					= 11
	COPPERMINE					= 12
	PRECIOUSMETALMINE			= 13
	RAREMETALMINE				= 14
	BREADFACTORY				= 15
	ALCOHOLFACTORY				= 16
	SUSHIFACTORY				= 17
	TEXTILEFACTORY				= 18
	CLOTHESFACTORY				= 19
	FURNITUREFACTORY			= 20
	STEELMILL					= 21
	TOOLINGFACTORY				= 22
	CEMENTFACTORY				= 23
	REFINARY					= 24
	PLASTICFACTORY				= 25
	GLASSFACTORY				= 26
	ELECTRONICCOMPONENTSFACTORY	= 27
	RADIOFACTORY				= 28
	COMPUTERFACTORY				= 29
	GUNFACTORY					= 30
	ENGINEFACTORY				= 31
	CARFACTORY					= 32
	PLANESFACTORY				= 33
	JEWELRYWORKSHOP				= 34
	PHONEFACTORY				= 35
	STONEQUERY					= 36
	SANDQUERY					= 37

INDUSTRY_FISHINGBOAT_PRICE					= 10
INDUSTRY_SALTEXTRACTION_PRICE				= 60
INDUSTRY_WHEAT_FIELDS_PRICE					= 10
INDUSTRY_POTATO_FIELDS_PRICE				= 40
INDUSTRY_COTTON_FIELDS_PRICE				= 40
INDUSTRY_RICE_FIELDS_PRICE					= 60
INDUSTRY_FURHUNTINGGROUNDS_PRICE			= 1000
INDUSTRY_LUMBERMILL_PRICE					= 10
INDUSTRY_STONEQUERY_PRICE					= 20
INDUSTRY_SANDQUERY_PRICE					= 40
INDUSTRY_OILWELL_PRICE						= 110
INDUSTRY_COALMINE_PRICE						= 50
INDUSTRY_IRONMINE_PRICE						= 70
INDUSTRY_COPPERMINE_PRICE					= 70
INDUSTRY_PRECIOUSMETALMINE_PRICE			= 3000
INDUSTRY_RAREMETALMINE_PRICE				= 2500
INDUSTRY_BREADFACTORY_PRICE					= 50
INDUSTRY_ALCOHOLFACTORY_PRICE				= 100
INDUSTRY_SUSHIFACTORY_PRICE					= 110
INDUSTRY_TEXTILEFACTORY_PRICE				= 60
INDUSTRY_CLOTHESFACTORY_PRICE				= 80
INDUSTRY_FURNITUREFACTORY_PRICE				= 80
INDUSTRY_STEELMILL_PRICE					= 100
INDUSTRY_TOOLINGFACTORY_PRICE				= 1000
INDUSTRY_CEMENTFACTORY_PRICE				= 70
INDUSTRY_REFINARY_PRICE						= 1000
INDUSTRY_PLASTICFACTORY_PRICE				= 10000
INDUSTRY_GLASSFACTORY_PRICE					= 70
INDUSTRY_ELECTRONICCOMPONENTSFACTORY_PRICE	= 30000
INDUSTRY_RADIOFACTORY_PRICE					= 1500
INDUSTRY_COMPUTERFACTORY_PRICE				= 150000
INDUSTRY_GUNFACTORY_PRICE					= 20000
INDUSTRY_ENGINEFACTORY_PRICE				= 30000
INDUSTRY_CARFACTORY_PRICE					= 50000
INDUSTRY_PLANESFACTORY_PRICE				= 500000
INDUSTRY_JEWELRYWORKSHOP_PRICE				= 5000
INDUSTRY_PHONEFACTORY_PRICE					= 300000

class CanPlaceOn(Enum):
	RESSOURCE 	= 1
	TERRAIN		= 2

industry_type = Dict[str, List[int] | int | List[Dict[str, int]]]

industry: Dict[int, industry_type] = {
	IndustryType.FISHINGBOAT: {
		'input': [],
		'output': GoodsType.FISH,
		'price': INDUSTRY_FISHINGBOAT_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.FISH, },
		],
	},
	IndustryType.SALTEXTRACTION: {
		'input': [],
		'output': GoodsType.SALT,
		'price': INDUSTRY_SALTEXTRACTION_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.SALT, },
		],
	},
	IndustryType.WHEAT_FIELDS: {
		'input': [],
		'output': GoodsType.WHEAT,
		'price': INDUSTRY_WHEAT_FIELDS_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.FERTILE_LAND, },
		],
	},
	IndustryType.POTATO_FIELDS: {
		'input': [],
		'output': GoodsType.POTATO,
		'price': INDUSTRY_POTATO_FIELDS_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.FERTILE_LAND, },
		],
	},
	IndustryType.COTTON_FIELDS: {
		'input': [],
		'output': GoodsType.COTTON,
		'price': INDUSTRY_COTTON_FIELDS_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.FERTILE_LAND, },
		],
	},
	IndustryType.RICE_FIELDS: {
		'input': [],
		'output': GoodsType.RICE,
		'price': INDUSTRY_RICE_FIELDS_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.FERTILE_LAND, },
		],
	},
	IndustryType.FURHUNTINGGROUNDS: {
		'input': [],
		'output': GoodsType.FUR,
		'price': INDUSTRY_FURHUNTINGGROUNDS_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.HUNTING_GROUNDS, },
		],
	},
	IndustryType.LUMBERMILL: {
		'input': [],
		'output': GoodsType.WOOD,
		'price': INDUSTRY_LUMBERMILL_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.WOOD, },
		],
	},
	IndustryType.OILWELL: {
		'input': [],
		'output': GoodsType.OIL,
		'price': INDUSTRY_OILWELL_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.OIL, },
		],
	},
	IndustryType.STONEQUERY: {
		'input': [],
		'output': GoodsType.STONE,
		'price': INDUSTRY_STONEQUERY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.STONE, },
		],
	},
	IndustryType.SANDQUERY: {
		'input': [],
		'output': GoodsType.SAND,
		'price': INDUSTRY_SANDQUERY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.SAND, },
		],
	},
	IndustryType.COALMINE: {
		'input': [],
		'output': GoodsType.COAL,
		'price': INDUSTRY_COALMINE_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.COAL, },
		],
	},
	IndustryType.IRONMINE: {
		'input': [],
		'output': GoodsType.IRON,
		'price': INDUSTRY_IRONMINE_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.IRON, },
		],
	},
	IndustryType.COPPERMINE: {
		'input': [],
		'output': GoodsType.COPPER,
		'price': INDUSTRY_COPPERMINE_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.COPPER, },
		],
	},
	IndustryType.PRECIOUSMETALMINE: {
		'input': [],
		'output': GoodsType.PRECIOUS_METAL,
		'price': INDUSTRY_PRECIOUSMETALMINE_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.PRECIOUS_METALS, },
		],
	},
	IndustryType.RAREMETALMINE: {
		'input': [],
		'output': GoodsType.RARE_METAL,
		'price': INDUSTRY_RAREMETALMINE_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.RESSOURCE,	'id': RessourceType.RARE_METALS, },
		],
	},
	IndustryType.BREADFACTORY: {
		'input': [
			GoodsType.WHEAT,
		],
		'output': GoodsType.BREAD,
		'price': INDUSTRY_BREADFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.ALCOHOLFACTORY: {
		'input': [
			GoodsType.POTATO,
		],
		'output': GoodsType.ALCOHOL,
		'price': INDUSTRY_ALCOHOLFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.SUSHIFACTORY: {
		'input': [
			GoodsType.RICE,
			GoodsType.SALT,
			GoodsType.FISH,
		],
		'output': GoodsType.SUSHI,
		'price': INDUSTRY_SUSHIFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.TEXTILEFACTORY: {
		'input': [
			GoodsType.COTTON,
		],
		'output': GoodsType.TEXTILE,
		'price': INDUSTRY_TEXTILEFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.CLOTHESFACTORY: {
		'input': [
			GoodsType.TEXTILE,
		],
		'output': GoodsType.CLOTHES,
		'price': INDUSTRY_CLOTHESFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.FURNITUREFACTORY: {
		'input': [
			GoodsType.WOOD,
			GoodsType.IRON,
		],
		'output': GoodsType.FURNITURE,
		'price': INDUSTRY_FURNITUREFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.STEELMILL: {
		'input': [
			GoodsType.COAL,
			GoodsType.IRON,
		],
		'output': GoodsType.STEEL,
		'price': INDUSTRY_STEELMILL_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.TOOLINGFACTORY: {
		'input': [
			GoodsType.STEEL,
			GoodsType.WOOD,
		],
		'output': GoodsType.TOOLS,
		'price': INDUSTRY_TOOLINGFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.CEMENTFACTORY: {
		'input': [
			GoodsType.STONE,
			GoodsType.SAND,
		],
		'output': GoodsType.CEMENT,
		'price': INDUSTRY_CEMENTFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.REFINARY: {
		'input': [
			GoodsType.OIL,
		],
		'output': GoodsType.FUEL,
		'price': INDUSTRY_REFINARY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.PLASTICFACTORY: {
		'input': [
			GoodsType.FUEL,
		],
		'output': GoodsType.PLASTIC,
		'price': INDUSTRY_PLASTICFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.GLASSFACTORY: {
		'input': [
			GoodsType.SAND,
		],
		'output': GoodsType.GLASS,
		'price': INDUSTRY_GLASSFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.ELECTRONICCOMPONENTSFACTORY: {
		'input': [
			GoodsType.COPPER,
			GoodsType.RARE_METAL,
		],
		'output': GoodsType.ELECTRONICS_COMPONENT,
		'price': INDUSTRY_ELECTRONICCOMPONENTSFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.RADIOFACTORY: {
		'input': [
			GoodsType.COPPER,
			GoodsType.STEEL,
		],
		'output': GoodsType.RADIO,
		'price': INDUSTRY_RADIOFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.COMPUTERFACTORY: {
		'input': [
			GoodsType.ELECTRONICS_COMPONENT,
			GoodsType.STEEL,
		],
		'output': GoodsType.COMPUTER,
		'price': INDUSTRY_COMPUTERFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.GUNFACTORY: {
		'input': [
			GoodsType.STEEL,
		],
		'output': GoodsType.GUNS,
		'price': INDUSTRY_GUNFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.ENGINEFACTORY: {
		'input': [
			GoodsType.STEEL,
			GoodsType.FUEL,
		],
		'output': GoodsType.ENGINE,
		'price': INDUSTRY_ENGINEFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.CARFACTORY: {
		'input': [
			GoodsType.ENGINE,
			GoodsType.STEEL,
			GoodsType.GLASS
		],
		'output': GoodsType.CAR,
		'price': INDUSTRY_CARFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.PLANESFACTORY: {
		'input': [
			GoodsType.RADIO,
			GoodsType.STEEL,
			GoodsType.GLASS,
			GoodsType.ENGINE,
		],
		'output': GoodsType.PLANES,
		'price': INDUSTRY_PLANESFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.JEWELRYWORKSHOP: {
		'input': [
			GoodsType.PRECIOUS_METAL
		],
		'output': GoodsType.JEWELRY,
		'price': INDUSTRY_JEWELRYWORKSHOP_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
	IndustryType.PHONEFACTORY: {
		'input': [
			GoodsType.COMPUTER,
			GoodsType.PLASTIC,
			GoodsType.GLASS,
		],
		'output': GoodsType.PHONE,
		'price': INDUSTRY_PHONEFACTORY_PRICE,
		'place_on': [
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.BEACH, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.PLAIN, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.FOREST, },
			{ 'type': CanPlaceOn.TERRAIN,		'id': TerrainTileType.MOUNTAIN_SIDE, }
		],
	},
}

def get_data(type: int) -> industry_type:
	return industry[type]

