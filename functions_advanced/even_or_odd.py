def even_odd(*args):

    command = args[-1]
    digits = args[:len(args) - 1]

    command_dict = {
        'even': [n for n in digits if n % 2 == 0],
        'odd': [n for n in digits if n % 2 != 0]
    }

    return command_dict[command]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
