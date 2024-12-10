money = 150
money_incr = 0
science = 0
science_incr = 0

i = 0
def wallet_tick():
	global i, money_incr, science_incr
	
	if i < 100:
		i += 1
		return
	i = 0
	money_incr = 0
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