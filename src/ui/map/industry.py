from model.industry import technologies
from model.industry.Plant import Plant
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

def drawIndustryProducts(id):
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
	technologies.IndustryType.FISHINGBOAT					: ('Fishing Boat'					, 'good_fish'					),
	technologies.IndustryType.SALTEXTRACTION				: ('Salt Extraction'				, 'good_salt'					),
	technologies.IndustryType.WHEAT_FIELDS					: ('Wheat Fields'					, 'good_wheat'					),
	technologies.IndustryType.POTATO_FIELDS					: ('Potato Fields'					, 'good_potato'					),
	technologies.IndustryType.COTTON_FIELDS					: ('Cotton Fields'					, 'good_cotton'					),
	technologies.IndustryType.RICE_FIELDS					: ('Rice Fields'					, 'good_rice'					),
	technologies.IndustryType.FURHUNTINGGROUNDS				: ('Fur Hunting Grounds'			, 'good_fur'					),
	technologies.IndustryType.LUMBERMILL					: ('Lumber Mill'					, 'good_wood'					),
	technologies.IndustryType.OILWELL						: ('Oil Well'						, 'good_oil'					),
	technologies.IndustryType.COALMINE						: ('Coal Mine'						, 'good_coal'					),
	technologies.IndustryType.IRONMINE						: ('Iron Mine'						, 'good_iron'					),
	technologies.IndustryType.COPPERMINE					: ('Copper Mine'					, 'good_copper'					),
	technologies.IndustryType.PRECIOUSMETALMINE				: ('Precious Metal Mine'			, 'good_precious_metal'			),
	technologies.IndustryType.RAREMETALMINE					: ('Rare Metal Mine'				, 'good_rare_metal'				),
	technologies.IndustryType.BREADFACTORY					: ('Bread Factory'					, 'good_bread'					),
	technologies.IndustryType.ALCOHOLFACTORY				: ('Alcohol Factory'				, 'good_alcohol'				),
	technologies.IndustryType.SUSHIFACTORY					: ('Sushi Factory'					, 'good_sushi'					),
	technologies.IndustryType.TEXTILEFACTORY				: ('Textile Factory'				, 'good_textile'				),
	technologies.IndustryType.CLOTHESFACTORY				: ('Clothes Factory'				, 'good_clothes'				),
	technologies.IndustryType.FURNITUREFACTORY				: ('Furniture Factory'				, 'good_furniture'				),
	technologies.IndustryType.STEELMILL						: ('Steel Mill'						, 'good_steel'					),
	technologies.IndustryType.TOOLINGFACTORY				: ('Tooling Factory'				, 'good_tools'					),
	technologies.IndustryType.CEMENTFACTORY					: ('Cement Factory'					, 'good_cement'					),
	technologies.IndustryType.REFINARY						: ('Refinary'						, 'good_fuel'					),
	technologies.IndustryType.PLASTICFACTORY				: ('Plastic Factory'				, 'good_plastic'				),
	technologies.IndustryType.GLASSFACTORY					: ('Glass Factory'					, 'good_glass'					),
	technologies.IndustryType.ELECTRONICCOMPONENTSFACTORY	: ('Electronic Components Factory'	, 'good_electronics_component'	),
	technologies.IndustryType.RADIOFACTORY					: ('Radio Factory'					, 'good_radio'					),
	technologies.IndustryType.COMPUTERFACTORY				: ('Computer Factory'				, 'good_computer'				),
	technologies.IndustryType.GUNFACTORY					: ('Gun Factory'					, 'good_guns'					),
	technologies.IndustryType.ENGINEFACTORY					: ('Engine Factory'					, 'good_engine'					),
	technologies.IndustryType.CARFACTORY					: ('Car Factory'					, 'good_car'					),
	technologies.IndustryType.PLANESFACTORY					: ('Planes Factory'					, 'good_planes'					),
	technologies.IndustryType.JEWELRYWORKSHOP				: ('Jewelry Workshop'				, 'good_jewelry'				),
	technologies.IndustryType.PHONEFACTORY					: ('Phone Factory'					, 'good_phone'					),
	technologies.IndustryType.STONEQUERY					: ('Stone Query'					, 'good_stone'					),
	technologies.IndustryType.SANDQUERY						: ('Sand Query'						, 'good_sand'					),
}

def print_industry(industry):
	return industryPrintMap[industry][0]

def draw_industry_map(industry: Plant):
	image_key = industryPrintMap[industry.type][1]
	return drawIndustryMap(image_key)

def draw_industry_menu(industry_id):
	image_key = industryPrintMap[industry_id][1]
	return drawIndustryMenu(industry_id, image_key)

def draw_industry_menu2(industry_id):
	image_key = industryPrintMap[industry_id][1]
	return drawIndustryMenu2(industry_id, image_key)

def draw_industry_product(industry_id):
	return drawIndustryProducts(industry_id)