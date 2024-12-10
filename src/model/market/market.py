from model.market import player_wallet
from model.market import Goods

TAXE = 0.9

market = {
	# name								   price		lot_size
	Goods.GOODS_FISH					: (200,			1),
	Goods.GOODS_SALT					: (1,			100),
	Goods.GOODS_WHEAT					: (100000,			1),
	Goods.GOODS_POTATO					: (1,			100),
	Goods.GOODS_COTTON					: (4,			100),
	Goods.GOODS_RICE					: (2,			100),
	Goods.GOODS_FUR						: (3,			100),
	Goods.GOODS_WOOD					: (1,			60),
	Goods.GOODS_STONE					: (1,			26),
	Goods.GOODS_SAND					: (2,			30),
	Goods.GOODS_OIL						: (7,			100),
	Goods.GOODS_COAL					: (4,			20),
	Goods.GOODS_IRON					: (22,			20),
	Goods.GOODS_COPPER					: (25,			20),
	Goods.GOODS_PRECIOUS_METAL			: (2700,		20),
	Goods.GOODS_RARE_METAL				: (130,			20),
	Goods.GOODS_BREAD					: (2,			15),
	Goods.GOODS_ALCOHOL					: (35,			20),
	Goods.GOODS_SUSHI					: (30,			20),
	Goods.GOODS_TEXTILE					: (4,			30),
	Goods.GOODS_CLOTHES					: (8,			100),
	Goods.GOODS_FURNITURE				: (9,			100),
	Goods.GOODS_STEEL					: (13,			100),
	Goods.GOODS_TOOLS					: (15,			100),
	Goods.GOODS_CEMENT					: (4,			100),
	Goods.GOODS_FUEL					: (9,			100),
	Goods.GOODS_PLASTIC					: (11,			100),
	Goods.GOODS_GLASS					: (3,			100),
	Goods.GOODS_ELECTRONICS_COMPONENT	: (22,			100),
	Goods.GOODS_RADIO					: (21,			100),
	Goods.GOODS_COMPUTER				: (37,			100),
	Goods.GOODS_GUNS					: (15,			100),
	Goods.GOODS_ENGINE					: (2000,		100),
	Goods.GOODS_CAR						: (10000,		100),
	Goods.GOODS_PLANES					: (10000000000,		10),
	Goods.GOODS_JEWELRY					: (10000,		100),
	Goods.GOODS_PHONE					: (2000000000,		1),
}

def get_price(goods_type):
	return market[goods_type][0]

def get_bundle_size(goods_type):
	return market[goods_type][1]

def sell_market(goods_type, amounts):
	print('sell', amounts, 'de', Goods.print_goods(goods_type), 'au prix de', int(get_price(goods_type) * TAXE))
	player_wallet.sell(int(get_price(goods_type) * TAXE * amounts + 1))

def buy_market(goods_type, amounts):
	print('buy', amounts, 'de', Goods.print_goods(goods_type), 'au prix de', market[goods_type])
	player_wallet.buy(int(get_price(goods_type) * amounts))
