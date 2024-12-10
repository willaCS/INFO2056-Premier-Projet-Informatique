import pygame


model_stat_setup_stats = {}

model_stat_setup_DELAY = 1000
model_stat_setup_STAT_RESET = 10

def model_stat_setup_add_stat(key, add, get):
	model_stat_setup_stats[key] = {
		"data": [],
		"add": add,
		"get": get,
	}


model_stat_setup_prev_time = 0
def model_stat_setup_stat_tick():
	global model_stat_setup_prev_time
	time = pygame.time.get_ticks()
	if model_stat_setup_prev_time + model_stat_setup_DELAY > time:
		return
	model_stat_setup_prev_time = time
	for key, elem in model_stat_setup_stats.items():
		if len(elem["data"]) >= model_stat_setup_STAT_RESET:
			elem["data"].remove(elem["data"][0])
		x = elem["add"]()
		elem["data"].append(x)


def model_stat_setup_get_stat(key):
	if key not in model_stat_setup_stats:
		return 0
	return model_stat_setup_stats[key]["get"](model_stat_setup_stats[key]["data"])