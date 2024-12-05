import inspect


def introspection_info(obj):
    type1 = type(obj)
    some_module = inspect.getmodule(obj)
    return f'{type1}, {dir(obj)}, {inspect.getmodule(introspection_info)}'


number_info = introspection_info(42)
print(number_info)
