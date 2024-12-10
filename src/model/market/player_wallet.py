money = 10
money_incr = 0
science = 0
science_incr = 0

def has_money(price):
	return money >= price

def buy(price):
	global money, money_incr
	money -= price
	money_incr -= price

def buy2(price):
	global money
	money -= price

def sell(price):
	global money, money_incr
	money += price	
	money_incr += price