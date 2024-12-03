from model.market import Goods
from model.terrain import Ressource
from ui.framework.image import drawImage


goodsMap = {
	Goods.GOODS_FISH					: ('Fish'						, lambda rect: drawImage('good_fish', rect)),
	Goods.GOODS_SALT					: ('Salt'						, lambda rect: drawImage('good_salt', rect)),
	Goods.GOODS_WHEAT					: ('Wheat'						, lambda rect: drawImage('good_wheat', rect)),
	Goods.GOODS_POTATO					: ('Potato'						, lambda rect: drawImage('good_potato', rect)),
	Goods.GOODS_COTTON					: ('Cotton'						, lambda rect: drawImage('good_cotton', rect)),
	Goods.GOODS_RICE					: ('Rice'						, lambda rect: drawImage('good_rice', rect)),
	Goods.GOODS_FUR						: ('Fur'						, lambda rect: drawImage('good_fur', rect)),
	Goods.GOODS_WOOD					: ('Wood'						, lambda rect: drawImage('good_wood', rect)),
	Goods.GOODS_OIL						: ('Oil'						, lambda rect: drawImage('good_oil', rect)),
	Goods.GOODS_COAL					: ('Coal'						, lambda rect: drawImage('good_coal', rect)),
	Goods.GOODS_IRON					: ('Iron'						, lambda rect: drawImage('good_iron', rect)),
	Goods.GOODS_COPPER					: ('Copper'						, lambda rect: drawImage('good_copper', rect)),
	Goods.GOODS_PRECIOUS_METAL			: ('Precious Metal'				, lambda rect: drawImage('good_precious_metal', rect)),
	Goods.GOODS_RARE_METAL				: ('Rare Metal'					, lambda rect: drawImage('good_rare_metal', rect)),
	Goods.GOODS_BREAD					: ('Bread'						, lambda rect: drawImage('good_bread', rect)),
	Goods.GOODS_ALCOHOL					: ('Alcohol'					, lambda rect: drawImage('good_alcohol', rect)),
	Goods.GOODS_SUSHI					: ('Sushi'						, lambda rect: drawImage('good_sushi', rect)),
	Goods.GOODS_TEXTILE					: ('Textile'					, lambda rect: drawImage('good_textile', rect)),
	Goods.GOODS_CLOTHES					: ('Clothes'					, lambda rect: drawImage('good_clothes', rect)),
	Goods.GOODS_FURNITURE				: ('Furniture'					, lambda rect: drawImage('good_furniture', rect)),
	Goods.GOODS_STEEL					: ('Steel'						, lambda rect: drawImage('good_steel', rect)),
	Goods.GOODS_TOOLS					: ('Tools'						, lambda rect: drawImage('good_tools', rect)),
	Goods.GOODS_CEMENT					: ('Cement'						, lambda rect: drawImage('good_cement', rect)),	
	Goods.GOODS_FUEL					: ('Fuel'						, lambda rect: drawImage('good_fuel', rect)),
	Goods.GOODS_PLASTIC					: ('Plastic'					, lambda rect: drawImage('good_plastic', rect)),
	Goods.GOODS_GLASS					: ('Glass'						, lambda rect: drawImage('good_glass', rect)),
	Goods.GOODS_ELECTRONICS_COMPONENT	: ('Electronic Components'		, lambda rect: drawImage('good_electronics_component', rect)),
	Goods.GOODS_RADIO					: ('Radio'						, lambda rect: drawImage('good_radio', rect)),
	Goods.GOODS_COMPUTER				: ('Computer'					, lambda rect: drawImage('good_computer', rect)),
	Goods.GOODS_GUNS					: ('Guns'						, lambda rect: drawImage('good_guns', rect)),
	Goods.GOODS_ENGINE					: ('Engine'						, lambda rect: drawImage('good_engine', rect)),
	Goods.GOODS_CAR						: ('Car'						, lambda rect: drawImage('good_car', rect)),
	Goods.GOODS_PLANES					: ('Planes'						, lambda rect: drawImage('good_planes', rect)),
	Goods.GOODS_JEWELRY					: ('Jewelry'					, lambda rect: drawImage('good_jewelry', rect)),
	Goods.GOODS_PHONE					: ('Phone'						, lambda rect: drawImage('good_phone', rect)),
	Goods.GOODS_STONE					: ('Stone'						, lambda rect: drawImage('good_stone', rect)),
	Goods.GOODS_SAND					: ('Sand'						, lambda rect: drawImage('good_sand', rect)),
}

ressources_to_goods_map = {
	Ressource.RESSOURCE_FISH           : [Goods.GOODS_FISH],
	Ressource.RESSOURCE_SALT           : [Goods.GOODS_SALT],
	Ressource.RESSOURCE_FERTILE_LAND   : [Goods.GOODS_WHEAT, Goods.GOODS_POTATO, Goods.GOODS_COTTON, Goods.GOODS_RICE],
	Ressource.RESSOURCE_HUNTING_GROUNDS: [Goods.GOODS_FUR],
	Ressource.RESSOURCE_WOOD           : [Goods.GOODS_WOOD],
	Ressource.RESSOURCE_OIL            : [Goods.GOODS_OIL],
	Ressource.RESSOURCE_COAL           : [Goods.GOODS_COAL],
	Ressource.RESSOURCE_IRON           : [Goods.GOODS_IRON],
	Ressource.RESSOURCE_COPPER         : [Goods.GOODS_COPPER],
	Ressource.RESSOURCE_PRECIOUS_METALS: [Goods.GOODS_PRECIOUS_METAL],
	Ressource.RESSOURCE_RARE_METALS    : [Goods.GOODS_RARE_METAL],
	Ressource.RESSOURCE_SAND           : [Goods.GOODS_SAND],
	Ressource.RESSOURCE_STONE          : [Goods.GOODS_STONE],
}
def ressources_to_goods(ressource_type):
	return ressources_to_goods_map.get(
		ressource_type,
		[]
	)

def print_goods(type):
	return goodsMap[type][0]

def draw_goods(type):
	return goodsMap.get(
		type,
		('', lambda rect: None)
	)[1]
