from model.industry import technologies
from model.market import player_wallet
from model.terrain import Ressource, TerrainTile
from model.terrain.terrain import model_terrain_terrain_get_terrain_tile

model_technologyTree_default_unlocked = [
	technologies.model_technologies_INDUSTRY_WHEAT_FIELDS,
	technologies.model_technologies_INDUSTRY_FISHINGBOAT,
	technologies.model_technologies_INDUSTRY_LUMBERMILL,
	technologies.model_technologies_INDUSTRY_STONEQUERY,
]

model_technologyTree_techTree = [
	{
		"name": "Food",
		"techs": [
			{
				"name": "Food 1",
				"cost": 100,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_POTATO_FIELDS,
					technologies.model_technologies_INDUSTRY_BREADFACTORY,
				]
			},
			{
				"name": "Food 2",
				"cost": 250,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_SALTEXTRACTION,
					technologies.model_technologies_INDUSTRY_RICE_FIELDS,
				]
			},
			{
				"name": "Food 3",
				"cost": 750,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_SUSHIFACTORY,
					technologies.model_technologies_INDUSTRY_ALCOHOLFACTORY,
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
					technologies.model_technologies_INDUSTRY_COTTON_FIELDS,
					technologies.model_technologies_INDUSTRY_SANDQUERY,
				]
			},
			{
				"name": "Process 2",
				"cost": 250,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_TEXTILEFACTORY,
					technologies.model_technologies_INDUSTRY_FURNITUREFACTORY,
					technologies.model_technologies_INDUSTRY_CEMENTFACTORY,
				]
			},
			{
				"name": "Process 3",
				"cost": 500,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_CLOTHESFACTORY,
					technologies.model_technologies_INDUSTRY_GLASSFACTORY,
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
					technologies.model_technologies_INDUSTRY_COALMINE,
				]
			},
			{
				"name": "Metalurgy 2",
				"cost": 500,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_IRONMINE,
					technologies.model_technologies_INDUSTRY_COPPERMINE,
				]
			},
			{
				"name": "Metalurgy 3",
				"cost": 5000,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_PRECIOUSMETALMINE,
					technologies.model_technologies_INDUSTRY_RAREMETALMINE,
					technologies.model_technologies_INDUSTRY_JEWELRYWORKSHOP,
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
					technologies.model_technologies_INDUSTRY_STEELMILL,
				]
			},
			{
				"name": "Advanced 2",
				"cost": 20,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_OILWELL,
				]
			},
			{
				"name": "Advanced 3",
				"cost": 30,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_REFINARY,
					technologies.model_technologies_INDUSTRY_RADIOFACTORY,
				]
			},
			{
				"name": "Advanced 4",
				"cost": 40,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_PLASTICFACTORY,
					technologies.model_technologies_INDUSTRY_GUNFACTORY,
				]
			},
			{
				"name": "Advanced 5",
				"cost": 50,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_ELECTRONICCOMPONENTSFACTORY,
					technologies.model_technologies_INDUSTRY_ENGINEFACTORY,
					technologies.model_technologies_INDUSTRY_CARFACTORY,
				]
			},
			{
				"name": "Advanced 6",
				"cost": 60,
				"unlocked": False,
				"unlocks": [
					technologies.model_technologies_INDUSTRY_COMPUTERFACTORY,
					technologies.model_technologies_INDUSTRY_PLANESFACTORY,
					technologies.model_technologies_INDUSTRY_PHONEFACTORY,
				]
			},
		]
	},
]

# action by player to unlock a technology
def model_technologyTree_add_tech(i, j):
	# TODO add check if player has enough science points
	j = j if i < len(model_technologyTree_techTree) else j + 3
	i = i if i < len(model_technologyTree_techTree) else len(model_technologyTree_techTree) - 1
	tech = model_technologyTree_techTree[i]['techs'][j]
	if tech['unlocked']:
		return
	if player_wallet.model_market_wallet_science < tech['cost']:
		return
	if j != 0 and not model_technologyTree_techTree[i]['techs'][j - 1]['unlocked']:
		return
	player_wallet.model_market_wallet_science -= tech['cost']
	tech['unlocked'] = True

def model_technologyTree_get_unlocked_techs():
	return [
		tech
			for tree in model_technologyTree_techTree
			for tech in tree['techs'] if tech['unlocked']
	]

def model_technologyTree_get_unlocked_buildings():
	return [
		*model_technologyTree_default_unlocked,
		*(unlock
			for tree in model_technologyTree_techTree
			for tech in tree['techs'] if tech['unlocked']
			for unlock in tech['unlocks']
		)
	]

def model_technologyTree_get_tech_for_draw(i, j):
	j = j if i < len(model_technologyTree_techTree) else j + 3
	i = i if i < len(model_technologyTree_techTree) else len(model_technologyTree_techTree) - 1
	return model_technologyTree_techTree[i]['techs'][j]


def model_technologyTree_get_placable_on(coord):
	if not coord:
		return []
	unlocked = model_technologyTree_get_unlocked_buildings()
	terrain = model_terrain_terrain_get_terrain_tile(coord)
	ressource = TerrainTile.model_terrain_terrainTile_ressource(terrain)
	
	res = []
	for indus in technologies.model_technologies_industry:
		if not indus in unlocked:
			continue
		test_ind = technologies.model_technologies_industry[indus]
		for place_on in test_ind['place_on']:
			if place_on['type'] == technologies.model_technologies_PLACE_ON_RESSOURCE:
				if ressource and place_on['id'] == Ressource.model_terrain_ressource_type(ressource):
					res.append(indus)
			elif place_on['type'] == technologies.model_technologies_PLACE_ON_TERRAIN:
				if place_on['id'] == TerrainTile.model_terrain_terrainTile_type(terrain):
					res.append(indus)
	return res