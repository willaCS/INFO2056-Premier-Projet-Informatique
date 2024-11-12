from globals import player
from map.Goods import print_goods

stock = {}

def add_stock(ressource_type, amount):
	if not ressource_type in stock:
		stock[ressource_type] = 0
	stock[ressource_type] += amount

def buy_stock(ressource_type, amount):
	if not ressource_type in stock:
		return amount
	if stock[ressource_type] < amount:
		available_stock = stock[ressource_type]
		stock[ressource_type] = 0
		return available_stock
	else:
		stock[ressource_type] -= amount
		return amount

def sell_stock_to_market():
	for s in stock:
		sell_market(s, stock[s])
		stock[s] = 0

def sell_market(ressource_type, amounts):
	print('sell', amounts, 'de', print_goods(ressource_type))
	player.money += 1 * amounts

def buy_market(ressource_type, amounts):
	print('buy', amounts, 'de', print_goods(ressource_type))
	player.money -= 1 * amounts