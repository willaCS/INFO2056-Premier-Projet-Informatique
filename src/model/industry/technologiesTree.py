from model.industry import technologies
from model.market import player_wallet

unlocked = [
	technologies.INDUSTRY_WHEAT_FIELDS,
	technologies.INDUSTRY_FISHINGBOAT,
	technologies.INDUSTRY_LUMBERMILL,
	technologies.INDUSTRY_STONEQUERY,
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
					technologies.INDUSTRY_POTATO_FIELDS,
					technologies.INDUSTRY_BREADFACTORY,
				]
			},
			{
				"name": "Food 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_SALTEXTRACTION,
					technologies.INDUSTRY_RICE_FIELDS,
				]
			},
			{
				"name": "Food 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_SUSHIFACTORY,
					technologies.INDUSTRY_ALCOHOLFACTORY,
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
					technologies.INDUSTRY_COTTON_FIELDS,
					technologies.INDUSTRY_SANDQUERY,
				]
			},
			{
				"name": "Process 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_TEXTILEFACTORY,
					technologies.INDUSTRY_FURNITUREFACTORY,
					technologies.INDUSTRY_CEMENTFACTORY,
				]
			},
			{
				"name": "Process 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_CLOTHESFACTORY,
					technologies.INDUSTRY_GLASSFACTORY,
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
					technologies.INDUSTRY_COALMINE,
				]
			},
			{
				"name": "Metalurgy 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_IRONMINE,
					technologies.INDUSTRY_COPPERMINE,
				]
			},
			{
				"name": "Metalurgy 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_PRECIOUSMETALMINE,
					technologies.INDUSTRY_RAREMETALMINE,
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
					technologies.INDUSTRY_STEELMILL,
				]
			},
			{
				"name": "Advanced 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_OILWELL,
				]
			},
			{
				"name": "Advanced 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_REFINARY,
					technologies.INDUSTRY_RADIOFACTORY,
				]
			},
			{
				"name": "Advanced 4",
				"cost": 40,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_PLASTICFACTORY,
					technologies.INDUSTRY_GUNFACTORY,
				]
			},
			{
				"name": "Advanced 5",
				"cost": 50,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_ELECTRONICCOMPONENTSFACTORY,
					technologies.INDUSTRY_ENGINEFACTORY,
					technologies.INDUSTRY_CARFACTORY,
				]
			},
			{
				"name": "Advanced 6",
				"cost": 60,
				"unlocked": False,
				"unlocks": [
					technologies.INDUSTRY_COMPUTERFACTORY,
					technologies.INDUSTRY_PLANESFACTORY,
					technologies.INDUSTRY_PHONEFACTORY,
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
	if player_wallet.science < tech['cost']:
		return
	if j != 0 and not techTree[i]['techs'][j - 1]['unlocked']:
		return
	player_wallet.science -= tech['cost']
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