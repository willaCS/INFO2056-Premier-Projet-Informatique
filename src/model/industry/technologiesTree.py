from model.industry.technologies import IndustryType, CanPlaceOn, industry
from model.market import player_wallet
from model.terrain import Ressource, TerrainTile
from model.terrain.terrain import get_terrain_tile

default_unlocked = [
	IndustryType.WHEAT_FIELDS,
	IndustryType.FISHINGBOAT,
	IndustryType.LUMBERMILL,
	IndustryType.STONEQUERY,
]

techTree = [
	{
		"name": "Food",
		"techs": [
			{
				"name": "Food 1",
				"cost": 100,
				"unlocked": False,
				"unlocks": [
					IndustryType.POTATO_FIELDS,
					IndustryType.BREADFACTORY,
				]
			},
			{
				"name": "Food 2",
				"cost": 250,
				"unlocked": False,
				"unlocks": [
					IndustryType.SALTEXTRACTION,
					IndustryType.RICE_FIELDS,
				]
			},
			{
				"name": "Food 3",
				"cost": 750,
				"unlocked": False,
				"unlocks": [
					IndustryType.SUSHIFACTORY,
					IndustryType.ALCOHOLFACTORY,
				]
			},
		]
	},
	{
		"name": "Process",
		"techs": [
			{
				"name": "Process 1",
				"cost": 100,
				"unlocked": False,
				"unlocks": [
					IndustryType.COTTON_FIELDS,
					IndustryType.SANDQUERY,
				]
			},
			{
				"name": "Process 2",
				"cost": 250,
				"unlocked": False,
				"unlocks": [
					IndustryType.TEXTILEFACTORY,
					IndustryType.FURNITUREFACTORY,
					IndustryType.CEMENTFACTORY,
				]
			},
			{
				"name": "Process 3",
				"cost": 500,
				"unlocked": False,
				"unlocks": [
					IndustryType.CLOTHESFACTORY,
					IndustryType.GLASSFACTORY,
				]
			},
		]
	},
	{
		"name": "Metalurgy",
		"techs": [
			{
				"name": "Metalurgy 1",
				"cost": 150,
				"unlocked": False,
				"unlocks": [
					IndustryType.COALMINE,
				]
			},
			{
				"name": "Metalurgy 2",
				"cost": 500,
				"unlocked": False,
				"unlocks": [
					IndustryType.IRONMINE,
					IndustryType.COPPERMINE,
				]
			},
			{
				"name": "Metalurgy 3",
				"cost": 5000,
				"unlocked": False,
				"unlocks": [
					IndustryType.PRECIOUSMETALMINE,
					IndustryType.RAREMETALMINE,
					IndustryType.JEWELRYWORKSHOP,
				]
			},
		]
	},
	{
		"name": "Advanced",
		"techs": [
			{
				"name": "Advanced 1",
				"cost": 750,
				"unlocked": False,
				"unlocks": [
					IndustryType.STEELMILL,
				]
			},
			{
				"name": "Advanced 2",
				"cost": 1000,
				"unlocked": False,
				"unlocks": [
					IndustryType.OILWELL,
				]
			},
			{
				"name": "Advanced 3",
				"cost": 3000,
				"unlocked": False,
				"unlocks": [
					IndustryType.REFINARY,
					IndustryType.RADIOFACTORY,
				]
			},
			{
				"name": "Advanced 4",
				"cost": 10000,
				"unlocked": False,
				"unlocks": [
					IndustryType.PLASTICFACTORY,
					IndustryType.GUNFACTORY,
				]
			},
			{
				"name": "Advanced 5",
				"cost": 50000,
				"unlocked": False,
				"unlocks": [
					IndustryType.ELECTRONICCOMPONENTSFACTORY,
					IndustryType.ENGINEFACTORY,
					IndustryType.CARFACTORY,
				]
			},
			{
				"name": "Advanced 6",
				"cost": 100000,
				"unlocked": False,
				"unlocks": [
					IndustryType.COMPUTERFACTORY,
					IndustryType.PLANESFACTORY,
					IndustryType.PHONEFACTORY,
				]
			},
		]
	},
]

# action by player to unlock a technology
def add_tech(i, j):
	# TODO add check if player has enough science points
	j = j if i < len(techTree) else j + 3
	i = i if i < len(techTree) else len(techTree) - 1
	tech = techTree[i]['techs'][j]
	if tech['unlocked']:
		return
	if player_wallet.science < tech['cost']:
		return
	if j != 0 and not techTree[i]['techs'][j - 1]['unlocked']:
		return
	player_wallet.science -= tech['cost']
	tech['unlocked'] = True

def get_unlocked_techs():
	return [
		tech
			for tree in techTree
			for tech in tree['techs'] if tech['unlocked']
	]

def get_unlocked_buildings():
	return [
		*default_unlocked,
		*(unlock
			for tree in techTree
			for tech in tree['techs'] if tech['unlocked']
			for unlock in tech['unlocks']
		)
	]

def get_tech_for_draw(i, j):
	j = j if i < len(techTree) else j + 3
	i = i if i < len(techTree) else len(techTree) - 1
	return techTree[i]['techs'][j]


def get_placable_on(coord):
	if not coord:
		return []
	unlocked = get_unlocked_buildings()
	terrain = get_terrain_tile(coord)
	ressource = terrain.ressource
	
	res = []
	for indus in industry:
		if not indus in unlocked:
			continue
		test_ind = industry[indus]
		for place_on in test_ind['place_on']:
			match place_on['type']:
				case CanPlaceOn.RESSOURCE:
					if ressource and place_on['id'] == ressource.type:
						res.append(indus)
				case CanPlaceOn.TERRAIN:
					if place_on['id'] == terrain.type:
						res.append(indus)
	return res