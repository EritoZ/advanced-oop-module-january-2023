def even_parameters(func):

    def wrapper(*args):
        check_not_even = [n for n in args if not isinstance(n, int) or n % 2 != 0]

        if check_not_even:
            return "Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))