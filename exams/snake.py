size = int(input())
field = []
snek_loc = []
burrows_locs = []
food_eaten = 0

commands_dict = {
    'left': lambda row, col: [row, col - 1, ''] if col - 1 in range(size) else [row, col, 'game over'],
    'right': lambda row, col: [row, col + 1, ''] if col + 1 in range(size) else [row, col, 'game over'],
    'up': lambda row, col: [row - 1, col, ''] if row - 1 in range(size) else [row, col, 'game over'],
    'down': lambda row, col: [row + 1, col, ''] if row + 1 in range(size) else [row, col, 'game over']
}

for i in range(size):
    current_row = list(input())

    if 'S' in current_row:
        snek_loc = [i, current_row.index('S'), '']
        current_row[current_row.index('S')] = '.'

    [burrows_locs.append([i, col, '']) for col, object in enumerate(current_row) if object == 'B']

    field.append(current_row)

while food_eaten != 10:

    command = input()

    snek_loc = commands_dict[command](snek_loc[0], snek_loc[1])

    current_row, current_col = snek_loc[0], snek_loc[1]

    if snek_loc[-1]:
        break

    current_object = field[current_row][current_col]

    if current_object == '*':
        food_eaten += 1

    elif current_object == 'B':
        snek_loc = burrows_locs[0] if burrows_locs[0] != snek_loc else burrows_locs[1]

        field[burrows_locs[0][0]][burrows_locs[0][1]] = '.'
        field[burrows_locs[1][0]][burrows_locs[1][1]] = '.'

    field[current_row][current_col] = '.'

if food_eaten == 10:
    field[current_row][current_col] = 'S'

    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food_eaten}")

[print(''.join(row)) for row in field]
