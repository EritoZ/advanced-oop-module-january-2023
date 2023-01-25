def even_odd_filter(**kwargs):

    command_dict = {
        'odd': lambda x: [n for n in kwargs[x] if n % 2 != 0],
        'even': lambda x: [n for n in kwargs[x] if n % 2 == 0]
    }

    for key in kwargs:
        kwargs[key] = command_dict[key](key)

    return dict(sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))