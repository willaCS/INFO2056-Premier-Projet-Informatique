from model.market import Goods
from model.terrain import Ressource
from ui.framework.image import drawImage


goodsMap = {
	Goods.GOODS_FISH					: ('Fish'						, drawImage('good_fish')),
	Goods.GOODS_SALT					: ('Salt'						, drawImage('good_salt')),
	Goods.GOODS_WHEAT					: ('Wheat'						, drawImage('good_wheat')),
	Goods.GOODS_POTATO					: ('Potato'						, drawImage('good_potato')),
	Goods.GOODS_COTTON					: ('Cotton'						, drawImage('good_cotton')),
	Goods.GOODS_RICE					: ('Rice'						, drawImage('good_rice')),
	Goods.GOODS_FUR						: ('Fur'						, drawImage('good_fur')),
	Goods.GOODS_WOOD					: ('Wood'						, drawImage('good_wood')),
	Goods.GOODS_OIL						: ('Oil'						, drawImage('good_oil')),
	Goods.GOODS_COAL					: ('Coal'						, drawImage('good_coal')),
	Goods.GOODS_IRON					: ('Iron'						, drawImage('good_iron')),
	Goods.GOODS_COPPER					: ('Copper'						, drawImage('good_copper')),
	Goods.GOODS_PRECIOUS_METAL			: ('Precious Metal'				, drawImage('good_precious_metal')),
	Goods.GOODS_RARE_METAL				: ('Rare Metal'					, drawImage('good_rare_metal')),
	Goods.GOODS_BREAD					: ('Bread'						, drawImage('good_bread')),
	Goods.GOODS_ALCOHOL					: ('Alcohol'					, drawImage('good_alcohol')),
	Goods.GOODS_SUSHI					: ('Sushi'						, drawImage('good_sushi')),
	Goods.GOODS_TEXTILE					: ('Textile'					, drawImage('good_textile')),
	Goods.GOODS_CLOTHES					: ('Clothes'					, drawImage('good_clothes')),
	Goods.GOODS_FURNITURE				: ('Furniture'					, drawImage('good_furniture')),
	Goods.GOODS_STEEL					: ('Steel'						, drawImage('good_steel')),
	Goods.GOODS_TOOLS					: ('Tools'						, drawImage('good_tools')),
	Goods.GOODS_CEMENT					: ('Cement'						, drawImage('good_cement')),	
	Goods.GOODS_FUEL					: ('Fuel'						, drawImage('good_fuel')),
	Goods.GOODS_PLASTIC					: ('Plastic'					, drawImage('good_plastic')),
	Goods.GOODS_GLASS					: ('Glass'						, drawImage('good_glass')),
	Goods.GOODS_ELECTRONICS_COMPONENT	: ('Electronic Components'		, drawImage('good_electronics_component')),
	Goods.GOODS_RADIO					: ('Radio'						, drawImage('good_radio')),
	Goods.GOODS_COMPUTER				: ('Computer'					, drawImage('good_computer')),
	Goods.GOODS_GUNS					: ('Guns'						, drawImage('good_guns')),
	Goods.GOODS_ENGINE					: ('Engine'						, drawImage('good_engine')),
	Goods.GOODS_CAR						: ('Car'						, drawImage('good_car')),
	Goods.GOODS_PLANES					: ('Planes'						, drawImage('good_planes')),
	Goods.GOODS_JEWELRY					: ('Jewelry'					, drawImage('good_jewelry')),
	Goods.GOODS_PHONE					: ('Phone'						, drawImage('good_phone')),
	Goods.GOODS_STONE					: ('Stone'						, drawImage('good_stone')),
	Goods.GOODS_SAND					: ('Sand'						, drawImage('good_sand')),
}


Ressource.RESSOURCE_COAL: Goods.GOODS_COAL

def print_goods(type):
	return goodsMap[type][0]

def draw_goods(type):
	return goodsMap.get(
		type,
		('', lambda rect: None)
	)[1]
