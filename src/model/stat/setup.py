from model.market import player_wallet
from .utils import model_stat_setup_add_stat

def model_stat_setup_get_money():
	res = player_wallet.model_market_wallet_money_incr
	player_wallet.model_market_wallet_money_incr = 0
	return res

def model_stat_setup_get_science():
	res = player_wallet.model_market_wallet_science_incr
	player_wallet.model_market_wallet_science_incr = 0
	return res

def model_stat_setup_average(data):
	if len(data) <= 0:
		return 0
	res = 0
	for elem in data:
		res += elem
	return res / len(data)

def model_stat_setup_setup_stats():
	model_stat_setup_add_stat(
		'money',
		model_stat_setup_get_money,
		lambda data: model_stat_setup_average(data)
	)
	model_stat_setup_add_stat(
		'science',
		model_stat_setup_get_science,
		lambda data: model_stat_setup_average(data)
	)