from typing import Any, Callable, Dict
from .mytyping import coord_i


def add_cache(arg_func: Callable[[coord_i], Any]) -> Callable[[coord_i], Any]:
	cache: Dict[coord_i, int] = {}
	
	def wrapper(coord: coord_i, refresh: bool = False):
		if refresh or cache.get(coord) == None:
			cache[coord] = arg_func(coord)
		return cache.get(coord)
	return wrapper