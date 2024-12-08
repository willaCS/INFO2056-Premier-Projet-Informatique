from model.market import player_wallet
from .utils import add_stat

def get_money():
	print('xxx', player_wallet.money_incr)
	res = player_wallet.money_incr
	player_wallet.money_incr = 0
	return res

def average(data):
	if len(data) <= 0:
		return 0
	res = 0
	print(data)
	for elem in data:
		res += elem
	return res / len(data)

def setup_stats():
	add_stat(
		'money',
		get_money,
		lambda data: average(data)
	)