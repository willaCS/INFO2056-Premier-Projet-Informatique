from model.market import player_wallet
from model.market.market import buy_market, sell_market

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
	# TODO : sell stock only by bundle of 1000
	
	for s in stock:
		if stock[s] == 0:
			continue
		elif stock[s] > 0:
			if stock[s] // BUNDLE_SIZE > 0:
				num_bundle = stock[s] // BUNDLE_SIZE
				stock[s] = stock[s] % BUNDLE_SIZE
				sell_market(num_bundle, stock[s])
		else:
			buy_market(s, -stock[s])
			stock[s] = 0
	player_wallet.money_incr = player_wallet.money - original_money

