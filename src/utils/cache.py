from typing import Any, Callable, Dict, Tuple


def add_cache(arg_func: Callable[[Tuple[int, int]], Any]) -> Callable[[Tuple[int, int]], Any]:
	cache: Dict[Tuple[int, int], int] = {}
	
	def wrapper(coord):
		if cache.get(coord) == None:
			res = arg_func(coord)
			cache[coord] = res
		return cache.get(coord)
	return wrapper