from typing import List, Dict
from model.industry import Plant, technologies

type_building = Dict[str, int | str]

buildings: List[type_building] = [
	{ 'id': technologies.INDUSTRY_FISHINGBOAT, 					'name': 'FISHINGBOAT',					 },
	{ 'id': technologies.INDUSTRY_SALTEXTRACTION, 				'name': 'SALTEXTRACTION',				 },
	{ 'id': technologies.INDUSTRY_WHEAT_FIELDS, 				'name': 'WHEAT_FIELDS',					 },
	{ 'id': technologies.INDUSTRY_POTATO_FIELDS, 				'name': 'POTATO_FIELDS',				 },
	{ 'id': technologies.INDUSTRY_COTTON_FIELDS, 				'name': 'COTTON_FIELDS',				 },
	{ 'id': technologies.INDUSTRY_RICE_FIELDS, 					'name': 'RICE_FIELDS',					 },
	{ 'id': technologies.INDUSTRY_FURHUNTINGGROUNDS, 			'name': 'FURHUNTINGGROUNDS',			 },
	{ 'id': technologies.INDUSTRY_LUMBERMILL, 					'name': 'LUMBERMILL',					 },
	{ 'id': technologies.INDUSTRY_OILWELL, 						'name': 'OILWELL',						 },
	{ 'id': technologies.INDUSTRY_COALMINE, 					'name': 'COALMINE',						 },
	{ 'id': technologies.INDUSTRY_IRONMINE, 					'name': 'IRONMINE',						 },
	{ 'id': technologies.INDUSTRY_COPPERMINE, 					'name': 'COPPERMINE',					 },
	{ 'id': technologies.INDUSTRY_PRECIOUSMETALMINE, 			'name': 'PRECIOUSMETALMINE',			 },
	{ 'id': technologies.INDUSTRY_RAREMETALMINE, 				'name': 'RAREMETALMINE',				 },
	{ 'id': technologies.INDUSTRY_BREADFACTORY, 				'name': 'BREADFACTORY',					 },
	{ 'id': technologies.INDUSTRY_ALCOHOLFACTORY, 				'name': 'ALCOHOLFACTORY',				 },
	{ 'id': technologies.INDUSTRY_SUSHIFACTORY, 				'name': 'SUSHIFACTORY',					 },
	{ 'id': technologies.INDUSTRY_TEXTILEFACTORY, 				'name': 'TEXTILEFACTORY',				 },
	{ 'id': technologies.INDUSTRY_CLOTHESFACTORY, 				'name': 'CLOTHESFACTORY',				 },
	{ 'id': technologies.INDUSTRY_FURNITUREFACTORY, 			'name': 'FURNITUREFACTORY',				 },
	{ 'id': technologies.INDUSTRY_STEELMILL, 					'name': 'STEELMILL',					 },
	{ 'id': technologies.INDUSTRY_TOOLINGFACTORY, 				'name': 'TOOLINGFACTORY',				 },
	{ 'id': technologies.INDUSTRY_CEMENTFACTORY, 				'name': 'CEMENTFACTORY',				 },
	{ 'id': technologies.INDUSTRY_REFINARY, 					'name': 'REFINARY',						 },
	{ 'id': technologies.INDUSTRY_PLASTICFACTORY, 				'name': 'PLASTICFACTORY',				 },
	{ 'id': technologies.INDUSTRY_GLASSFACTORY, 				'name': 'GLASSFACTORY',					 },
	{ 'id': technologies.INDUSTRY_ELECTRONICCOMPONENTSFACTORY,	'name': 'ELECTRONICCOMPONENTSFACTORY',	 },
	{ 'id': technologies.INDUSTRY_RADIOFACTORY, 				'name': 'RADIOFACTORY',					 },
	{ 'id': technologies.INDUSTRY_COMPUTERFACTORY, 				'name': 'COMPUTERFACTORY',				 },
	{ 'id': technologies.INDUSTRY_GUNFACTORY, 					'name': 'GUNFACTORY',					 },
	{ 'id': technologies.INDUSTRY_ENGINEFACTORY, 				'name': 'ENGINEFACTORY',				 },
	{ 'id': technologies.INDUSTRY_CARFACTORY, 					'name': 'CARFACTORY',					 },
	{ 'id': technologies.INDUSTRY_PLANESFACTORY, 				'name': 'PLANESFACTORY',				 },
	{ 'id': technologies.INDUSTRY_JEWELRYWORKSHOP, 				'name': 'JEWELRYWORKSHOP',				 },
	{ 'id': technologies.INDUSTRY_PHONEFACTORY, 				'name': 'PHONEFACTORY',					 },
	{ 'id': technologies.INDUSTRY_STONEQUERY, 					'name': 'STONEQUERY',					 },
	{ 'id': technologies.INDUSTRY_SANDQUERY, 					'name': 'SANDQUERY',					 },
]

index = 0

def next():
	global index
	index = index + 1 if index < len(buildings) - 1 else 0

def prev():
	global index
	index = index - 1 if index > 0 else len(buildings) - 1

def activeBuilding():
	return buildings[index]