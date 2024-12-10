from model.market import player_wallet
from model.market import Goods

TAXE = 0.9

market = {
	# name								   price		lot_size
	Goods.GOODS_FISH					: (2,			100),
	Goods.GOODS_SALT					: (1,			100),
	Goods.GOODS_WHEAT					: (2,			1000),
	Goods.GOODS_POTATO					: (4,			100),
	Goods.GOODS_COTTON					: (4,			100),
	Goods.GOODS_RICE					: (2,			100),
	Goods.GOODS_FUR						: (3,			100),
	Goods.GOODS_WOOD					: (1,			100),
	Goods.GOODS_STONE					: (1,			100),
	Goods.GOODS_SAND					: (1,			100),
	Goods.GOODS_OIL						: (7,			100),
	Goods.GOODS_COAL					: (5,			100),
	Goods.GOODS_IRON					: (6,			100),
	Goods.GOODS_COPPER					: (6,			100),
	Goods.GOODS_PRECIOUS_METAL			: (10,			100),
	Goods.GOODS_RARE_METAL				: (8,			100),
	Goods.GOODS_BREAD					: (3,			100),
	Goods.GOODS_ALCOHOL					: (3,			100),
	Goods.GOODS_SUSHI					: (6,			100),
	Goods.GOODS_TEXTILE					: (6,			100),
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
	Goods.GOODS_PLANES					: (100000,		10),
	Goods.GOODS_JEWELRY					: (10000,		100),
	Goods.GOODS_PHONE					: (20000,		1),
}

def get_price(goods_type):
	return market[goods_type][0]

def get_bundle_size(goods_type):
	return market[goods_type][1]

def sell_market(goods_type, amounts):
	print('sell', amounts, 'de', Goods.print_goods(goods_type), 'au prix de', int(get_price(goods_type) * TAXE))
	player_wallet.sell(int(get_price(goods_type) * TAXE * amounts))

def buy_market(goods_type, amounts):
	print('buy', amounts, 'de', Goods.print_goods(goods_type), 'au prix de', market[goods_type])
	player_wallet.buy(int(get_price(goods_type) * amounts))
