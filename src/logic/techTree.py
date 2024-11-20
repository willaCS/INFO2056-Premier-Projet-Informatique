from map import Industry
from globals import player

unlocked = [
	Industry.INDUSTRY_WHEAT_FIELDS,
	Industry.INDUSTRY_FISHINGBOAT,
	Industry.INDUSTRY_LUMBERMILL,
	Industry.INDUSTRY_STONEQUERY,
]

techTree = [
	{
		"name": "Food",
		"techs": [
			{
				"name": "Food 1",
				"cost": 10,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_POTATO_FIELDS,
					Industry.INDUSTRY_BREADFACTORY,
				]
			},
			{
				"name": "Food 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_SALTEXTRACTION,
					Industry.INDUSTRY_RICE_FIELDS,
				]
			},
			{
				"name": "Food 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_SUSHIFACTORY,
					Industry.INDUSTRY_ALCOHOLFACTORY,
				]
			},
		]
	},
	{
		"name": "Process",
		"techs": [
			{
				"name": "Process 1",
				"cost": 10,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_COTTON_FIELDS,
					Industry.INDUSTRY_SANDQUERY,
				]
			},
			{
				"name": "Process 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_TEXTILEFACTORY,
					Industry.INDUSTRY_FURNITUREFACTORY,
					Industry.INDUSTRY_CEMENTFACTORY,
				]
			},
			{
				"name": "Process 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_CLOTHESFACTORY,
					Industry.INDUSTRY_GLASSFACTORY,
				]
			},
		]
	},
	{
		"name": "Metalurgy",
		"techs": [
			{
				"name": "Metalurgy 1",
				"cost": 10,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_COALMINE,
				]
			},
			{
				"name": "Metalurgy 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_IRONMINE,
					Industry.INDUSTRY_COPPERMINE,
				]
			},
			{
				"name": "Metalurgy 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_PRECIOUSMETALMINE,
					Industry.INDUSTRY_RAREMETALMINE,
				]
			},
		]
	},
	{
		"name": "Advanced",
		"techs": [
			{
				"name": "Advanced 1",
				"cost": 10,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_STEELMILL,
				]
			},
			{
				"name": "Advanced 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_OILWELL,
				]
			},
			{
				"name": "Advanced 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_REFINARY,
					Industry.INDUSTRY_RADIOFACTORY,
				]
			},
			{
				"name": "Advanced 4",
				"cost": 40,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_PLASTICFACTORY,
					Industry.INDUSTRY_GUNFACTORY,
				]
			},
			{
				"name": "Advanced 5",
				"cost": 50,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_ELECTRONICCOMPONENTSFACTORY,
					Industry.INDUSTRY_ENGINEFACTORY,
					Industry.INDUSTRY_CARFACTORY,
				]
			},
			{
				"name": "Advanced 6",
				"cost": 60,
				"unlocked": False,
				"unlocks": [
					Industry.INDUSTRY_COMPUTERFACTORY,
					Industry.INDUSTRY_PLANESFACTORY,
					Industry.INDUSTRY_PHONEFACTORY,
				]
			},
		]
	},
]

def add_tech(i, j):
	# TODO add check if player has enough science points
	j = j if i < len(techTree) else j + 3
	i = i if i < len(techTree) else len(techTree) - 1
	tech = techTree[i]['techs'][j]
	if player.science < tech['cost']:
		return
	if j != 0 and not techTree[i]['techs'][j - 1]['unlocked']:
		return
	player.science -= tech['cost']
	tech['unlocked'] = True
	for unlock in tech['unlocks']:
		unlocked.append(unlock)

def get_unlocked_techs():
	return [
		tech
			for tree in techTree
			for tech in tree['techs'] if tech['unlocked']
	]

def get_unlocked_buildings():
	return [
		*unlocked,
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