import inspect

def call(user_func, **kwargs):
    sig = inspect.signature(user_func)
    supported_args = sig.parameters.keys()
    filtered_kwargs = {k: v for k, v in kwargs.items() if k in supported_args}
    return user_func(**filtered_kwargs)