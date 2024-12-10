from model.market import Goods
from model.terrain import Ressource
from ui.framework.image import ui_framework_image_drawImage


ui_map_goods_goodsMap = {
	Goods.model_market_goods_GOODS_FISH					: ('Fish'						, lambda rect: ui_framework_image_drawImage('good_fish', rect)),
	Goods.model_market_goods_GOODS_SALT					: ('Salt'						, lambda rect: ui_framework_image_drawImage('good_salt', rect)),
	Goods.model_market_goods_GOODS_WHEAT					: ('Wheat'						, lambda rect: ui_framework_image_drawImage('good_wheat', rect)),
	Goods.model_market_goods_GOODS_POTATO					: ('Potato'						, lambda rect: ui_framework_image_drawImage('good_potato', rect)),
	Goods.model_market_goods_GOODS_COTTON					: ('Cotton'						, lambda rect: ui_framework_image_drawImage('good_cotton', rect)),
	Goods.model_market_goods_GOODS_RICE					: ('Rice'						, lambda rect: ui_framework_image_drawImage('good_rice', rect)),
	Goods.model_market_goods_GOODS_FUR						: ('Fur'						, lambda rect: ui_framework_image_drawImage('good_fur', rect)),
	Goods.model_market_goods_GOODS_WOOD					: ('Wood'						, lambda rect: ui_framework_image_drawImage('good_wood', rect)),
	Goods.model_market_goods_GOODS_OIL						: ('Oil'						, lambda rect: ui_framework_image_drawImage('good_oil', rect)),
	Goods.model_market_goods_GOODS_COAL					: ('Coal'						, lambda rect: ui_framework_image_drawImage('good_coal', rect)),
	Goods.model_market_goods_GOODS_IRON					: ('Iron'						, lambda rect: ui_framework_image_drawImage('good_iron', rect)),
	Goods.model_market_goods_GOODS_COPPER					: ('Copper'						, lambda rect: ui_framework_image_drawImage('good_copper', rect)),
	Goods.model_market_goods_GOODS_PRECIOUS_METAL			: ('Precious Metal'				, lambda rect: ui_framework_image_drawImage('good_precious_metal', rect)),
	Goods.model_market_goods_GOODS_RARE_METAL				: ('Rare Metal'					, lambda rect: ui_framework_image_drawImage('good_rare_metal', rect)),
	Goods.model_market_goods_GOODS_BREAD					: ('Bread'						, lambda rect: ui_framework_image_drawImage('good_bread', rect)),
	Goods.model_market_goods_GOODS_ALCOHOL					: ('Alcohol'					, lambda rect: ui_framework_image_drawImage('good_alcohol', rect)),
	Goods.model_market_goods_GOODS_SUSHI					: ('Sushi'						, lambda rect: ui_framework_image_drawImage('good_sushi', rect)),
	Goods.model_market_goods_GOODS_TEXTILE					: ('Textile'					, lambda rect: ui_framework_image_drawImage('good_textile', rect)),
	Goods.model_market_goods_GOODS_CLOTHES					: ('Clothes'					, lambda rect: ui_framework_image_drawImage('good_clothes', rect)),
	Goods.model_market_goods_GOODS_FURNITURE				: ('Furniture'					, lambda rect: ui_framework_image_drawImage('good_furniture', rect)),
	Goods.model_market_goods_GOODS_STEEL					: ('Steel'						, lambda rect: ui_framework_image_drawImage('good_steel', rect)),
	Goods.model_market_goods_GOODS_TOOLS					: ('Tools'						, lambda rect: ui_framework_image_drawImage('good_tools', rect)),
	Goods.model_market_goods_GOODS_CEMENT					: ('Cement'						, lambda rect: ui_framework_image_drawImage('good_cement', rect)),	
	Goods.model_market_goods_GOODS_FUEL					: ('Fuel'						, lambda rect: ui_framework_image_drawImage('good_fuel', rect)),
	Goods.model_market_goods_GOODS_PLASTIC					: ('Plastic'					, lambda rect: ui_framework_image_drawImage('good_plastic', rect)),
	Goods.model_market_goods_GOODS_GLASS					: ('Glass'						, lambda rect: ui_framework_image_drawImage('good_glass', rect)),
	Goods.model_market_goods_GOODS_ELECTRONICS_COMPONENT	: ('Electronic Components'		, lambda rect: ui_framework_image_drawImage('good_electronics_component', rect)),
	Goods.model_market_goods_GOODS_RADIO					: ('Radio'						, lambda rect: ui_framework_image_drawImage('good_radio', rect)),
	Goods.model_market_goods_GOODS_COMPUTER				: ('Computer'					, lambda rect: ui_framework_image_drawImage('good_computer', rect)),
	Goods.model_market_goods_GOODS_GUNS					: ('Guns'						, lambda rect: ui_framework_image_drawImage('good_guns', rect)),
	Goods.model_market_goods_GOODS_ENGINE					: ('Engine'						, lambda rect: ui_framework_image_drawImage('good_engine', rect)),
	Goods.model_market_goods_GOODS_CAR						: ('Car'						, lambda rect: ui_framework_image_drawImage('good_car', rect)),
	Goods.model_market_goods_GOODS_PLANES					: ('Planes'						, lambda rect: ui_framework_image_drawImage('good_planes', rect)),
	Goods.model_market_goods_GOODS_JEWELRY					: ('Jewelry'					, lambda rect: ui_framework_image_drawImage('good_jewelry', rect)),
	Goods.model_market_goods_GOODS_PHONE					: ('Phone'						, lambda rect: ui_framework_image_drawImage('good_phone', rect)),
	Goods.model_market_goods_GOODS_STONE					: ('Stone'						, lambda rect: ui_framework_image_drawImage('good_stone', rect)),
	Goods.model_market_goods_GOODS_SAND					: ('Sand'						, lambda rect: ui_framework_image_drawImage('good_sand', rect)),
}

