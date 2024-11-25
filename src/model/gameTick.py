from model import Speed
from model.market.market_tick import market_tick
from model.market.player_wallet import wallet_tick

def game_model_tick():
	if Speed.can_execute_simulation():
		market_tick()
		wallet_tick()