size_data = map(int, input().split(', '))
rows, columns = size_data
santa_workshop = []
total_items = 0
items_dict = {
    'D': [0, 'Christmas decorations'],
    'G': [0, 'Gifts'],
    'C': [0, 'Cookies']
}
commands_dict = {
    'left': lambda row, index, steps: [[row, col_i % columns] for col_i in range(index - 1, index - steps - 1, -1)],
    'right': lambda row, index, steps: [[row, col_i % columns] for col_i in range(index + 1, index + steps + 1)],
    'up': lambda row, index, steps: [[row_i % rows, index] for row_i in range(row - 1, row - steps - 1, -1)],
    'down': lambda row, index, steps: [[row_i % rows, index] for row_i in range(row + 1, row + steps + 1)]
}

for i in range(rows):
    current_row = input().split()

    if 'Y' in current_row:
        my_loc = [i, current_row.index('Y')]
        current_row[current_row.index('Y')] = 'x'

    total_items += current_row.count('D') + current_row.count('G') + current_row.count('C')

    santa_workshop.append(current_row)

command = input()
while command != 'End':
    data = command.split('-')
    direction, current_steps = data[0], int(data[1])

    # noinspection PyUnboundLocalVariable
    coordinates_data = commands_dict[direction](*my_loc, current_steps)

    for coordinates in coordinates_data:

        current_object = santa_workshop[coordinates[0]][coordinates[1]]

        if current_object in ('D', 'G', 'C'):
            total_items -= 1
            items_dict[current_object][0] += 1

            if not total_items:
                break

        santa_workshop[coordinates[0]][coordinates[1]] = 'x'

    # noinspection PyUnboundLocalVariable
    my_loc[0], my_loc[1] = coordinates[0], coordinates[1]

    if not total_items:
        break

    command = input()

# noinspection PyUnboundLocalVariable
santa_workshop[my_loc[0]][my_loc[1]] = 'Y'

if not total_items:
    print("Merry Christmas!")

print("You've collected:")
for item in items_dict:
    print(f'- {items_dict[item][0]} {items_dict[item][1]}')

[print(' '.join(row)) for row in santa_workshop]
