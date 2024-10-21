import time

testing = {}
def add_test(funcName, time):
	global testing
	if not funcName in testing:
		testing[funcName] = {
			"time": 0,
			"n": 0
		}
	testing[funcName]["time"] += time
	testing[funcName]["n"] += 1

def time_tester(func):
	def wrapper(*args):
		global testing
		t0 = time.time()
		result = func(*args)
		add_test(func.__name__, time.time() - t0)
		return result
	return wrapper

def test_tick():
	global testing
	for elem in testing:
		n = testing[elem]["n"]
		time = testing[elem]["time"]
		print(f"{elem: <30s}: {n:<10d} {time}")
		testing[elem]["time"] = 0
		testing[elem]["n"] = 0
	return 1