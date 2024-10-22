from typing import Any, Callable, Dict, Tuple


def add_cache(arg_func: Callable[[Tuple[int, int]], Any]) -> Callable[[Tuple[int, int]], Any]:
	cache: Dict[Tuple[int, int], int] = {}
	
	def wrapper(coord, refresh = False):
		if refresh or cache.get(coord) == None:
			cache[coord] = arg_func(coord)
		return cache.get(coord)
	return wrapper