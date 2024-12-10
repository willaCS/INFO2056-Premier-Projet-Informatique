from model.industry import Plant, technologies
from ui.framework import text
import ui.visual_config as vc
from ui import Screenmode, Zoom
from ui.common.buttons import ui_common_centerRightText
from ui.framework.draw import ui_framework_draw_drawRect
from ui.framework.image import ui_framework_image_drawImage
from ui.map import goods

ui_map_industry_PADDING = 10

def ui_map_industry_drawIndustryMenu(id, key):
	technology = technologies.model_technologies_get_data(id)
	def res(rect, x, technology=technology):

		ui_framework_image_drawImage('industry', rect)
		if rect[1][1] - ui_map_industry_PADDING * 2 < 1:
			return
		ui_framework_image_drawImage(key,
			((rect[0][0] + ui_map_industry_PADDING, rect[0][1] + ui_map_industry_PADDING),
			(rect[1][0] - ui_map_industry_PADDING * 2, rect[1][1] - ui_map_industry_PADDING * 2)
		))
		ui_common_centerRightText(
			(
				(
					rect[0][0],
					rect[0][1] + rect[1][1] - 20
				),
				(
					rect[1][0],
					20,
				)
			),
			'font3', '{}'.format(text.longNumber(technology['price'])), 1, (255, 255, 255)
		)
	return res

def ui_map_industry_drawIndustryMenu2(id, key):
	technology = technologies.model_technologies_get_data(id)
	def res(rect, x, technology=technology):

		ui_framework_image_drawImage('industry', rect)
		if rect[1][1] - ui_map_industry_PADDING * 2 < 1:
			return
		ui_framework_image_drawImage(key,
			((rect[0][0] + ui_map_industry_PADDING, rect[0][1] + ui_map_industry_PADDING),
			(rect[1][0] - ui_map_industry_PADDING * 2, rect[1][1] - ui_map_industry_PADDING * 2)
		))
	return res

def ui_map_industry_drawIndustryMap(key):
	def res(rect):
		match Screenmode.SCREENMODE_val:
			case Screenmode.SCREENMODE_MAIN:
				ui_framework_image_drawImage('industry', rect)
				padding = Zoom.Zoom_tile_size // 16
				if rect[1][1] - padding * 2 < 1:
					return
				ui_framework_image_drawImage(key,
					((rect[0][0] + padding, rect[0][1] + padding),
					(rect[1][0] - padding * 2, rect[1][1] - padding * 2)
				))
			case Screenmode.SCREENMODE_ECONOMY_SUPPLY:
				ui_framework_draw_drawRect(rect, (255, 255, 0))
			case _:
				ui_framework_draw_drawRect(rect, (0, 0, 0))
	return res

def ui_map_industry_drawIndustryProducts(id, key):
	technology = technologies.model_technologies_get_data(id)
	inputs = technology['input']
	output = technology['output']
	drawFuncs = [
		*(goods.ui_map_goods_draw_goods(input) for input in inputs),
		lambda rect: ui_framework_image_drawImage('arrow', rect),
		goods.ui_map_goods_draw_goods(output),
	]
	def res(rect):
		ui_framework_draw_drawRect(rect, vc.VC_BACKGROUND2, vc.VC_ROUNDING_SMOOTH)
		rectangle = (rect[1][1], rect[1][1])
		for index, func in enumerate(drawFuncs):
			func((
				(
					rect[0][0] + (rect[1][1] + vc.VC_PADDING) * index,
					rect[0][1]
				),
				rectangle
			))
		
	return res

