import inspect

name_func_tuples = inspect.getmembers(SOME_MODULE_U_IMPORTED, inspect.isfunction)
name_func_tuples = [t for t in name_func_tuples if inspect.getmodule(t[1]) == SOME_MODULE_U_IMPORTED]
functions = dict(name_func_tuples)
print(functions)
