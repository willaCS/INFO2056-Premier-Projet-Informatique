from logic import stockpile
from map.Map import map
from map.generation import map as generation
from map import Industry, Ressource, TerrainTile, Tile

def game_simulation_tick():
	for tile in sorted(map.values(), key=lambda item: Tile.subtype(item)):
		match Tile.type(tile):
			case Tile.TILETYPE_INDUSTRY:
				simulation_industry(tile, generation.random_terrain_landscape(Tile.position(tile)))
			case _:
				pass
	stockpile.sell_stock_to_market()


def simulation_industry(tile, terrainTile):	
	match Tile.subtype(tile):
		case Industry.INDUSTRY_FISHINGBOAT \
			| Industry.INDUSTRY_SALTEXTRACTION \
			| Industry.INDUSTRY_WHEAT_FIELDS \
			| Industry.INDUSTRY_POTATO_FIELDS \
			| Industry.INDUSTRY_COTTON_FIELDS \
			| Industry.INDUSTRY_RICE_FIELDS \
			| Industry.INDUSTRY_FURHUNTINGGROUNDS \
			| Industry.INDUSTRY_LUMBERMILL \
			| Industry.INDUSTRY_OILWELL \
			| Industry.INDUSTRY_COALMINE \
			| Industry.INDUSTRY_IRONMINE \
			| Industry.INDUSTRY_COPPERMINE \
			| Industry.INDUSTRY_PRECIOUSMETALMINE \
			| Industry.INDUSTRY_RAREMETALMINE:
			generate_goods(tile, Ressource.richness(TerrainTile.ressource(terrainTile)))
		case _:
			generate_goods(tile, 1)
		
def generate_goods(tile, amount):
	if not 'generated' in tile:
		tile['generated'] = 0
	tile['generated'] += amount
	industry = Industry.industry[Tile.subtype(tile)]
	for input in industry['input']:
		rest = stockpile.buy_stock(input, 5)
		if rest > 0:
			stockpile.buy_market(input, rest)
	stockpile.add_stock(industry['output'], 5)


		
