from model.market import player_wallet
from model.market import Goods

TAXE = 0.9

market = {
	# name								   price		lot_size
	Goods.GOODS_FISH					: (1,			60),
	Goods.GOODS_SALT					: (1,			40),
	Goods.GOODS_WHEAT					: (1,			60),
	Goods.GOODS_POTATO					: (1,			50),
	Goods.GOODS_COTTON					: (1,			50),
	Goods.GOODS_RICE					: (1,			40),
	Goods.GOODS_FUR						: (3,			100),
	Goods.GOODS_WOOD					: (1,			60),
	Goods.GOODS_STONE					: (1,			55),
	Goods.GOODS_SAND					: (1,			50),
	Goods.GOODS_OIL						: (2,			30),
	Goods.GOODS_COAL					: (1,			45),
	Goods.GOODS_IRON					: (1,			30),
	Goods.GOODS_COPPER					: (1,			30),
	Goods.GOODS_PRECIOUS_METAL			: (4,		    20),
	Goods.GOODS_RARE_METAL				: (4,			20),
	Goods.GOODS_BREAD					: (1,			45),
	Goods.GOODS_ALCOHOL					: (1,			20),
	Goods.GOODS_SUSHI					: (1,			10),
	Goods.GOODS_TEXTILE					: (1,			40),
	Goods.GOODS_CLOTHES					: (1,			25),
	Goods.GOODS_FURNITURE				: (2,			35),
	Goods.GOODS_STEEL					: (2,			30),
	Goods.GOODS_TOOLS					: (15,			100),
	Goods.GOODS_CEMENT					: (1,			35),
	Goods.GOODS_FUEL					: (2,			20),
	Goods.GOODS_PLASTIC					: (20,			20),
	Goods.GOODS_GLASS					: (1,			30),
	Goods.GOODS_ELECTRONICS_COMPONENT	: (60,			20),
	Goods.GOODS_RADIO					: (4,			20),
	Goods.GOODS_COMPUTER				: (60,			10),
	Goods.GOODS_GUNS					: (40,			20),
	Goods.GOODS_ENGINE					: (60,		    20),
	Goods.GOODS_CAR						: (100,		    20),
	Goods.GOODS_PLANES					: (150,		    10),
	Goods.GOODS_JEWELRY					: (20,		    20),
	Goods.GOODS_PHONE					: (100,		    10),
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
