from functools import reduce


def operate(operator, *args):

    operators_dict = {
        '+': reduce(lambda x, y: x + y, args),
        '-': reduce(lambda x, y: x - y, args),
        '*': reduce(lambda x, y: x * y, args),
        '/': reduce(lambda x, y: x / y, args)
    }

    return operators_dict[operator]


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 0, 4))