ui_map_goods_ressources_to_goods_map = {
	Ressource.model_terrain_ressource_RESSOURCE_FISH           : [Goods.model_market_goods_GOODS_FISH],
	Ressource.model_terrain_ressource_RESSOURCE_SALT           : [Goods.model_market_goods_GOODS_SALT],
	Ressource.model_terrain_ressource_RESSOURCE_FERTILE_LAND   : [Goods.model_market_goods_GOODS_WHEAT, Goods.model_market_goods_GOODS_POTATO, Goods.model_market_goods_GOODS_COTTON, Goods.model_market_goods_GOODS_RICE],
	Ressource.model_terrain_ressource_RESSOURCE_HUNTING_GROUNDS: [Goods.model_market_goods_GOODS_FUR],
	Ressource.model_terrain_ressource_RESSOURCE_WOOD           : [Goods.model_market_goods_GOODS_WOOD],
	Ressource.model_terrain_ressource_RESSOURCE_OIL            : [Goods.model_market_goods_GOODS_OIL],
	Ressource.model_terrain_ressource_RESSOURCE_COAL           : [Goods.model_market_goods_GOODS_COAL],
	Ressource.model_terrain_ressource_RESSOURCE_IRON           : [Goods.model_market_goods_GOODS_IRON],
	Ressource.model_terrain_ressource_RESSOURCE_COPPER         : [Goods.model_market_goods_GOODS_COPPER],
	Ressource.model_terrain_ressource_RESSOURCE_PRECIOUS_METALS: [Goods.model_market_goods_GOODS_PRECIOUS_METAL],
	Ressource.model_terrain_ressource_RESSOURCE_RARE_METALS    : [Goods.model_market_goods_GOODS_RARE_METAL],
	Ressource.model_terrain_ressource_RESSOURCE_SAND           : [Goods.model_market_goods_GOODS_SAND],
	Ressource.model_terrain_ressource_RESSOURCE_STONE          : [Goods.model_market_goods_GOODS_STONE],
}
def ui_map_goods_ressources_to_goods(ressource_type):
	return ui_map_goods_ressources_to_goods_map.get(
		ressource_type,
		[]
	)

def ui_map_goods_print_goods(type):
	return ui_map_goods_goodsMap[type][0]

def ui_map_goods_draw_goods(type):
	return ui_map_goods_goodsMap.get(
		type,
		('', lambda rect: None)
	)[1]
