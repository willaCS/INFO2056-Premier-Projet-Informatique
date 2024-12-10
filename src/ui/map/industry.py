from model.industry import Plant, technologies
from ui.framework import text
import ui.visual_config as vc
from ui import Screenmode, Zoom
from ui.common.buttons import centerRightText
from ui.framework.draw import drawRect
from ui.framework.image import drawImage
from ui.map import goods

PADDING = 10

def drawIndustryMenu(id, key):
	technology = technologies.get_data(id)
	def res(rect, x, technology=technology):

		drawImage('industry', rect)
		if rect[1][1] - PADDING * 2 < 1:
			return
		drawImage(key,
			((rect[0][0] + PADDING, rect[0][1] + PADDING),
			(rect[1][0] - PADDING * 2, rect[1][1] - PADDING * 2)
		))
		centerRightText(
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

def drawIndustryMenu2(id, key):
	technology = technologies.get_data(id)
	def res(rect, x, technology=technology):

		drawImage('industry', rect)
		if rect[1][1] - PADDING * 2 < 1:
			return
		drawImage(key,
			((rect[0][0] + PADDING, rect[0][1] + PADDING),
			(rect[1][0] - PADDING * 2, rect[1][1] - PADDING * 2)
		))
	return res

def drawIndustryMap(key):
	def res(rect):
		match Screenmode.val:
			case Screenmode.SCREENMODE_MAIN:
				drawImage('industry', rect)
				padding = Zoom.tile_size // 16
				if rect[1][1] - padding * 2 < 1:
					return
				drawImage(key,
					((rect[0][0] + padding, rect[0][1] + padding),
					(rect[1][0] - padding * 2, rect[1][1] - padding * 2)
				))
			case Screenmode.SCREENMODE_ECONOMY_SUPPLY:
				drawRect(rect, (255, 255, 0))
			case _:
				drawRect(rect, (0, 0, 0))
	return res

def drawIndustryProducts(id, key):
	technology = technologies.get_data(id)
	inputs = technology['input']
	output = technology['output']
	drawFuncs = [
		*(goods.draw_goods(input) for input in inputs),
		lambda rect: drawImage('arrow', rect),
		goods.draw_goods(output),
	]
	def res(rect):
		drawRect(rect, vc.BACKGROUND2, vc.ROUNDING_SMOOTH)
		rectangle = (rect[1][1], rect[1][1])
		for index, func in enumerate(drawFuncs):
			func((
				(
					rect[0][0] + (rect[1][1] + vc.PADDING) * index,
					rect[0][1]
				),
				rectangle
			))
		
	return res

industryPrintMap = {
technologies.INDUSTRY_FISHINGBOAT					: ('Fishing Boat'					, drawIndustryMap('good_fish')					, drawIndustryMenu(technologies.INDUSTRY_FISHINGBOAT					,'good_fish')					, drawIndustryProducts(technologies.INDUSTRY_FISHINGBOAT					,'good_fish')					, drawIndustryMenu2(technologies.INDUSTRY_FISHINGBOAT					,'good_fish')					),
technologies.INDUSTRY_SALTEXTRACTION				: ('Salt Extraction'				, drawIndustryMap('good_salt')					, drawIndustryMenu(technologies.INDUSTRY_SALTEXTRACTION					,'good_salt')					, drawIndustryProducts(technologies.INDUSTRY_SALTEXTRACTION					,'good_salt')					, drawIndustryMenu2(technologies.INDUSTRY_SALTEXTRACTION				,'good_salt')					),
technologies.INDUSTRY_WHEAT_FIELDS					: ('Wheat Fields'					, drawIndustryMap('good_wheat')					, drawIndustryMenu(technologies.INDUSTRY_WHEAT_FIELDS					,'good_wheat')					, drawIndustryProducts(technologies.INDUSTRY_WHEAT_FIELDS					,'good_wheat')					, drawIndustryMenu2(technologies.INDUSTRY_WHEAT_FIELDS					,'good_wheat')					),
technologies.INDUSTRY_POTATO_FIELDS					: ('Potato Fields'					, drawIndustryMap('good_potato')				, drawIndustryMenu(technologies.INDUSTRY_POTATO_FIELDS					,'good_potato')					, drawIndustryProducts(technologies.INDUSTRY_POTATO_FIELDS					,'good_potato')					, drawIndustryMenu2(technologies.INDUSTRY_POTATO_FIELDS					,'good_potato')					),
technologies.INDUSTRY_COTTON_FIELDS					: ('Cotton Fields'					, drawIndustryMap('good_cotton')				, drawIndustryMenu(technologies.INDUSTRY_COTTON_FIELDS					,'good_cotton')					, drawIndustryProducts(technologies.INDUSTRY_COTTON_FIELDS					,'good_cotton')					, drawIndustryMenu2(technologies.INDUSTRY_COTTON_FIELDS					,'good_cotton')					),
technologies.INDUSTRY_RICE_FIELDS					: ('Rice Fields'					, drawIndustryMap('good_rice')					, drawIndustryMenu(technologies.INDUSTRY_RICE_FIELDS					,'good_rice')					, drawIndustryProducts(technologies.INDUSTRY_RICE_FIELDS					,'good_rice')					, drawIndustryMenu2(technologies.INDUSTRY_RICE_FIELDS					,'good_rice')					),
technologies.INDUSTRY_FURHUNTINGGROUNDS				: ('Fur Hunting Grounds'			, drawIndustryMap('good_fur')					, drawIndustryMenu(technologies.INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					, drawIndustryProducts(technologies.INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					, drawIndustryMenu2(technologies.INDUSTRY_FURHUNTINGGROUNDS				,'good_fur')					),
technologies.INDUSTRY_LUMBERMILL					: ('Lumber Mill'					, drawIndustryMap('good_wood')					, drawIndustryMenu(technologies.INDUSTRY_LUMBERMILL						,'good_wood')					, drawIndustryProducts(technologies.INDUSTRY_LUMBERMILL						,'good_wood')					, drawIndustryMenu2(technologies.INDUSTRY_LUMBERMILL					,'good_wood')					),
technologies.INDUSTRY_OILWELL						: ('Oil Well'						, drawIndustryMap('good_oil')					, drawIndustryMenu(technologies.INDUSTRY_OILWELL						,'good_oil')					, drawIndustryProducts(technologies.INDUSTRY_OILWELL						,'good_oil')					, drawIndustryMenu2(technologies.INDUSTRY_OILWELL						,'good_oil')					),
technologies.INDUSTRY_COALMINE						: ('Coal Mine'						, drawIndustryMap('good_coal')					, drawIndustryMenu(technologies.INDUSTRY_COALMINE						,'good_coal')					, drawIndustryProducts(technologies.INDUSTRY_COALMINE						,'good_coal')					, drawIndustryMenu2(technologies.INDUSTRY_COALMINE						,'good_coal')					),
technologies.INDUSTRY_IRONMINE						: ('Iron Mine'						, drawIndustryMap('good_iron')					, drawIndustryMenu(technologies.INDUSTRY_IRONMINE						,'good_iron')					, drawIndustryProducts(technologies.INDUSTRY_IRONMINE						,'good_iron')					, drawIndustryMenu2(technologies.INDUSTRY_IRONMINE						,'good_iron')					),
technologies.INDUSTRY_COPPERMINE					: ('Copper Mine'					, drawIndustryMap('good_copper')				, drawIndustryMenu(technologies.INDUSTRY_COPPERMINE						,'good_copper')					, drawIndustryProducts(technologies.INDUSTRY_COPPERMINE						,'good_copper')					, drawIndustryMenu2(technologies.INDUSTRY_COPPERMINE					,'good_copper')					),
technologies.INDUSTRY_PRECIOUSMETALMINE				: ('Precious Metal Mine'			, drawIndustryMap('good_precious_metal')		, drawIndustryMenu(technologies.INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			, drawIndustryProducts(technologies.INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			, drawIndustryMenu2(technologies.INDUSTRY_PRECIOUSMETALMINE				,'good_precious_metal')			),
technologies.INDUSTRY_RAREMETALMINE					: ('Rare Metal Mine'				, drawIndustryMap('good_rare_metal')			, drawIndustryMenu(technologies.INDUSTRY_RAREMETALMINE					,'good_rare_metal')				, drawIndustryProducts(technologies.INDUSTRY_RAREMETALMINE					,'good_rare_metal')				, drawIndustryMenu2(technologies.INDUSTRY_RAREMETALMINE					,'good_rare_metal')				),
technologies.INDUSTRY_BREADFACTORY					: ('Bread Factory'					, drawIndustryMap('good_bread')					, drawIndustryMenu(technologies.INDUSTRY_BREADFACTORY					,'good_bread')					, drawIndustryProducts(technologies.INDUSTRY_BREADFACTORY					,'good_bread')					, drawIndustryMenu2(technologies.INDUSTRY_BREADFACTORY					,'good_bread')					),
technologies.INDUSTRY_ALCOHOLFACTORY				: ('Alcohol Factory'				, drawIndustryMap('good_alcohol')				, drawIndustryMenu(technologies.INDUSTRY_ALCOHOLFACTORY					,'good_alcohol')				, drawIndustryProducts(technologies.INDUSTRY_ALCOHOLFACTORY					,'good_alcohol')				, drawIndustryMenu2(technologies.INDUSTRY_ALCOHOLFACTORY				,'good_alcohol')				),
technologies.INDUSTRY_SUSHIFACTORY					: ('Sushi Factory'					, drawIndustryMap('good_sushi')					, drawIndustryMenu(technologies.INDUSTRY_SUSHIFACTORY					,'good_sushi')					, drawIndustryProducts(technologies.INDUSTRY_SUSHIFACTORY					,'good_sushi')					, drawIndustryMenu2(technologies.INDUSTRY_SUSHIFACTORY					,'good_sushi')					),
technologies.INDUSTRY_TEXTILEFACTORY				: ('Textile Factory'				, drawIndustryMap('good_textile')				, drawIndustryMenu(technologies.INDUSTRY_TEXTILEFACTORY					,'good_textile')				, drawIndustryProducts(technologies.INDUSTRY_TEXTILEFACTORY					,'good_textile')				, drawIndustryMenu2(technologies.INDUSTRY_TEXTILEFACTORY				,'good_textile')				),
technologies.INDUSTRY_CLOTHESFACTORY				: ('Clothes Factory'				, drawIndustryMap('good_clothes')				, drawIndustryMenu(technologies.INDUSTRY_CLOTHESFACTORY					,'good_clothes')				, drawIndustryProducts(technologies.INDUSTRY_CLOTHESFACTORY					,'good_clothes')				, drawIndustryMenu2(technologies.INDUSTRY_CLOTHESFACTORY				,'good_clothes')				),
technologies.INDUSTRY_FURNITUREFACTORY				: ('Furniture Factory'				, drawIndustryMap('good_furniture')				, drawIndustryMenu(technologies.INDUSTRY_FURNITUREFACTORY				,'good_furniture')				, drawIndustryProducts(technologies.INDUSTRY_FURNITUREFACTORY				,'good_furniture')				, drawIndustryMenu2(technologies.INDUSTRY_FURNITUREFACTORY				,'good_furniture')				),
technologies.INDUSTRY_STEELMILL						: ('Steel Mill'						, drawIndustryMap('good_steel')					, drawIndustryMenu(technologies.INDUSTRY_STEELMILL						,'good_steel')					, drawIndustryProducts(technologies.INDUSTRY_STEELMILL						,'good_steel')					, drawIndustryMenu2(technologies.INDUSTRY_STEELMILL						,'good_steel')					),
technologies.INDUSTRY_TOOLINGFACTORY				: ('Tooling Factory'				, drawIndustryMap('good_tools')					, drawIndustryMenu(technologies.INDUSTRY_TOOLINGFACTORY					,'good_tools')					, drawIndustryProducts(technologies.INDUSTRY_TOOLINGFACTORY					,'good_tools')					, drawIndustryMenu2(technologies.INDUSTRY_TOOLINGFACTORY				,'good_tools')					),
technologies.INDUSTRY_CEMENTFACTORY					: ('Cement Factory'					, drawIndustryMap('good_cement')				, drawIndustryMenu(technologies.INDUSTRY_CEMENTFACTORY					,'good_cement')					, drawIndustryProducts(technologies.INDUSTRY_CEMENTFACTORY					,'good_cement')					, drawIndustryMenu2(technologies.INDUSTRY_CEMENTFACTORY					,'good_cement')					),
technologies.INDUSTRY_REFINARY						: ('Refinary'						, drawIndustryMap('good_fuel')					, drawIndustryMenu(technologies.INDUSTRY_REFINARY						,'good_fuel')					, drawIndustryProducts(technologies.INDUSTRY_REFINARY						,'good_fuel')					, drawIndustryMenu2(technologies.INDUSTRY_REFINARY						,'good_fuel')					),
technologies.INDUSTRY_PLASTICFACTORY				: ('Plastic Factory'				, drawIndustryMap('good_plastic')				, drawIndustryMenu(technologies.INDUSTRY_PLASTICFACTORY					,'good_plastic')				, drawIndustryProducts(technologies.INDUSTRY_PLASTICFACTORY					,'good_plastic')				, drawIndustryMenu2(technologies.INDUSTRY_PLASTICFACTORY				,'good_plastic')				),
technologies.INDUSTRY_GLASSFACTORY					: ('Glass Factory'					, drawIndustryMap('good_glass')					, drawIndustryMenu(technologies.INDUSTRY_GLASSFACTORY					,'good_glass')					, drawIndustryProducts(technologies.INDUSTRY_GLASSFACTORY					,'good_glass')					, drawIndustryMenu2(technologies.INDUSTRY_GLASSFACTORY					,'good_glass')					),
technologies.INDUSTRY_ELECTRONICCOMPONENTSFACTORY	: ('Electronic Components Factory'	, drawIndustryMap('good_electronics_component')	, drawIndustryMenu(technologies.INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	, drawIndustryProducts(technologies.INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	, drawIndustryMenu2(technologies.INDUSTRY_ELECTRONICCOMPONENTSFACTORY	,'good_electronics_component')	),
technologies.INDUSTRY_RADIOFACTORY					: ('Radio Factory'					, drawIndustryMap('good_radio')					, drawIndustryMenu(technologies.INDUSTRY_RADIOFACTORY					,'good_radio')					, drawIndustryProducts(technologies.INDUSTRY_RADIOFACTORY					,'good_radio')					, drawIndustryMenu2(technologies.INDUSTRY_RADIOFACTORY					,'good_radio')					),
technologies.INDUSTRY_COMPUTERFACTORY				: ('Computer Factory'				, drawIndustryMap('good_computer')				, drawIndustryMenu(technologies.INDUSTRY_COMPUTERFACTORY				,'good_computer')				, drawIndustryProducts(technologies.INDUSTRY_COMPUTERFACTORY				,'good_computer')				, drawIndustryMenu2(technologies.INDUSTRY_COMPUTERFACTORY				,'good_computer')				),
technologies.INDUSTRY_GUNFACTORY					: ('Gun Factory'					, drawIndustryMap('good_guns')					, drawIndustryMenu(technologies.INDUSTRY_GUNFACTORY						,'good_guns')					, drawIndustryProducts(technologies.INDUSTRY_GUNFACTORY						,'good_guns')					, drawIndustryMenu2(technologies.INDUSTRY_GUNFACTORY					,'good_guns')					),
technologies.INDUSTRY_ENGINEFACTORY					: ('Engine Factory'					, drawIndustryMap('good_engine')				, drawIndustryMenu(technologies.INDUSTRY_ENGINEFACTORY					,'good_engine')					, drawIndustryProducts(technologies.INDUSTRY_ENGINEFACTORY					,'good_engine')					, drawIndustryMenu2(technologies.INDUSTRY_ENGINEFACTORY					,'good_engine')					),
technologies.INDUSTRY_CARFACTORY					: ('Car Factory'					, drawIndustryMap('good_car')					, drawIndustryMenu(technologies.INDUSTRY_CARFACTORY						,'good_car')					, drawIndustryProducts(technologies.INDUSTRY_CARFACTORY						,'good_car')					, drawIndustryMenu2(technologies.INDUSTRY_CARFACTORY					,'good_car')					),
technologies.INDUSTRY_PLANESFACTORY					: ('Planes Factory'					, drawIndustryMap('good_planes')				, drawIndustryMenu(technologies.INDUSTRY_PLANESFACTORY					,'good_planes')					, drawIndustryProducts(technologies.INDUSTRY_PLANESFACTORY					,'good_planes')					, drawIndustryMenu2(technologies.INDUSTRY_PLANESFACTORY					,'good_planes')					),
technologies.INDUSTRY_JEWELRYWORKSHOP				: ('Jewelry Workshop'				, drawIndustryMap('good_jewelry')				, drawIndustryMenu(technologies.INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				, drawIndustryProducts(technologies.INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				, drawIndustryMenu2(technologies.INDUSTRY_JEWELRYWORKSHOP				,'good_jewelry')				),
technologies.INDUSTRY_PHONEFACTORY					: ('Phone Factory'					, drawIndustryMap('good_phone')					, drawIndustryMenu(technologies.INDUSTRY_PHONEFACTORY					,'good_phone')					, drawIndustryProducts(technologies.INDUSTRY_PHONEFACTORY					,'good_phone')					, drawIndustryMenu2(technologies.INDUSTRY_PHONEFACTORY					,'good_phone')					),
technologies.INDUSTRY_STONEQUERY					: ('Stone Query'					, drawIndustryMap('good_stone')					, drawIndustryMenu(technologies.INDUSTRY_STONEQUERY						,'good_stone')					, drawIndustryProducts(technologies.INDUSTRY_STONEQUERY						,'good_stone')					, drawIndustryMenu2(technologies.INDUSTRY_STONEQUERY					,'good_stone')					),
technologies.INDUSTRY_SANDQUERY						: ('Sand Query'						, drawIndustryMap('good_sand')					, drawIndustryMenu(technologies.INDUSTRY_SANDQUERY						,'good_sand')					, drawIndustryProducts(technologies.INDUSTRY_SANDQUERY						,'good_sand')					, drawIndustryMenu2(technologies.INDUSTRY_SANDQUERY						,'good_sand')					),                 
}

def print_industry(industry):
	return industryPrintMap[industry][0]

def draw_industry_map(industry):
	return draw_industry_by_id(Plant.type(industry))[1]

def draw_industry_menu(industry_id):
	return draw_industry_by_id(industry_id)[2]

def draw_industry_menu2(industry_id):
	return draw_industry_by_id(industry_id)[4]

def draw_industry_product(industry_id):
	return draw_industry_by_id(industry_id)[3]

def draw_industry_by_id(industry_id):
	return industryPrintMap.get(
		industry_id,
		('', lambda rect: None)
	)