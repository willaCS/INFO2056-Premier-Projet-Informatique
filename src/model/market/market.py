from model.market import player_wallet
from model.market import Goods

model_market_market_TAXE = 0.9

model_market_market_market = {
	# name								   price		lot_size
	Goods.model_market_goods_GOODS_FISH					: (1,			60),
	Goods.model_market_goods_GOODS_SALT					: (4,			20),
	Goods.model_market_goods_GOODS_WHEAT					: (1,			60),
	Goods.model_market_goods_GOODS_POTATO					: (2,			28),
	Goods.model_market_goods_GOODS_COTTON					: (2,			30),
	Goods.model_market_goods_GOODS_RICE					: (2,			15),
	Goods.model_market_goods_GOODS_FUR						: (3,			100),
	Goods.model_market_goods_GOODS_WOOD					: (1,			60),
	Goods.model_market_goods_GOODS_STONE					: (1,			26),
	Goods.model_market_goods_GOODS_SAND					: (2,			30),
	Goods.model_market_goods_GOODS_OIL						: (7,			100),
	Goods.model_market_goods_GOODS_COAL					: (4,			20),
	Goods.model_market_goods_GOODS_IRON					: (22,			20),
	Goods.model_market_goods_GOODS_COPPER					: (25,			20),
	Goods.model_market_goods_GOODS_PRECIOUS_METAL			: (2700,		20),
	Goods.model_market_goods_GOODS_RARE_METAL				: (130,			20),
	Goods.model_market_goods_GOODS_BREAD					: (2,			15),
	Goods.model_market_goods_GOODS_ALCOHOL					: (35,			20),
	Goods.model_market_goods_GOODS_SUSHI					: (30,			20),
	Goods.model_market_goods_GOODS_TEXTILE					: (4,			30),
	Goods.model_market_goods_GOODS_CLOTHES					: (8,			100),
	Goods.model_market_goods_GOODS_FURNITURE				: (9,			100),
	Goods.model_market_goods_GOODS_STEEL					: (13,			100),
	Goods.model_market_goods_GOODS_TOOLS					: (15,			100),
	Goods.model_market_goods_GOODS_CEMENT					: (4,			100),
	Goods.model_market_goods_GOODS_FUEL					: (9,			100),
	Goods.model_market_goods_GOODS_PLASTIC					: (11,			100),
	Goods.model_market_goods_GOODS_GLASS					: (3,			100),
	Goods.model_market_goods_GOODS_ELECTRONICS_COMPONENT	: (22,			100),
	Goods.model_market_goods_GOODS_RADIO					: (21,			100),
	Goods.model_market_goods_GOODS_COMPUTER				: (37,			100),
	Goods.model_market_goods_GOODS_GUNS					: (15,			100),
	Goods.model_market_goods_GOODS_ENGINE					: (2000,		100),
	Goods.model_market_goods_GOODS_CAR						: (10000,		100),
	Goods.model_market_goods_GOODS_PLANES					: (100000,		10),
	Goods.model_market_goods_GOODS_JEWELRY					: (10000,		100),
	Goods.model_market_goods_GOODS_PHONE					: (20000,		1),
}

def model_market_market_get_price(goods_type):
	return model_market_market_market[goods_type][0]

def model_market_market_get_bundle_size(goods_type):
	return model_market_market_market[goods_type][1]

def model_market_market_sell_market(goods_type, amounts):
	print('sell', amounts, 'de', Goods.model_market_goods_print_goods(goods_type), 'au prix de', int(model_market_market_get_price(goods_type) * model_market_market_TAXE))
	player_wallet.model_market_wallet_sell(int(model_market_market_get_price(goods_type) * model_market_market_TAXE * amounts + 1))

def model_market_market_buy_market(goods_type, amounts):
	print('buy', amounts, 'de', Goods.model_market_goods_print_goods(goods_type), 'au prix de', model_market_market_market[goods_type])
	player_wallet.model_market_wallet_buy(int(model_market_market_get_price(goods_type) * amounts))
