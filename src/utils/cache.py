from typing import Any, Callable, Dict
from .mytyping import utils_myTyping_coord_i


def utils_cache_add_cache(arg_func: Callable[[utils_myTyping_coord_i], Any]) -> Callable[[utils_myTyping_coord_i], Any]:
	cache: Dict[utils_myTyping_coord_i, int] = {}
	
	def wrapper(coord: utils_myTyping_coord_i, refresh: bool = False):
		if refresh or cache.get(coord) == None:
			cache[coord] = arg_func(coord)
		return cache.get(coord)
	return wrapper