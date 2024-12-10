from model.stat import utils
from model.market import player_wallet
from model.market.market import model_market_market_buy_market, model_market_market_get_bundle_size, model_market_market_sell_market

model_market_stockpile_stock = {}

def model_market_stockpile_get_stock(ressource_type):
	return model_market_stockpile_stock.get(
		ressource_type,
		0
	)

def model_market_stockpile_add_stock(ressource_type, amount):
	if not ressource_type in model_market_stockpile_stock:
		model_market_stockpile_stock[ressource_type] = 0
	model_market_stockpile_stock[ressource_type] += amount

def model_market_stockpile_buy_stock(ressource_type, amount):
	if not ressource_type in model_market_stockpile_stock:
		model_market_stockpile_stock[ressource_type] = 0
	model_market_stockpile_stock[ressource_type] -= amount

original_money = player_wallet.model_market_wallet_money

def model_market_stockpile_sell_stock_to_market():
	global original_money

	for s in model_market_stockpile_stock:
		if model_market_stockpile_stock[s] == 0:
			continue
		elif model_market_stockpile_stock[s] > 0:
			bundle_size = model_market_market_get_bundle_size(s)
			if model_market_stockpile_stock[s] // bundle_size > 0:
				num_bundle = model_market_stockpile_stock[s] // bundle_size
				model_market_stockpile_stock[s] = model_market_stockpile_stock[s] % bundle_size
				model_market_market_sell_market(s, num_bundle)
		else:
			model_market_market_buy_market(s, -model_market_stockpile_stock[s])
			model_market_stockpile_stock[s] = 0
	player_wallet.model_market_wallet_money_incr = player_wallet.model_market_wallet_money - original_money
	original_money = player_wallet.model_market_wallet_money

