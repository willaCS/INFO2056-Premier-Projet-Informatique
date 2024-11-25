from model.industry import Plant, technologies
from ui.framework import drawRect

industryPrintMap = {
	technologies.INDUSTRY_FISHINGBOAT					: ('Fishing Boat'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_SALTEXTRACTION				: ('Salt Extraction'				, lambda rect: drawRect(rect, (230, 230, 230))),
	technologies.INDUSTRY_WHEAT_FIELDS					: ('Wheat Fields'					, lambda rect: drawRect(rect, (255, 222,  19))),
	technologies.INDUSTRY_POTATO_FIELDS					: ('Potato Fields'					, lambda rect: drawRect(rect, (227, 164,  68))),
	technologies.INDUSTRY_COTTON_FIELDS					: ('Cotton Fields'					, lambda rect: drawRect(rect, (149, 255, 140))),
	technologies.INDUSTRY_RICE_FIELDS					: ('Rice Fields'					, lambda rect: drawRect(rect, (144, 228, 245))),
	technologies.INDUSTRY_FURHUNTINGGROUNDS				: ('Fur Hunting Grounds'			, lambda rect: drawRect(rect, (156, 105,  28))),
	technologies.INDUSTRY_LUMBERMILL					: ('Lumber Mill'					, lambda rect: drawRect(rect, (102,  64,   7))),
	technologies.INDUSTRY_OILWELL						: ('Oil Well'						, lambda rect: drawRect(rect, ( 80,  80,  80))),
	technologies.INDUSTRY_COALMINE						: ('Coal Mine'						, lambda rect: drawRect(rect, ( 20,  20,  20))),
	technologies.INDUSTRY_IRONMINE						: ('Iron Mine'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_COPPERMINE					: ('Copper Mine'					, lambda rect: drawRect(rect, (255,  89,   0))),
	technologies.INDUSTRY_PRECIOUSMETALMINE				: ('Precious Metal Mine'			, lambda rect: drawRect(rect, (  0, 150, 161))),
	technologies.INDUSTRY_RAREMETALMINE					: ('Rare Metal Mine'				, lambda rect: drawRect(rect, (101, 135, 101))),
	technologies.INDUSTRY_BREADFACTORY					: ('Bread Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_ALCOHOLFACTORY				: ('Alcohol Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_SUSHIFACTORY					: ('Sushi Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_TEXTILEFACTORY				: ('Textile Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_CLOTHESFACTORY				: ('Clothes Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_FURNITUREFACTORY				: ('Furniture Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_STEELMILL						: ('Steel Mill'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_TOOLINGFACTORY				: ('Tooling Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_CEMENTFACTORY					: ('Cement Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_REFINARY						: ('Refinary'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_PLASTICFACTORY				: ('Plastic Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_GLASSFACTORY					: ('Glass Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_ELECTRONICCOMPONENTSFACTORY	: ('Electronic Components Factory'	, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_RADIOFACTORY					: ('Radio Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_COMPUTERFACTORY				: ('Computer Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_GUNFACTORY					: ('Gun Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_ENGINEFACTORY					: ('Engine Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_CARFACTORY					: ('Car Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_PLANESFACTORY					: ('Planes Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_JEWELRYWORKSHOP				: ('Jewelry Workshop'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_PHONEFACTORY					: ('Phone Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_STONEQUERY					: ('Stone Query'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	technologies.INDUSTRY_SANDQUERY						: ('Sand Query'						, lambda rect: drawRect(rect, (  0,   0,   0))),
}

def print_industry(industry):
	return industryPrintMap[industry][0]

def draw_industry(industry):
	func = industryPrintMap.get(
		Plant.type(industry),
		('', lambda rect: None)
	)[1]
	return lambda rect: func(rect)
