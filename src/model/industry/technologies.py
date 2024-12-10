from typing import Dict, List

from model.terrain import Ressource, TerrainTile
from model.market import Goods

model_technologies_INDUSTRY_NONE 							= 0
model_technologies_INDUSTRY_FISHINGBOAT					= 1
model_technologies_INDUSTRY_SALTEXTRACTION					= 2
model_technologies_INDUSTRY_WHEAT_FIELDS					= 3
model_technologies_INDUSTRY_POTATO_FIELDS					= 4
model_technologies_INDUSTRY_COTTON_FIELDS					= 5
model_technologies_INDUSTRY_RICE_FIELDS					= 6
model_technologies_INDUSTRY_FURHUNTINGGROUNDS				= 7
model_technologies_INDUSTRY_LUMBERMILL						= 8
model_technologies_INDUSTRY_OILWELL						= 9
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
model_technologies_INDUSTRY_COMPUTERFACTORY				= 29
model_technologies_INDUSTRY_GUNFACTORY						= 30
model_technologies_INDUSTRY_ENGINEFACTORY					= 31
model_technologies_INDUSTRY_CARFACTORY						= 32
model_technologies_INDUSTRY_PLANESFACTORY					= 33
model_technologies_INDUSTRY_JEWELRYWORKSHOP				= 34
model_technologies_INDUSTRY_PHONEFACTORY					= 35
model_technologies_INDUSTRY_STONEQUERY						= 36
model_technologies_INDUSTRY_SANDQUERY						= 37

model_technologies_INDUSTRY_FISHINGBOAT_PRICE					= 10
model_technologies_INDUSTRY_SALTEXTRACTION_PRICE				= 60
model_technologies_INDUSTRY_WHEAT_FIELDS_PRICE					= 10
model_technologies_INDUSTRY_POTATO_FIELDS_PRICE				= 40
model_technologies_INDUSTRY_COTTON_FIELDS_PRICE				= 40
model_technologies_INDUSTRY_RICE_FIELDS_PRICE					= 60
model_technologies_INDUSTRY_FURHUNTINGGROUNDS_PRICE			= 1000
model_technologies_INDUSTRY_LUMBERMILL_PRICE					= 10
model_technologies_INDUSTRY_STONEQUERY_PRICE					= 20
model_technologies_INDUSTRY_SANDQUERY_PRICE					= 40
model_technologies_INDUSTRY_OILWELL_PRICE						= 1000
model_technologies_INDUSTRY_COALMINE_PRICE						= 100
model_technologies_INDUSTRY_IRONMINE_PRICE						= 500
model_technologies_INDUSTRY_COPPERMINE_PRICE					= 500
model_technologies_INDUSTRY_PRECIOUSMETALMINE_PRICE			= 50000
model_technologies_INDUSTRY_RAREMETALMINE_PRICE				= 2500
model_technologies_INDUSTRY_BREADFACTORY_PRICE					= 60
model_technologies_INDUSTRY_ALCOHOLFACTORY_PRICE				= 750
model_technologies_INDUSTRY_SUSHIFACTORY_PRICE					= 600
model_technologies_INDUSTRY_TEXTILEFACTORY_PRICE				= 60
model_technologies_INDUSTRY_CLOTHESFACTORY_PRICE				= 1000
model_technologies_INDUSTRY_FURNITUREFACTORY_PRICE				= 100
model_technologies_INDUSTRY_STEELMILL_PRICE					= 1000
model_technologies_INDUSTRY_TOOLINGFACTORY_PRICE				= 1000
model_technologies_INDUSTRY_CEMENTFACTORY_PRICE				= 1000
model_technologies_INDUSTRY_REFINARY_PRICE						= 1000
model_technologies_INDUSTRY_PLASTICFACTORY_PRICE				= 1000
model_technologies_INDUSTRY_GLASSFACTORY_PRICE					= 1000
model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY_PRICE	= 1000
model_technologies_INDUSTRY_RADIOFACTORY_PRICE					= 1000
model_technologies_INDUSTRY_COMPUTERFACTORY_PRICE				= 5000000
model_technologies_INDUSTRY_GUNFACTORY_PRICE					= 25000
model_technologies_INDUSTRY_ENGINEFACTORY_PRICE				= 500000
model_technologies_INDUSTRY_CARFACTORY_PRICE					= 1000000
model_technologies_INDUSTRY_PLANESFACTORY_PRICE				= 1000000000
model_technologies_INDUSTRY_JEWELRYWORKSHOP_PRICE				= 1000
model_technologies_INDUSTRY_PHONEFACTORY_PRICE					= 10000000

