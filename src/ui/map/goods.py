from model.market import Goods
from ui.framework.draw import drawRect


goodsMap = {
	Goods.GOODS_FISH					: ('Fish'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_SALT					: ('Salt'						, lambda rect: drawRect(rect, (230, 230, 230))),
	Goods.GOODS_WHEAT					: ('Wheat'						, lambda rect: drawRect(rect, (255, 222,  19))),
	Goods.GOODS_POTATO					: ('Potato'						, lambda rect: drawRect(rect, (227, 164,  68))),
	Goods.GOODS_COTTON					: ('Cotton'						, lambda rect: drawRect(rect, (149, 255, 140))),
	Goods.GOODS_RICE					: ('Rice'						, lambda rect: drawRect(rect, (144, 228, 245))),
	Goods.GOODS_FUR						: ('Fur'						, lambda rect: drawRect(rect, (156, 105,  28))),
	Goods.GOODS_WOOD					: ('Wood'						, lambda rect: drawRect(rect, (102,  64,   7))),
	Goods.GOODS_OIL						: ('Oil'						, lambda rect: drawRect(rect, ( 80,  80,  80))),
	Goods.GOODS_COAL					: ('Coal'						, lambda rect: drawRect(rect, ( 20,  20,  20))),
	Goods.GOODS_IRON					: ('Iron'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_COPPER					: ('Copper'						, lambda rect: drawRect(rect, (255,  89,   0))),
	Goods.GOODS_PRECIOUS_METAL			: ('Precious Metal'				, lambda rect: drawRect(rect, (  0, 150, 161))),
	Goods.GOODS_RARE_METAL				: ('Rare Metal'					, lambda rect: drawRect(rect, (101, 135, 101))),
	Goods.GOODS_BREAD					: ('Bread'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_ALCOHOL					: ('Alcohol'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_SUSHI					: ('Sushi'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_TEXTILE					: ('Textile'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_CLOTHES					: ('Clothes'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_FURNITURE				: ('Furniture'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_STEEL					: ('Steel'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_TOOLS					: ('Tools'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_CEMENT					: ('Cement'						, lambda rect: drawRect(rect, (  0,   0,   0))),	
	Goods.GOODS_FUEL					: ('Fuel'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_PLASTIC					: ('Plastic'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_GLASS					: ('Glass'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_ELECTRONICS_COMPONENT	: ('Electronic Components'		, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_RADIO					: ('Radio'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_COMPUTER				: ('Computer'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_GUNS					: ('Guns'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_ENGINE					: ('Engine'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_CAR						: ('Car'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_PLANES					: ('Planes'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_JEWELRY					: ('Jewelry'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_PHONE					: ('Phone'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_STONE					: ('Stone'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Goods.GOODS_SAND					: ('Sand'						, lambda rect: drawRect(rect, (  0,   0,   0))),
}

def print_goods(type):
	return goodsMap[type][0]

def draw_goods(type):
	return goodsMap.get(
		type,
		('', lambda rect: None)
	)[1]
