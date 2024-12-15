from model.market.Goods import GoodsType
from model.terrain.Ressource import RessourceType
from ui.framework.image import drawImage


goodsMap = {
	GoodsType.FISH					: ('Fish'						, lambda rect: drawImage('good_fish', rect)),
	GoodsType.SALT					: ('Salt'						, lambda rect: drawImage('good_salt', rect)),
	GoodsType.WHEAT					: ('Wheat'						, lambda rect: drawImage('good_wheat', rect)),
	GoodsType.POTATO				: ('Potato'						, lambda rect: drawImage('good_potato', rect)),
	GoodsType.COTTON				: ('Cotton'						, lambda rect: drawImage('good_cotton', rect)),
	GoodsType.RICE					: ('Rice'						, lambda rect: drawImage('good_rice', rect)),
	GoodsType.FUR					: ('Fur'						, lambda rect: drawImage('good_fur', rect)),
	GoodsType.WOOD					: ('Wood'						, lambda rect: drawImage('good_wood', rect)),
	GoodsType.OIL					: ('Oil'						, lambda rect: drawImage('good_oil', rect)),
	GoodsType.COAL					: ('Coal'						, lambda rect: drawImage('good_coal', rect)),
	GoodsType.IRON					: ('Iron'						, lambda rect: drawImage('good_iron', rect)),
	GoodsType.COPPER				: ('Copper'						, lambda rect: drawImage('good_copper', rect)),
	GoodsType.PRECIOUS_METAL		: ('Precious Metal'				, lambda rect: drawImage('good_precious_metal', rect)),
	GoodsType.RARE_METAL			: ('Rare Metal'					, lambda rect: drawImage('good_rare_metal', rect)),
	GoodsType.BREAD					: ('Bread'						, lambda rect: drawImage('good_bread', rect)),
	GoodsType.ALCOHOL				: ('Alcohol'					, lambda rect: drawImage('good_alcohol', rect)),
	GoodsType.SUSHI					: ('Sushi'						, lambda rect: drawImage('good_sushi', rect)),
	GoodsType.TEXTILE				: ('Textile'					, lambda rect: drawImage('good_textile', rect)),
	GoodsType.CLOTHES				: ('Clothes'					, lambda rect: drawImage('good_clothes', rect)),
	GoodsType.FURNITURE				: ('Furniture'					, lambda rect: drawImage('good_furniture', rect)),
	GoodsType.STEEL					: ('Steel'						, lambda rect: drawImage('good_steel', rect)),
	GoodsType.TOOLS					: ('Tools'						, lambda rect: drawImage('good_tools', rect)),
	GoodsType.CEMENT				: ('Cement'						, lambda rect: drawImage('good_cement', rect)),	
	GoodsType.FUEL					: ('Fuel'						, lambda rect: drawImage('good_fuel', rect)),
	GoodsType.PLASTIC				: ('Plastic'					, lambda rect: drawImage('good_plastic', rect)),
	GoodsType.GLASS					: ('Glass'						, lambda rect: drawImage('good_glass', rect)),
	GoodsType.ELECTRONICS_COMPONENT	: ('Electronic Components'		, lambda rect: drawImage('good_electronics_component', rect)),
	GoodsType.RADIO					: ('Radio'						, lambda rect: drawImage('good_radio', rect)),
	GoodsType.COMPUTER				: ('Computer'					, lambda rect: drawImage('good_computer', rect)),
	GoodsType.GUNS					: ('Guns'						, lambda rect: drawImage('good_guns', rect)),
	GoodsType.ENGINE				: ('Engine'						, lambda rect: drawImage('good_engine', rect)),
	GoodsType.CAR					: ('Car'						, lambda rect: drawImage('good_car', rect)),
	GoodsType.PLANES				: ('Planes'						, lambda rect: drawImage('good_planes', rect)),
	GoodsType.JEWELRY				: ('Jewelry'					, lambda rect: drawImage('good_jewelry', rect)),
	GoodsType.PHONE					: ('Phone'						, lambda rect: drawImage('good_phone', rect)),
	GoodsType.STONE					: ('Stone'						, lambda rect: drawImage('good_stone', rect)),
	GoodsType.SAND					: ('Sand'						, lambda rect: drawImage('good_sand', rect)),
}

ressources_to_goods_map = {
	RessourceType.FISH           : [GoodsType.FISH],
	RessourceType.SALT           : [GoodsType.SALT],
	RessourceType.FERTILE_LAND   : [GoodsType.WHEAT, GoodsType.POTATO, GoodsType.COTTON, GoodsType.RICE],
	RessourceType.HUNTING_GROUNDS: [GoodsType.FUR],
	RessourceType.WOOD           : [GoodsType.WOOD],
	RessourceType.OIL            : [GoodsType.OIL],
	RessourceType.COAL           : [GoodsType.COAL],
	RessourceType.IRON           : [GoodsType.IRON],
	RessourceType.COPPER         : [GoodsType.COPPER],
	RessourceType.PRECIOUS_METALS: [GoodsType.PRECIOUS_METAL],
	RessourceType.RARE_METALS    : [GoodsType.RARE_METAL],
	RessourceType.SAND           : [GoodsType.SAND],
	RessourceType.STONE          : [GoodsType.STONE],
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
