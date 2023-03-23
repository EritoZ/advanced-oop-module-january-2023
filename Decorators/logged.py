def logged(func):
    def wrapper(*args):
        result = func(*args)
        message = (f'you called {func.__name__}{args}', f'it returned {result}')

        return '\n'.join(message)

    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))