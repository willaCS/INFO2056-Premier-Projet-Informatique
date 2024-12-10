from model.market import stockpile
from model.industry.plants import map, plant_add_experience
from model.market import player_wallet
from model.industry import Plant, technologies

def market_tick():
	for plant in sorted(map.values(), key=lambda item: Plant.type(item)):
		industry_tick(plant)
	stockpile.sell_stock_to_market()

def industry_tick(tile):
	generate_goods(tile)

def generate_goods(tile, amount = 1):	
	techno = technologies.industry[Plant.type(tile)]

	for input in techno['input']:
		stockpile.buy_stock(input, amount)
	stockpile.add_stock(techno['output'], amount)

	tile['generated'] += amount

	if tile['generated'] % 100 == 0:
		player_wallet.science += 1
