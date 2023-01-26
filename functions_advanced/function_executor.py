def func_executor(*args):

    func_results = [f'{func.__name__} - {func(*parameters)}' for func, parameters in args]

    return '\n'.join(func_results)
