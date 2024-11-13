from logic import stockpile
from map.Map import map
from map.generation import map as generation
from map import Industry, Ressource, TerrainTile, Tile
from globals import player

def game_simulation_tick():
	for tile in sorted(map.values(), key=lambda item: Tile.subtype(item)):
		match Tile.type(tile):
			case Tile.TILETYPE_INDUSTRY:
				simulation_industry(tile, generation.random_terrain_landscape(Tile.position(tile)))
			case _:
				pass
	stockpile.sell_stock_to_market()
	game_affichage_refresh()

i = 0
def game_affichage_refresh():
	global i
	
	if i < 100:
		i += 1
		return
	i = 0
	player.money_incr = 0
	player.science_incr = 0

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
			generate_goods(tile)
		
def generate_goods(tile, amount = None):

	if not 'xp' in tile:
		tile['xp'] = 0
	if not 'generated' in tile:
		tile['generated'] = 0

	industry = Industry.industry[Tile.subtype(tile)]

	if not amount:
		amount = int(1 + tile['xp'] / 100)
	print(amount, tile['xp'], tile['generated'])
	
	for input in industry['input']:
		stockpile.buy_stock(input, amount)
	stockpile.add_stock(industry['output'], amount)

	tile['xp'] += 1
	tile['generated'] += amount

	if tile['xp'] % 100 == 0:
		player.science += 1
		player.science_incr += 1
	
