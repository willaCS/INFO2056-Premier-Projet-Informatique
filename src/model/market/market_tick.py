from model.market import stockpile
from model.industry.plants import model_plants_map, plant_add_experience
from model.market import player_wallet
from model.industry import Plant, technologies

def model_market_tick_market_tick():
	for plant in sorted(model_plants_map.values(), key=lambda item: Plant.model_Plant_type(item)):
		model_market_tick_industry_tick(plant)
	stockpile.model_market_stockpile_sell_stock_to_market()

def model_market_tick_industry_tick(tile):
	model_market_tick_generate_goods(tile)

def model_market_tick_generate_goods(tile, amount = 1):	
	techno = technologies.model_technologies_industry[Plant.model_Plant_type(tile)]

	for input in techno['input']:
		stockpile.model_market_stockpile_buy_stock(input, amount)
	stockpile.model_market_stockpile_add_stock(techno['output'], amount)

	tile['generated'] += amount

	if tile['generated'] % 100 == 0:
		player_wallet.model_market_wallet_science += 1
