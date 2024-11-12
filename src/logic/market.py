from globals import player
from map import Goods

PRICE_GOODS_FISH					= 1
PRICE_GOODS_SALT					= 1
PRICE_GOODS_WHEAT					= 1
PRICE_GOODS_POTATO					= 1
PRICE_GOODS_COTTON					= 4
PRICE_GOODS_RICE					= 2
PRICE_GOODS_FUR						= 3
PRICE_GOODS_WOOD					= 1
PRICE_GOODS_OIL						= 50
PRICE_GOODS_COAL					= 5
PRICE_GOODS_IRON					= 10
PRICE_GOODS_COPPER					= 8
PRICE_GOODS_PRECIOUS_METAL			= 100
PRICE_GOODS_RARE_METAL				= 80
PRICE_GOODS_STONE					= 1
PRICE_GOODS_SAND					= 1
PRICE_GOODS_BREAD					= PRICE_GOODS_WHEAT + 2
PRICE_GOODS_ALCOHOL					= PRICE_GOODS_POTATO + 2
PRICE_GOODS_SUSHI					= PRICE_GOODS_RICE + PRICE_GOODS_SALT + PRICE_GOODS_FISH + 2
PRICE_GOODS_TEXTILE					= PRICE_GOODS_COTTON + 2
PRICE_GOODS_CLOTHES					= PRICE_GOODS_TEXTILE + 2
PRICE_GOODS_FURNITURE				= PRICE_GOODS_WOOD + PRICE_GOODS_IRON + 2
PRICE_GOODS_STEEL					= PRICE_GOODS_IRON + PRICE_GOODS_COAL + 2
PRICE_GOODS_TOOLS					= PRICE_GOODS_STEEL + 2
PRICE_GOODS_CEMENT					= PRICE_GOODS_STONE + PRICE_GOODS_SAND + 2
PRICE_GOODS_FUEL					= PRICE_GOODS_OIL + 2
PRICE_GOODS_PLASTIC					= PRICE_GOODS_FUEL + 2
PRICE_GOODS_GLASS					= PRICE_GOODS_SAND + 2
PRICE_GOODS_ELECTRONICS_COMPONENT	= PRICE_GOODS_GLASS + PRICE_GOODS_PLASTIC + PRICE_GOODS_COPPER + 2
PRICE_GOODS_RADIO					= PRICE_GOODS_STEEL + PRICE_GOODS_COPPER + 2
PRICE_GOODS_COMPUTER				= PRICE_GOODS_ELECTRONICS_COMPONENT + PRICE_GOODS_STEEL + 2
PRICE_GOODS_GUNS					= PRICE_GOODS_STEEL + 2
PRICE_GOODS_ENGINE					= PRICE_GOODS_FUEL + PRICE_GOODS_STEEL + 2
PRICE_GOODS_CAR						= PRICE_GOODS_ENGINE + PRICE_GOODS_STEEL + PRICE_GOODS_GLASS + 2
PRICE_GOODS_PLANES					= PRICE_GOODS_ENGINE + PRICE_GOODS_STEEL + PRICE_GOODS_GLASS + PRICE_GOODS_RADIO + 2
PRICE_GOODS_JEWELRY					= PRICE_GOODS_PRECIOUS_METAL + 2
PRICE_GOODS_PHONE					= PRICE_GOODS_ELECTRONICS_COMPONENT + PRICE_GOODS_PLASTIC + PRICE_GOODS_GLASS + 2




market = {
	Goods.GOODS_FISH					: PRICE_GOODS_FISH,
	Goods.GOODS_SALT					: PRICE_GOODS_SALT,
	Goods.GOODS_WHEAT					: PRICE_GOODS_WHEAT,
	Goods.GOODS_POTATO					: PRICE_GOODS_POTATO,
	Goods.GOODS_COTTON					: PRICE_GOODS_COTTON,
	Goods.GOODS_RICE					: PRICE_GOODS_RICE,
	Goods.GOODS_FUR						: PRICE_GOODS_FUR,
	Goods.GOODS_WOOD					: PRICE_GOODS_WOOD,
	Goods.GOODS_OIL						: PRICE_GOODS_OIL,
	Goods.GOODS_COAL					: PRICE_GOODS_COAL,
	Goods.GOODS_IRON					: PRICE_GOODS_IRON,
	Goods.GOODS_COPPER					: PRICE_GOODS_COPPER,
	Goods.GOODS_PRECIOUS_METAL			: PRICE_GOODS_PRECIOUS_METAL,
	Goods.GOODS_RARE_METAL				: PRICE_GOODS_RARE_METAL,
	Goods.GOODS_BREAD					: PRICE_GOODS_BREAD,
	Goods.GOODS_ALCOHOL					: PRICE_GOODS_ALCOHOL,
	Goods.GOODS_SUSHI					: PRICE_GOODS_SUSHI,
	Goods.GOODS_TEXTILE					: PRICE_GOODS_TEXTILE,
	Goods.GOODS_CLOTHES					: PRICE_GOODS_CLOTHES,
	Goods.GOODS_FURNITURE				: PRICE_GOODS_FURNITURE	,
	Goods.GOODS_STEEL					: PRICE_GOODS_STEEL,
	Goods.GOODS_TOOLS					: PRICE_GOODS_TOOLS,
	Goods.GOODS_CEMENT					: PRICE_GOODS_CEMENT,
	Goods.GOODS_FUEL					: PRICE_GOODS_FUEL,
	Goods.GOODS_PLASTIC					: PRICE_GOODS_PLASTIC,
	Goods.GOODS_GLASS					: PRICE_GOODS_GLASS,
	Goods.GOODS_ELECTRONICS_COMPONENT	: PRICE_GOODS_ELECTRONICS_COMPONENT,
	Goods.GOODS_RADIO					: PRICE_GOODS_RADIO,
	Goods.GOODS_COMPUTER				: PRICE_GOODS_COMPUTER,
	Goods.GOODS_GUNS					: PRICE_GOODS_GUNS,
	Goods.GOODS_ENGINE					: PRICE_GOODS_ENGINE,
	Goods.GOODS_CAR						: PRICE_GOODS_CAR,
	Goods.GOODS_PLANES					: PRICE_GOODS_PLANES,
	Goods.GOODS_JEWELRY					: PRICE_GOODS_JEWELRY,
	Goods.GOODS_PHONE					: PRICE_GOODS_PHONE,
	Goods.GOODS_STONE					: PRICE_GOODS_STONE,
	Goods.GOODS_SAND					: PRICE_GOODS_SAND,
}

def sell_market(goods_type, amounts):
	print('sell', amounts, 'de', Goods.print_goods(goods_type))
	player.money += market[goods_type] * amounts

def buy_market(goods_type, amounts):
	print('buy', amounts, 'de', Goods.print_goods(goods_type))
	player.money -= market[goods_type] * amounts