def naughty_or_nice_list(*args, **kwargs):
    kids_list = args[0]
    kids_nums = [kid[0] for kid in kids_list]
    kids_names = [kid[1] for kid in kids_list]
    more_kids = kwargs
    santa_list = {'Nice': [], 'Naughty': [], 'Not found': []}

    for command in range(args.index(kids_list) + 1, len(args)):
        current_command = args[command].split('-')
        count_n, grade = int(current_command[0]), current_command[1]

        if kids_nums.count(count_n) == 1:
            kid_index = kids_nums.index(count_n)

            santa_list[grade].append(kids_names.pop(kid_index))
            kids_nums.remove(count_n)

    for name in more_kids:

        if kids_names.count(name) == 1:
            name_grade = more_kids[name]

            santa_list[name_grade].append(kids_names.pop(kids_names.index(name)))

    [santa_list['Not found'].append(name) for name in kids_names]

    return '\n'.join([f'{grade}: {", ".join(names)}' for grade, names in santa_list.items() if names])


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))