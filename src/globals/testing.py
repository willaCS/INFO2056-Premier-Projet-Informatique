from typing import List, Dict
from map import Industry, Tile

type_building = Dict[str, int | str]

buildings: List[type_building] = [
	{ 'id': Industry.INDUSTRY_FISHINGBOAT, 					'name': 'FISHINGBOAT',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_SALTEXTRACTION, 				'name': 'SALTEXTRACTION',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_WHEAT_FIELDS, 				'name': 'WHEAT_FIELDS',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_POTATO_FIELDS, 				'name': 'POTATO_FIELDS',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_COTTON_FIELDS, 				'name': 'COTTON_FIELDS',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_RICE_FIELDS, 					'name': 'RICE_FIELDS',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_FURHUNTINGGROUNDS, 			'name': 'FURHUNTINGGROUNDS',			'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_LUMBERMILL, 					'name': 'LUMBERMILL',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_OILWELL, 						'name': 'OILWELL',						'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_COALMINE, 					'name': 'COALMINE',						'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_IRONMINE, 					'name': 'IRONMINE',						'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_COPPERMINE, 					'name': 'COPPERMINE',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_PRECIOUSMETALMINE, 			'name': 'PRECIOUSMETALMINE',			'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_RAREMETALMINE, 				'name': 'RAREMETALMINE',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_BREADFACTORY, 				'name': 'BREADFACTORY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_ALCOHOLFACTORY, 				'name': 'ALCOHOLFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_SUSHIFACTORY, 				'name': 'SUSHIFACTORY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_TEXTILEFACTORY, 				'name': 'TEXTILEFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_CLOTHESFACTORY, 				'name': 'CLOTHESFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_FURNITUREFACTORY, 			'name': 'FURNITUREFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_STEELMILL, 					'name': 'STEELMILL',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_TOOLINGFACTORY, 				'name': 'TOOLINGFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_CEMENTFACTORY, 				'name': 'CEMENTFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_REFINARY, 					'name': 'REFINARY',						'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_PLASTICFACTORY, 				'name': 'PLASTICFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_GLASSFACTORY, 				'name': 'GLASSFACTORY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_ELECTRONICCOMPONENTSFACTORY,	'name': 'ELECTRONICCOMPONENTSFACTORY',	'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_RADIOFACTORY, 				'name': 'RADIOFACTORY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_COMPUTERFACTORY, 				'name': 'COMPUTERFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_GUNFACTORY, 					'name': 'GUNFACTORY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_ENGINEFACTORY, 				'name': 'ENGINEFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_CARFACTORY, 					'name': 'CARFACTORY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_PLANESFACTORY, 				'name': 'PLANESFACTORY',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_JEWELRYWORKSHOP, 				'name': 'JEWELRYWORKSHOP',				'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_PHONEFACTORY, 				'name': 'PHONEFACTORY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_STONEQUERY, 					'name': 'STONEQUERY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.INDUSTRY_SANDQUERY, 					'name': 'SANDQUERY',					'type': Tile.TILETYPE_INDUSTRY, },
	{ 'id': Industry.TRANSPORT_ROAD,	 					'name': 'ROAD',							'type': Tile.TILETYPE_TRANSPORT, },
	{ 'id': Industry.TRANSPORT_RAILWAY,						'name': 'RAILWAY',						'type': Tile.TILETYPE_TRANSPORT, },
	{ 'id': Industry.TRANSPORT_HUB_TRUCK,					'name': 'TRANSPORT_HUB_TRUCK',			'type': Tile.TILETYPE_TRANSPORTHUB, },
	{ 'id': Industry.TRANSPORT_HUB_RAILWAY_STATION,			'name': 'RAILWAY_STATION',				'type': Tile.TILETYPE_TRANSPORTHUB, },
	{ 'id': Industry.TRANSPORT_HUB_HARBOR,					'name': 'HARBOR',						'type': Tile.TILETYPE_TRANSPORTHUB, },
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