model_market_wallet_money = 10
model_market_wallet_money_incr = 0
model_market_wallet_science = 0
model_market_wallet_science_incr = 0

def model_market_wallet_has_money(price):
	return model_market_wallet_money >= price

def model_market_wallet_buy(price):
	global model_market_wallet_money, model_market_wallet_money_incr
	model_market_wallet_money -= price
	model_market_wallet_money_incr -= price

def model_market_wallet_buy2(price):
	global model_market_wallet_money
	model_market_wallet_money -= price

def model_market_wallet_sell(price):
	global model_market_wallet_money, model_market_wallet_money_incr
	model_market_wallet_money += price	
	model_market_wallet_money_incr += price