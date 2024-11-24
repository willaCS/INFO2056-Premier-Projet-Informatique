from map import Industry
from ui.framework import drawRect

industryPrintMap = {
	Industry.INDUSTRY_FISHINGBOAT					: ('Fishing Boat'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_SALTEXTRACTION				: ('Salt Extraction'				, lambda rect: drawRect(rect, (230, 230, 230))),
	Industry.INDUSTRY_WHEAT_FIELDS					: ('Wheat Fields'					, lambda rect: drawRect(rect, (255, 222,  19))),
	Industry.INDUSTRY_POTATO_FIELDS					: ('Potato Fields'					, lambda rect: drawRect(rect, (227, 164,  68))),
	Industry.INDUSTRY_COTTON_FIELDS					: ('Cotton Fields'					, lambda rect: drawRect(rect, (149, 255, 140))),
	Industry.INDUSTRY_RICE_FIELDS					: ('Rice Fields'					, lambda rect: drawRect(rect, (144, 228, 245))),
	Industry.INDUSTRY_FURHUNTINGGROUNDS				: ('Fur Hunting Grounds'			, lambda rect: drawRect(rect, (156, 105,  28))),
	Industry.INDUSTRY_LUMBERMILL					: ('Lumber Mill'					, lambda rect: drawRect(rect, (102,  64,   7))),
	Industry.INDUSTRY_OILWELL						: ('Oil Well'						, lambda rect: drawRect(rect, ( 80,  80,  80))),
	Industry.INDUSTRY_COALMINE						: ('Coal Mine'						, lambda rect: drawRect(rect, ( 20,  20,  20))),
	Industry.INDUSTRY_IRONMINE						: ('Iron Mine'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_COPPERMINE					: ('Copper Mine'					, lambda rect: drawRect(rect, (255,  89,   0))),
	Industry.INDUSTRY_PRECIOUSMETALMINE				: ('Precious Metal Mine'			, lambda rect: drawRect(rect, (  0, 150, 161))),
	Industry.INDUSTRY_RAREMETALMINE					: ('Rare Metal Mine'				, lambda rect: drawRect(rect, (101, 135, 101))),
	Industry.INDUSTRY_BREADFACTORY					: ('Bread Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_ALCOHOLFACTORY				: ('Alcohol Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_SUSHIFACTORY					: ('Sushi Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_TEXTILEFACTORY				: ('Textile Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_CLOTHESFACTORY				: ('Clothes Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_FURNITUREFACTORY				: ('Furniture Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_STEELMILL						: ('Steel Mill'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_TOOLINGFACTORY				: ('Tooling Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_CEMENTFACTORY					: ('Cement Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_REFINARY						: ('Refinary'						, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_PLASTICFACTORY				: ('Plastic Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_GLASSFACTORY					: ('Glass Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_ELECTRONICCOMPONENTSFACTORY	: ('Electronic Components Factory'	, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_RADIOFACTORY					: ('Radio Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_COMPUTERFACTORY				: ('Computer Factory'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_GUNFACTORY					: ('Gun Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_ENGINEFACTORY					: ('Engine Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_CARFACTORY					: ('Car Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_PLANESFACTORY					: ('Planes Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_JEWELRYWORKSHOP				: ('Jewelry Workshop'				, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_PHONEFACTORY					: ('Phone Factory'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_STONEQUERY					: ('Stone Query'					, lambda rect: drawRect(rect, (  0,   0,   0))),
	Industry.INDUSTRY_SANDQUERY						: ('Sand Query'						, lambda rect: drawRect(rect, (  0,   0,   0))),
}

def print_industry(industry):
	return industryPrintMap[industry][0]

def draw_industry(industry):
	func = industryPrintMap.get(
		industry,
		('', lambda rect: None)
	)[1]
	return lambda rect: func(rect)