ui_map_industry_industryPrintMap = {
technologies.model_technologies_INDUSTRY_FISHINGBOAT					: ('Fishing Boat'					, ui_map_industry_drawIndustryMap('good_fish')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_FISHINGBOAT					,'good_fish')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_FISHINGBOAT					,'good_fish')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_FISHINGBOAT					,'good_fish')					),
technologies.model_technologies_INDUSTRY_SALTEXTRACTION				: ('Salt Extraction'				, ui_map_industry_drawIndustryMap('good_salt')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_SALTEXTRACTION					,'good_salt')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_SALTEXTRACTION					,'good_salt')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_SALTEXTRACTION				,'good_salt')					),
technologies.model_technologies_INDUSTRY_WHEAT_FIELDS					: ('Wheat Fields'					, ui_map_industry_drawIndustryMap('good_wheat')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_WHEAT_FIELDS					,'good_wheat')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_WHEAT_FIELDS					,'good_wheat')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_WHEAT_FIELDS					,'good_wheat')					),
technologies.model_technologies_INDUSTRY_POTATO_FIELDS					: ('Potato Fields'					, ui_map_industry_drawIndustryMap('good_potato')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_POTATO_FIELDS					,'good_potato')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_POTATO_FIELDS					,'good_potato')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_POTATO_FIELDS					,'good_potato')					),
technologies.model_technologies_INDUSTRY_COTTON_FIELDS					: ('Cotton Fields'					, ui_map_industry_drawIndustryMap('good_cotton')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_COTTON_FIELDS					,'good_cotton')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_COTTON_FIELDS					,'good_cotton')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_COTTON_FIELDS					,'good_cotton')					),
technologies.model_technologies_INDUSTRY_RICE_FIELDS					: ('Rice Fields'					, ui_map_industry_drawIndustryMap('good_rice')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_RICE_FIELDS					,'good_rice')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_RICE_FIELDS					,'good_rice')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_RICE_FIELDS					,'good_rice')					),
technologies.model_technologies_INDUSTRY_FURHUNTINGGROUNDS				: ('Fur Hunting Grounds'			, ui_map_industry_drawIndustryMap('good_fur')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					),
technologies.model_technologies_INDUSTRY_LUMBERMILL					: ('Lumber Mill'					, ui_map_industry_drawIndustryMap('good_wood')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_LUMBERMILL						,'good_wood')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_LUMBERMILL						,'good_wood')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_LUMBERMILL					,'good_wood')					),
technologies.model_technologies_INDUSTRY_OILWELL						: ('Oil Well'						, ui_map_industry_drawIndustryMap('good_oil')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_OILWELL						,'good_oil')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_OILWELL						,'good_oil')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_OILWELL						,'good_oil')					),
technologies.model_technologies_INDUSTRY_COALMINE						: ('Coal Mine'						, ui_map_industry_drawIndustryMap('good_coal')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_COALMINE						,'good_coal')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_COALMINE						,'good_coal')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_COALMINE						,'good_coal')					),
technologies.model_technologies_INDUSTRY_IRONMINE						: ('Iron Mine'						, ui_map_industry_drawIndustryMap('good_iron')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_IRONMINE						,'good_iron')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_IRONMINE						,'good_iron')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_IRONMINE						,'good_iron')					),
technologies.model_technologies_INDUSTRY_COPPERMINE					: ('Copper Mine'					, ui_map_industry_drawIndustryMap('good_copper')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_COPPERMINE						,'good_copper')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_COPPERMINE						,'good_copper')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_COPPERMINE					,'good_copper')					),
technologies.model_technologies_INDUSTRY_PRECIOUSMETALMINE				: ('Precious Metal Mine'			, ui_map_industry_drawIndustryMap('good_precious_metal')		, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			),
technologies.model_technologies_INDUSTRY_RAREMETALMINE					: ('Rare Metal Mine'				, ui_map_industry_drawIndustryMap('good_rare_metal')			, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_RAREMETALMINE					,'good_rare_metal')				, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_RAREMETALMINE					,'good_rare_metal')				, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_RAREMETALMINE					,'good_rare_metal')				),
technologies.model_technologies_INDUSTRY_BREADFACTORY					: ('Bread Factory'					, ui_map_industry_drawIndustryMap('good_bread')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_BREADFACTORY					,'good_bread')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_BREADFACTORY					,'good_bread')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_BREADFACTORY					,'good_bread')					),
technologies.model_technologies_INDUSTRY_ALCOHOLFACTORY				: ('Alcohol Factory'				, ui_map_industry_drawIndustryMap('good_alcohol')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_ALCOHOLFACTORY					,'good_alcohol')				, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_ALCOHOLFACTORY					,'good_alcohol')				, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_ALCOHOLFACTORY				,'good_alcohol')				),
technologies.model_technologies_INDUSTRY_SUSHIFACTORY					: ('Sushi Factory'					, ui_map_industry_drawIndustryMap('good_sushi')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_SUSHIFACTORY					,'good_sushi')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_SUSHIFACTORY					,'good_sushi')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_SUSHIFACTORY					,'good_sushi')					),
technologies.model_technologies_INDUSTRY_TEXTILEFACTORY				: ('Textile Factory'				, ui_map_industry_drawIndustryMap('good_textile')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_TEXTILEFACTORY					,'good_textile')				, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_TEXTILEFACTORY					,'good_textile')				, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_TEXTILEFACTORY				,'good_textile')				),
technologies.model_technologies_INDUSTRY_CLOTHESFACTORY				: ('Clothes Factory'				, ui_map_industry_drawIndustryMap('good_clothes')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_CLOTHESFACTORY					,'good_clothes')				, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_CLOTHESFACTORY					,'good_clothes')				, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_CLOTHESFACTORY				,'good_clothes')				),
technologies.model_technologies_INDUSTRY_FURNITUREFACTORY				: ('Furniture Factory'				, ui_map_industry_drawIndustryMap('good_furniture')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_FURNITUREFACTORY				,'good_furniture')				, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_FURNITUREFACTORY				,'good_furniture')				, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_FURNITUREFACTORY				,'good_furniture')				),
technologies.model_technologies_INDUSTRY_STEELMILL						: ('Steel Mill'						, ui_map_industry_drawIndustryMap('good_steel')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_STEELMILL						,'good_steel')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_STEELMILL						,'good_steel')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_STEELMILL						,'good_steel')					),
technologies.model_technologies_INDUSTRY_TOOLINGFACTORY				: ('Tooling Factory'				, ui_map_industry_drawIndustryMap('good_tools')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_TOOLINGFACTORY					,'good_tools')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_TOOLINGFACTORY					,'good_tools')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_TOOLINGFACTORY				,'good_tools')					),
technologies.model_technologies_INDUSTRY_CEMENTFACTORY					: ('Cement Factory'					, ui_map_industry_drawIndustryMap('good_cement')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_CEMENTFACTORY					,'good_cement')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_CEMENTFACTORY					,'good_cement')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_CEMENTFACTORY					,'good_cement')					),
technologies.model_technologies_INDUSTRY_REFINARY						: ('Refinary'						, ui_map_industry_drawIndustryMap('good_fuel')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_REFINARY						,'good_fuel')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_REFINARY						,'good_fuel')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_REFINARY						,'good_fuel')					),
technologies.model_technologies_INDUSTRY_PLASTICFACTORY				: ('Plastic Factory'				, ui_map_industry_drawIndustryMap('good_plastic')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_PLASTICFACTORY					,'good_plastic')				, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_PLASTICFACTORY					,'good_plastic')				, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_PLASTICFACTORY				,'good_plastic')				),
technologies.model_technologies_INDUSTRY_GLASSFACTORY					: ('Glass Factory'					, ui_map_industry_drawIndustryMap('good_glass')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_GLASSFACTORY					,'good_glass')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_GLASSFACTORY					,'good_glass')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_GLASSFACTORY					,'good_glass')					),
technologies.model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	: ('Electronic Components Factory'	, ui_map_industry_drawIndustryMap('good_electronics_component')	, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	),
technologies.model_technologies_INDUSTRY_RADIOFACTORY					: ('Radio Factory'					, ui_map_industry_drawIndustryMap('good_radio')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_RADIOFACTORY					,'good_radio')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_RADIOFACTORY					,'good_radio')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_RADIOFACTORY					,'good_radio')					),
technologies.model_technologies_INDUSTRY_COMPUTERFACTORY				: ('Computer Factory'				, ui_map_industry_drawIndustryMap('good_computer')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_COMPUTERFACTORY				,'good_computer')				, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_COMPUTERFACTORY				,'good_computer')				, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_COMPUTERFACTORY				,'good_computer')				),
technologies.model_technologies_INDUSTRY_GUNFACTORY					: ('Gun Factory'					, ui_map_industry_drawIndustryMap('good_guns')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_GUNFACTORY						,'good_guns')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_GUNFACTORY						,'good_guns')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_GUNFACTORY					,'good_guns')					),
technologies.model_technologies_INDUSTRY_ENGINEFACTORY					: ('Engine Factory'					, ui_map_industry_drawIndustryMap('good_engine')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_ENGINEFACTORY					,'good_engine')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_ENGINEFACTORY					,'good_engine')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_ENGINEFACTORY					,'good_engine')					),
technologies.model_technologies_INDUSTRY_CARFACTORY					: ('Car Factory'					, ui_map_industry_drawIndustryMap('good_car')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_CARFACTORY						,'good_car')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_CARFACTORY						,'good_car')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_CARFACTORY					,'good_car')					),
technologies.model_technologies_INDUSTRY_PLANESFACTORY					: ('Planes Factory'					, ui_map_industry_drawIndustryMap('good_planes')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_PLANESFACTORY					,'good_planes')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_PLANESFACTORY					,'good_planes')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_PLANESFACTORY					,'good_planes')					),
technologies.model_technologies_INDUSTRY_JEWELRYWORKSHOP				: ('Jewelry Workshop'				, ui_map_industry_drawIndustryMap('good_jewelry')				, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				),
technologies.model_technologies_INDUSTRY_PHONEFACTORY					: ('Phone Factory'					, ui_map_industry_drawIndustryMap('good_phone')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_PHONEFACTORY					,'good_phone')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_PHONEFACTORY					,'good_phone')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_PHONEFACTORY					,'good_phone')					),
technologies.model_technologies_INDUSTRY_STONEQUERY					: ('Stone Query'					, ui_map_industry_drawIndustryMap('good_stone')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_STONEQUERY						,'good_stone')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_STONEQUERY						,'good_stone')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_STONEQUERY					,'good_stone')					),
technologies.model_technologies_INDUSTRY_SANDQUERY						: ('Sand Query'						, ui_map_industry_drawIndustryMap('good_sand')					, ui_map_industry_drawIndustryMenu(technologies.model_technologies_INDUSTRY_SANDQUERY						,'good_sand')					, ui_map_industry_drawIndustryProducts(technologies.model_technologies_INDUSTRY_SANDQUERY						,'good_sand')					, ui_map_industry_drawIndustryMenu2(technologies.model_technologies_INDUSTRY_SANDQUERY						,'good_sand')					),                 
}

def ui_map_industry_print_industry(industry):
	return ui_map_industry_industryPrintMap[industry][0]

def ui_map_industry_draw_industry_map(industry):
	return ui_map_industry_draw_industry_by_id(Plant.model_Plant_type(industry))[1]

def ui_map_industry_draw_industry_menu(industry_id):
	return ui_map_industry_draw_industry_by_id(industry_id)[2]

def ui_map_industry_draw_industry_menu2(industry_id):
	return ui_map_industry_draw_industry_by_id(industry_id)[4]

def ui_map_industry_draw_industry_product(industry_id):
	return ui_map_industry_draw_industry_by_id(industry_id)[3]

def ui_map_industry_draw_industry_by_id(industry_id):
	return ui_map_industry_industryPrintMap.get(
		industry_id,
		('', lambda rect: None)
	)