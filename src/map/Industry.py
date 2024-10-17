from map import Goods


INDUSTRY_FISHINGBOAT					= 1
INDUSTRY_SALTEXTRACTION					= 2
INDUSTRY_WHEAT							= 3
INDUSTRY_POTATO							= 4
INDUSTRY_COTTON							= 5
INDUSTRY_RICE							= 6
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

industry = {
	INDUSTRY_FISHINGBOAT: {
		'input': [],
		'output': Goods.GOODS_FISH
	},
	INDUSTRY_SALTEXTRACTION: {
		'input': [],
		'output': Goods.GOODS_SALT
	},
	INDUSTRY_WHEAT: {
		'input': [],
		'output': Goods.GOODS_WHEAT
	},
	INDUSTRY_POTATO: {
		'input': [],
		'output': Goods.GOODS_POTATO
	},
	INDUSTRY_COTTON: {
		'input': [],
		'output': Goods.GOODS_COTTON
	},
	INDUSTRY_RICE: {
		'input': [],
		'output': Goods.GOODS_RICE
	},
	INDUSTRY_FURHUNTINGGROUNDS: {
		'input': [],
		'output': Goods.GOODS_FUR
	},
	INDUSTRY_LUMBERMILL: {
		'input': [],
		'output': Goods.GOODS_WOOD
	},
	INDUSTRY_OILWELL: {
		'input': [],
		'output': Goods.GOODS_OIL
	},
	INDUSTRY_STONEQUERY: {
		'input': [],
		'output': Goods.GOODS_STONE
	},
	INDUSTRY_SANDQUERY: {
		'input': [],
		'output': Goods.GOODS_SAND
	},
	INDUSTRY_COALMINE: {
		'input': [],
		'output': Goods.GOODS_COAL
	},
	INDUSTRY_IRONMINE: {
		'input': [],
		'output': Goods.GOODS_IRON
	},
	INDUSTRY_COPPERMINE: {
		'input': [],
		'output': Goods.GOODS_COPPER
	},
	INDUSTRY_PRECIOUSMETALMINE: {
		'input': [],
		'output': Goods.GOODS_PRECIOUS_METAL
	},
	INDUSTRY_RAREMETALMINE: {
		'input': [],
		'output': Goods.GOODS_RARE_METAL
	},
	INDUSTRY_BREADFACTORY: {
		'input': [
			Goods.GOODS_WHEAT,
		],
		'output': Goods.GOODS_BREAD
	},
	INDUSTRY_ALCOHOLFACTORY: {
		'input': [
			Goods.GOODS_POTATO,
		],
		'output': Goods.GOODS_ALCOHOL
	},
	INDUSTRY_SUSHIFACTORY: {
		'input': [
			Goods.GOODS_RICE,
			Goods.GOODS_SALT,
			Goods.GOODS_FISH,
		],
		'output': Goods.GOODS_SUSHI
	},
	INDUSTRY_TEXTILEFACTORY: {
		'input': [
			Goods.GOODS_COTTON,
		],
		'output': Goods.GOODS_TEXTILE
	},
	INDUSTRY_CLOTHESFACTORY: {
		'input': [
			Goods.GOODS_TEXTILE,
		],
		'output': Goods.GOODS_CLOTHES
	},
	INDUSTRY_FURNITUREFACTORY: {
		'input': [
			Goods.GOODS_WOOD,
			Goods.GOODS_IRON,
		],
		'output': Goods.GOODS_FURNITURE
	},
	INDUSTRY_STEELMILL: {
		'input': [
			Goods.GOODS_COAL,
			Goods.GOODS_IRON,
		],
		'output': Goods.GOODS_STEEL
	},
	INDUSTRY_TOOLINGFACTORY: {
		'input': [
			Goods.GOODS_STEEL,
			Goods.GOODS_WOOD,
		],
		'output': Goods.GOODS_TOOLS
	},
	INDUSTRY_CEMENTFACTORY: {
		'input': [
			Goods.GOODS_STONE,
			Goods.GOODS_SAND,
		],
		'output': Goods.GOODS_CEMENT
	},
	INDUSTRY_REFINARY: {
		'input': [
			Goods.GOODS_OIL,
		],
		'output': Goods.GOODS_FUEL
	},
	INDUSTRY_PLASTICFACTORY: {
		'input': [
			Goods.GOODS_FUEL,
		],
		'output': Goods.GOODS_PLASTIC
	},
	INDUSTRY_GLASSFACTORY: {
		'input': [
			Goods.GOODS_SAND,
		],
		'output': Goods.GOODS_GLASS
	},
	INDUSTRY_ELECTRONICCOMPONENTSFACTORY: {
		'input': [
			Goods.GOODS_COPPER,
			Goods.GOODS_RARE_METAL,
		],
		'output': Goods.GOODS_ELECTRONICS_COMPONENT
	},
	INDUSTRY_RADIOFACTORY: {
		'input': [
			Goods.GOODS_COPPER,
			Goods.GOODS_STEEL,
		],
		'output': Goods.GOODS_RADIO
	},
	INDUSTRY_COMPUTERFACTORY: {
		'input': [
			Goods.GOODS_ELECTRONICS_COMPONENT,
			Goods.GOODS_STEEL,
		],
		'output': Goods.GOODS_COMPUTER
	},
	INDUSTRY_GUNFACTORY: {
		'input': [
			Goods.GOODS_STEEL,
		],
		'output': Goods.GOODS_GUNS
	},
	INDUSTRY_ENGINEFACTORY: {
		'input': [
			Goods.GOODS_STEEL,
			Goods.GOODS_FUEL,
		],
		'output': Goods.GOODS_ENGINE
	},
	INDUSTRY_CARFACTORY: {
		'input': [
			Goods.GOODS_ENGINE,
			Goods.GOODS_STEEL,
			Goods.GOODS_GLASS
		],
		'output': Goods.GOODS_CAR
	},
	INDUSTRY_PLANESFACTORY: {
		'input': [
			Goods.GOODS_RADIO,
			Goods.GOODS_STEEL,
			Goods.GOODS_GLASS,
			Goods.GOODS_ENGINE,
		],
		'output': Goods.GOODS_PLANES
	},
	INDUSTRY_JEWELRYWORKSHOP: {
		'input': [
			Goods.GOODS_PRECIOUS_METAL
		],
		'output': Goods.GOODS_JEWELRY
	},
	INDUSTRY_PHONEFACTORY: {
		'input': [
			Goods.GOODS_COMPUTER,
			Goods.GOODS_PLASTIC,
			Goods.GOODS_GLASS,
		],
		'output': Goods.GOODS_PHONE
	},
}

print(industry)