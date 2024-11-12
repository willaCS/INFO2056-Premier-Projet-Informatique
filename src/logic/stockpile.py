from globals import player
from logic.market import buy_market, sell_market

stock = {}

def add_stock(ressource_type, amount):
	if not ressource_type in stock:
		stock[ressource_type] = 0
	stock[ressource_type] += amount

def buy_stock(ressource_type, amount):
	if not ressource_type in stock:
		stock[ressource_type] = 0
	stock[ressource_type] -= amount

def sell_stock_to_market():
	original_money = player.money
	for s in stock:
		if stock[s] == 0:
			continue
		elif stock[s] > 0:
			sell_market(s, stock[s])
		else:
			buy_market(s, -stock[s])
		stock[s] = 0
	player.money_incr = player.money - original_money

