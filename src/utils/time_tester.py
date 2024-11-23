import time
from typing import Any, Callable, Dict

testing: Dict[str, Dict[str, int | float]] = {}

def add_test(funcName: str, time: float) -> None:
	global testing
	if not funcName in testing:
		testing[funcName] = {
			"time": 0,
			"n": 0
		}
	testing[funcName]["time"] += time
	testing[funcName]["n"] += 1

def time_tester(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
	def wrapper(*args: Any):
		global testing
		t0 = time.time()
		result = func(*args)
		add_test(func.__name__, time.time() - t0)
		return result
	return wrapper

def test_tick() -> None:
	global testing
	for elem in testing:
		n = testing[elem]["n"]
		time = testing[elem]["time"]
		print(f"{elem: <30s}: {n:<10d} {time}")
		testing[elem]["time"] = 0
		testing[elem]["n"] = 0


def get_lambda_source(lambda_func, position):
    import inspect
    import ast
    import astunparse
    code_string = inspect.getsource(lambda_func).lstrip()
    class LambdaGetter(ast.NodeTransformer):
        def __init__(self):
            super().__init__()
            self.lambda_sources = []

        def visit_Lambda(self, node):
            self.lambda_sources.append(astunparse.unparse(node).strip()[1:-1])

        def get(self, code_string):
            tree = ast.parse(code_string)
            self.visit(tree)
            return self.lambda_sources
    return LambdaGetter().get(code_string)[position]