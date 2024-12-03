from model.industry import Plant, technologies
from ui import Screenmode, Zoom
from ui.framework.draw import drawRect
from ui.framework.image import drawImage

def drawIndustry(key):
	
	def res(rect):
		pad = Zoom.tile_size // 16
		match Screenmode.val:
			case Screenmode.SCREENMODE_MAIN:
				drawImage('industry', rect)
				if rect[1][1] - pad * 2 < 1:
					return
				drawImage(key,
					((rect[0][0] + pad, rect[0][1] + pad),
					(rect[1][0] - pad * 2, rect[1][1] - pad * 2)
				))
			case Screenmode.SCREENMODE_ECONOMY_SUPPLY:
				drawRect(rect, (255, 255, 0))
			case _:
				drawRect(rect, (0, 0, 0))
	return res

industryPrintMap = {
	technologies.INDUSTRY_FISHINGBOAT					: ('Fishing Boat'					, drawIndustry('good_fish')),
	technologies.INDUSTRY_SALTEXTRACTION				: ('Salt Extraction'				, drawIndustry('good_salt')),
	technologies.INDUSTRY_WHEAT_FIELDS					: ('Wheat Fields'					, drawIndustry('good_wheat')),
	technologies.INDUSTRY_POTATO_FIELDS					: ('Potato Fields'					, drawIndustry('good_potato')),
	technologies.INDUSTRY_COTTON_FIELDS					: ('Cotton Fields'					, drawIndustry('good_cotton')),
	technologies.INDUSTRY_RICE_FIELDS					: ('Rice Fields'					, drawIndustry('good_rice')),
	technologies.INDUSTRY_FURHUNTINGGROUNDS				: ('Fur Hunting Grounds'			, drawIndustry('good_fur')),
	technologies.INDUSTRY_LUMBERMILL					: ('Lumber Mill'					, drawIndustry('good_wood')),
	technologies.INDUSTRY_OILWELL						: ('Oil Well'						, drawIndustry('good_oil')),
	technologies.INDUSTRY_COALMINE						: ('Coal Mine'						, drawIndustry('good_coal')),
	technologies.INDUSTRY_IRONMINE						: ('Iron Mine'						, drawIndustry('good_iron')),
	technologies.INDUSTRY_COPPERMINE					: ('Copper Mine'					, drawIndustry('good_copper')),
	technologies.INDUSTRY_PRECIOUSMETALMINE				: ('Precious Metal Mine'			, drawIndustry('good_precious_metal')),
	technologies.INDUSTRY_RAREMETALMINE					: ('Rare Metal Mine'				, drawIndustry('good_rare_metal')),
	technologies.INDUSTRY_BREADFACTORY					: ('Bread Factory'					, drawIndustry('good_bread')),
	technologies.INDUSTRY_ALCOHOLFACTORY				: ('Alcohol Factory'				, drawIndustry('good_alcohol')),
	technologies.INDUSTRY_SUSHIFACTORY					: ('Sushi Factory'					, drawIndustry('good_sushi')),
	technologies.INDUSTRY_TEXTILEFACTORY				: ('Textile Factory'				, drawIndustry('good_textile')),
	technologies.INDUSTRY_CLOTHESFACTORY				: ('Clothes Factory'				, drawIndustry('good_clothes')),
	technologies.INDUSTRY_FURNITUREFACTORY				: ('Furniture Factory'				, drawIndustry('good_furniture')),
	technologies.INDUSTRY_STEELMILL						: ('Steel Mill'						, drawIndustry('good_steel')),
	technologies.INDUSTRY_TOOLINGFACTORY				: ('Tooling Factory'				, drawIndustry('good_tools')),
	technologies.INDUSTRY_CEMENTFACTORY					: ('Cement Factory'					, drawIndustry('good_cement')),
	technologies.INDUSTRY_REFINARY						: ('Refinary'						, drawIndustry('good_fuel')),
	technologies.INDUSTRY_PLASTICFACTORY				: ('Plastic Factory'				, drawIndustry('good_plastic')),
	technologies.INDUSTRY_GLASSFACTORY					: ('Glass Factory'					, drawIndustry('good_glass')),
	technologies.INDUSTRY_ELECTRONICCOMPONENTSFACTORY	: ('Electronic Components Factory'	, drawIndustry('good_electronics_component')),
	technologies.INDUSTRY_RADIOFACTORY					: ('Radio Factory'					, drawIndustry('good_radio')),
	technologies.INDUSTRY_COMPUTERFACTORY				: ('Computer Factory'				, drawIndustry('good_computer')),
	technologies.INDUSTRY_GUNFACTORY					: ('Gun Factory'					, drawIndustry('good_guns')),
	technologies.INDUSTRY_ENGINEFACTORY					: ('Engine Factory'					, drawIndustry('good_engine')),
	technologies.INDUSTRY_CARFACTORY					: ('Car Factory'					, drawIndustry('good_car')),
	technologies.INDUSTRY_PLANESFACTORY					: ('Planes Factory'					, drawIndustry('good_planes')),
	technologies.INDUSTRY_JEWELRYWORKSHOP				: ('Jewelry Workshop'				, drawIndustry('good_jewelry')),
	technologies.INDUSTRY_PHONEFACTORY					: ('Phone Factory'					, drawIndustry('good_phone')),
	technologies.INDUSTRY_STONEQUERY					: ('Stone Query'					, drawIndustry('good_stone')),
	technologies.INDUSTRY_SANDQUERY						: ('Sand Query'						, drawIndustry('good_sand')),                 
}

def print_industry(industry):
	return industryPrintMap[industry][0]

def draw_industry(industry):
	return draw_industry_by_id(Plant.type(industry))

def draw_industry_by_id(industry_id):
	return industryPrintMap.get(
		industry_id,
		('', lambda rect: None)
	)[1]