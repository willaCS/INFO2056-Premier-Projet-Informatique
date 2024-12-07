from model.market import player_wallet
from model.market.market import buy_market, get_bundle_size, sell_market

BUNDLE_SIZE = 100

stock = {}

def get_stock(ressource_type):
	return stock.get(
		ressource_type,
		0
	)

def add_stock(ressource_type, amount):
	if not ressource_type in stock:
		stock[ressource_type] = 0
	stock[ressource_type] += amount

def buy_stock(ressource_type, amount):
	if not ressource_type in stock:
		stock[ressource_type] = 0
	stock[ressource_type] -= amount

def sell_stock_to_market():
	original_money = player_wallet.money
	
	for s in stock:
		if stock[s] == 0:
			continue
		elif stock[s] > 0:
			bundle_size = get_bundle_size(s)
			if stock[s] // bundle_size > 0:
				num_bundle = stock[s] // bundle_size
				stock[s] = stock[s] % bundle_size
				sell_market(s, num_bundle)
		else:
			buy_market(s, -stock[s])
			stock[s] = 0
	player_wallet.money_incr = player_wallet.money - original_money

