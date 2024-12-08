import pygame


stats = {}

DELAY = 1000
STAT_RESET = 10

def add_stat(key, add, get):
	print('xd')
	stats[key] = {
		"data": [],
		"add": add,
		"get": get,
	}


prev_time = 0
def stat_tick():
	global prev_time
	time = pygame.time.get_ticks()
	if prev_time + DELAY > time:
		return
	prev_time = time
	for key, elem in stats.items():
		if len(elem["data"]) >= STAT_RESET:
			elem["data"].remove(elem["data"][0])
		x = elem["add"]()
		elem["data"].append(x)
		print(elem["data"], x)


def get_stat(key):
	if key not in stats:
		return 0
	return stats[key]["get"](stats[key]["data"])