model_technologies_PLACE_ON_RESSOURCE = 1
model_technologies_PLACE_ON_TERRAIN = 2

model_technologies_industry_type = Dict[str, List[int] | int | List[Dict[str, int]]]

model_technologies_industry: Dict[int, model_technologies_industry_type] = {
	model_technologies_INDUSTRY_FISHINGBOAT: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_FISH,
		'price': model_technologies_INDUSTRY_FISHINGBOAT_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_FISH, },
		],
	},
	model_technologies_INDUSTRY_SALTEXTRACTION: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_SALT,
		'price': model_technologies_INDUSTRY_SALTEXTRACTION_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_SALT, },
		],
	},
	model_technologies_INDUSTRY_WHEAT_FIELDS: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_WHEAT,
		'price': model_technologies_INDUSTRY_WHEAT_FIELDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_FERTILE_LAND, },
		],
	},
	model_technologies_INDUSTRY_POTATO_FIELDS: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_POTATO,
		'price': model_technologies_INDUSTRY_POTATO_FIELDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_FERTILE_LAND, },
		],
	},
	model_technologies_INDUSTRY_COTTON_FIELDS: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_COTTON,
		'price': model_technologies_INDUSTRY_COTTON_FIELDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_FERTILE_LAND, },
		],
	},
	model_technologies_INDUSTRY_RICE_FIELDS: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_RICE,
		'price': model_technologies_INDUSTRY_RICE_FIELDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_FERTILE_LAND, },
		],
	},
	model_technologies_INDUSTRY_FURHUNTINGGROUNDS: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_FUR,
		'price': model_technologies_INDUSTRY_FURHUNTINGGROUNDS_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_HUNTING_GROUNDS, },
		],
	},
	model_technologies_INDUSTRY_LUMBERMILL: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_WOOD,
		'price': model_technologies_INDUSTRY_LUMBERMILL_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_WOOD, },
		],
	},
	model_technologies_INDUSTRY_OILWELL: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_OIL,
		'price': model_technologies_INDUSTRY_OILWELL_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_OIL, },
		],
	},
	model_technologies_INDUSTRY_STONEQUERY: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_STONE,
		'price': model_technologies_INDUSTRY_STONEQUERY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_STONE, },
		],
	},
	model_technologies_INDUSTRY_SANDQUERY: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_SAND,
		'price': model_technologies_INDUSTRY_SANDQUERY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_SAND, },
		],
	},
	model_technologies_INDUSTRY_COALMINE: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_COAL,
		'price': model_technologies_INDUSTRY_COALMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_COAL, },
		],
	},
	model_technologies_INDUSTRY_IRONMINE: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_IRON,
		'price': model_technologies_INDUSTRY_IRONMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_IRON, },
		],
	},
	model_technologies_INDUSTRY_COPPERMINE: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_COPPER,
		'price': model_technologies_INDUSTRY_COPPERMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_COPPER, },
		],
	},
	model_technologies_INDUSTRY_PRECIOUSMETALMINE: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_PRECIOUS_METAL,
		'price': model_technologies_INDUSTRY_PRECIOUSMETALMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_PRECIOUS_METALS, },
		],
	},
	model_technologies_INDUSTRY_RAREMETALMINE: {
		'input': [],
		'output': Goods.model_market_goods_GOODS_RARE_METAL,
		'price': model_technologies_INDUSTRY_RAREMETALMINE_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_RESSOURCE,	'id': Ressource.model_terrain_ressource_RESSOURCE_RARE_METALS, },
		],
	},
	model_technologies_INDUSTRY_BREADFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_WHEAT,
		],
		'output': Goods.model_market_goods_GOODS_BREAD,
		'price': model_technologies_INDUSTRY_BREADFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_ALCOHOLFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_POTATO,
		],
		'output': Goods.model_market_goods_GOODS_ALCOHOL,
		'price': model_technologies_INDUSTRY_ALCOHOLFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_SUSHIFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_RICE,
			Goods.model_market_goods_GOODS_SALT,
			Goods.model_market_goods_GOODS_FISH,
		],
		'output': Goods.model_market_goods_GOODS_SUSHI,
		'price': model_technologies_INDUSTRY_SUSHIFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_TEXTILEFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_COTTON,
		],
		'output': Goods.model_market_goods_GOODS_TEXTILE,
		'price': model_technologies_INDUSTRY_TEXTILEFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_CLOTHESFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_TEXTILE,
		],
		'output': Goods.model_market_goods_GOODS_CLOTHES,
		'price': model_technologies_INDUSTRY_CLOTHESFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_FURNITUREFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_WOOD,
			Goods.model_market_goods_GOODS_IRON,
		],
		'output': Goods.model_market_goods_GOODS_FURNITURE,
		'price': model_technologies_INDUSTRY_FURNITUREFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_STEELMILL: {
		'input': [
			Goods.model_market_goods_GOODS_COAL,
			Goods.model_market_goods_GOODS_IRON,
		],
		'output': Goods.model_market_goods_GOODS_STEEL,
		'price': model_technologies_INDUSTRY_STEELMILL_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_TOOLINGFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_STEEL,
			Goods.model_market_goods_GOODS_WOOD,
		],
		'output': Goods.model_market_goods_GOODS_TOOLS,
		'price': model_technologies_INDUSTRY_TOOLINGFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_CEMENTFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_STONE,
			Goods.model_market_goods_GOODS_SAND,
		],
		'output': Goods.model_market_goods_GOODS_CEMENT,
		'price': model_technologies_INDUSTRY_CEMENTFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_REFINARY: {
		'input': [
			Goods.model_market_goods_GOODS_OIL,
		],
		'output': Goods.model_market_goods_GOODS_FUEL,
		'price': model_technologies_INDUSTRY_REFINARY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_PLASTICFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_FUEL,
		],
		'output': Goods.model_market_goods_GOODS_PLASTIC,
		'price': model_technologies_INDUSTRY_PLASTICFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_GLASSFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_SAND,
		],
		'output': Goods.model_market_goods_GOODS_GLASS,
		'price': model_technologies_INDUSTRY_GLASSFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_COPPER,
			Goods.model_market_goods_GOODS_RARE_METAL,
		],
		'output': Goods.model_market_goods_GOODS_ELECTRONICS_COMPONENT,
		'price': model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_RADIOFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_COPPER,
			Goods.model_market_goods_GOODS_STEEL,
		],
		'output': Goods.model_market_goods_GOODS_RADIO,
		'price': model_technologies_INDUSTRY_RADIOFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_COMPUTERFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_ELECTRONICS_COMPONENT,
			Goods.model_market_goods_GOODS_STEEL,
		],
		'output': Goods.model_market_goods_GOODS_COMPUTER,
		'price': model_technologies_INDUSTRY_COMPUTERFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_GUNFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_STEEL,
		],
		'output': Goods.model_market_goods_GOODS_GUNS,
		'price': model_technologies_INDUSTRY_GUNFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_ENGINEFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_STEEL,
			Goods.model_market_goods_GOODS_FUEL,
		],
		'output': Goods.model_market_goods_GOODS_ENGINE,
		'price': model_technologies_INDUSTRY_ENGINEFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_CARFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_ENGINE,
			Goods.model_market_goods_GOODS_STEEL,
			Goods.model_market_goods_GOODS_GLASS
		],
		'output': Goods.model_market_goods_GOODS_CAR,
		'price': model_technologies_INDUSTRY_CARFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_PLANESFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_RADIO,
			Goods.model_market_goods_GOODS_STEEL,
			Goods.model_market_goods_GOODS_GLASS,
			Goods.model_market_goods_GOODS_ENGINE,
		],
		'output': Goods.model_market_goods_GOODS_PLANES,
		'price': model_technologies_INDUSTRY_PLANESFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_JEWELRYWORKSHOP: {
		'input': [
			Goods.model_market_goods_GOODS_PRECIOUS_METAL
		],
		'output': Goods.model_market_goods_GOODS_JEWELRY,
		'price': model_technologies_INDUSTRY_JEWELRYWORKSHOP_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
	model_technologies_INDUSTRY_PHONEFACTORY: {
		'input': [
			Goods.model_market_goods_GOODS_COMPUTER,
			Goods.model_market_goods_GOODS_PLASTIC,
			Goods.model_market_goods_GOODS_GLASS,
		],
		'output': Goods.model_market_goods_GOODS_PHONE,
		'price': model_technologies_INDUSTRY_PHONEFACTORY_PRICE,
		'place_on': [
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_BEACH, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_PLAIN, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_FOREST, },
			{ 'type': model_technologies_PLACE_ON_TERRAIN,		'id': TerrainTile.model_terrain_terrainTile_TERRAINTILETYPE_MOUNTAIN_SIDE, }
		],
	},
}

def model_technologies_get_data(type: int) -> model_technologies_industry_type:
	return model_technologies_industry[type]

