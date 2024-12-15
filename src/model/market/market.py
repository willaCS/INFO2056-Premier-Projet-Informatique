from model.market import player_wallet
from model.market.Goods import GoodsType, print_goods

TAXE = 0.9

market = {
	# name							  price		lot_size
	GoodsType.FISH					: (1,			60),
	GoodsType.SALT					: (1,			40),
	GoodsType.WHEAT					: (1,			60),
	GoodsType.POTATO				: (1,			50),
	GoodsType.COTTON				: (1,			50),
	GoodsType.RICE					: (1,			40),
	GoodsType.FUR					: (3,			100),
	GoodsType.WOOD					: (1,			60),
	GoodsType.STONE					: (1,			55),
	GoodsType.SAND					: (1,			50),
	GoodsType.OIL					: (2,			30),
	GoodsType.COAL					: (1,			45),
	GoodsType.IRON					: (1,			30),
	GoodsType.COPPER				: (1,			30),
	GoodsType.PRECIOUS_METAL		: (4,		    20),
	GoodsType.RARE_METAL			: (4,			20),
	GoodsType.BREAD					: (1,			45),
	GoodsType.ALCOHOL				: (1,			20),
	GoodsType.SUSHI					: (1,			10),
	GoodsType.TEXTILE				: (1,			40),
	GoodsType.CLOTHES				: (1,			25),
	GoodsType.FURNITURE				: (2,			35),
	GoodsType.STEEL					: (2,			30),
	GoodsType.TOOLS					: (15,			100),
	GoodsType.CEMENT				: (1,			35),
	GoodsType.FUEL					: (2,			20),
	GoodsType.PLASTIC				: (20,			20),
	GoodsType.GLASS					: (1,			30),
	GoodsType.ELECTRONICS_COMPONENT	: (60,			20),
	GoodsType.RADIO					: (4,			20),
	GoodsType.COMPUTER				: (60,			10),
	GoodsType.GUNS					: (40,			20),
	GoodsType.ENGINE				: (60,		    20),
	GoodsType.CAR					: (100,		    20),
	GoodsType.PLANES				: (150,		    10),
	GoodsType.JEWELRY				: (20,		    20),
	GoodsType.PHONE					: (100,		    10),
}

def get_price(goods_type):
	return market[goods_type][0]

def get_bundle_size(goods_type):
	return market[goods_type][1]

def sell_market(goods_type, amounts):
	print('sell', amounts, 'de', print_goods(goods_type), 'au prix de', int(get_price(goods_type) * TAXE))
	player_wallet.sell(int(get_price(goods_type) * TAXE * amounts + 1))

def buy_market(goods_type, amounts):
	print('buy', amounts, 'de', print_goods(goods_type), 'au prix de', market[goods_type])
	player_wallet.buy(int(get_price(goods_type) * amounts))
