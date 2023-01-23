size = int(input())
matrix = []
bunny_location = [0, 0]
directions_values = []
directions = {
    'right': lambda current_row, col: [[current_row, i] for i in range(col + 1, size)],
    'left': lambda current_row, col: [[current_row, i] for i in range(col - 1, -1, -1)],
    'up': lambda current_row, col: [[i, col] for i in range(current_row - 1, -1, -1)],
    'down': lambda current_row, col: [[i, col] for i in range(current_row + 1, size)]
}

for i in range(size):
    row = tuple(map(lambda x: int(x) if x[-1].isdigit() else x, input().split()))

    if 'B' in row:
        bunny_location[0] = i
        bunny_location[1] = row.index('B')

    matrix.append(row)

for direction in directions:

    direction_coordinates = directions[direction](bunny_location[0], bunny_location[1])
    direction_value = 0

    for i, (row_el, col_el) in enumerate(direction_coordinates):

        if matrix[row_el][col_el] == 'X':
            direction_coordinates = direction_coordinates[:i]
            break

        direction_value += matrix[row_el][col_el]

    directions_values.append((direction, direction_coordinates, direction_value))

most_valued_path = max(directions_values, key=lambda x: x[-1])

print(most_valued_path[0])
print('\n'.join(map(str, most_valued_path[1])))
print(most_valued_path[-1])
