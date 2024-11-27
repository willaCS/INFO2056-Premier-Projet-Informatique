from model.market import stockpile
from model.industry.plants import map, plant_add_experience
from model.terrain import Ressource, TerrainTile, terrain
from model.market import player_wallet
from model.industry import Plant, technologies

def market_tick():
	for plant in sorted(map.values(), key=lambda item: Plant.type(item)):
		industry_tick(plant, terrain.get_terrain_tile(Plant.position(plant)))
	stockpile.sell_stock_to_market()

def industry_tick(tile, terrainTile):	
	match Plant.type(tile):
		case technologies.INDUSTRY_FISHINGBOAT \
			| technologies.INDUSTRY_SALTEXTRACTION \
			| technologies.INDUSTRY_WHEAT_FIELDS \
			| technologies.INDUSTRY_POTATO_FIELDS \
			| technologies.INDUSTRY_COTTON_FIELDS \
			| technologies.INDUSTRY_RICE_FIELDS \
			| technologies.INDUSTRY_FURHUNTINGGROUNDS \
			| technologies.INDUSTRY_LUMBERMILL \
			| technologies.INDUSTRY_OILWELL \
			| technologies.INDUSTRY_COALMINE \
			| technologies.INDUSTRY_IRONMINE \
			| technologies.INDUSTRY_COPPERMINE \
			| technologies.INDUSTRY_PRECIOUSMETALMINE \
			| technologies.INDUSTRY_RAREMETALMINE:
			generate_goods(tile, Ressource.richness(TerrainTile.ressource(terrainTile)))
		case _:
			generate_goods(tile)


def generate_goods(tile, amount = None):	
	techno = technologies.industry[Plant.type(tile)]

	if not amount:
		amount = int(1 + Plant.xp(tile) / 100)
	# print(amount, Plant.xp(tile), Plant.generated(tile))

	for input in techno['input']:
		stockpile.buy_stock(input, amount)
	stockpile.add_stock(techno['output'], amount)

	plant_add_experience(tile, amount)

	if tile['xp'] % 100 == 0:
		player_wallet.science += 1
		player_wallet.science_incr += 1
