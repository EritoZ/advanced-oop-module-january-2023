a_string = input()
size = int(input())
field = []
player_loc = []

commands_dict = {
    'left': lambda row, col: [row, col - 1] if col - 1 in range(size) else [row, col],
    'right': lambda row, col: [row, col + 1] if col + 1 in range(size) else [row, col],
    'up': lambda row, col: [row - 1, col] if row - 1 in range(size) else [row, col],
    'down': lambda row, col: [row + 1, col] if row + 1 in range(size) else [row, col]
}

for i in range(size):
    current_row = list(input())

    if 'P' in current_row:
        player_index = current_row.index('P')
        player_loc = [i, player_index]
        current_row[player_index] = '-'

    field.append(current_row)

commands_n = int(input())

for c in range(commands_n):
    command = input()

    player_loc_copy = player_loc.copy()

    player_loc = commands_dict[command](*player_loc)
    current_object = field[player_loc[0]][player_loc[1]]

    if player_loc == player_loc_copy:
        a_string = a_string[:len(a_string) - 1]

    elif current_object.isalpha():
        a_string += current_object
        field[player_loc[0]][player_loc[1]] = '-'

field[player_loc[0]][player_loc[1]] = 'P'

print(a_string)
[print(''.join(row)) for row in field]
