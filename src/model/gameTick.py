from model import Speed
from model.market.market_tick import model_market_tick_market_tick
from model.stat import utils

def model_gameTick_game_model_tick():
	if Speed.model_speed_can_execute_simulation():
		model_market_tick_market_tick()
		utils.model_stat_setup_stat_tick()