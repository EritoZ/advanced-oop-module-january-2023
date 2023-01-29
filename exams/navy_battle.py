battlefield_size = int(input())
matrix = []

commands_dict = {
    'left': lambda row, index: [row, index - 1] if index - 1 in range(battlefield_size) else [row, index],
    'right': lambda row, index: [row, index + 1] if index + 1 in range(battlefield_size) else [row, index],
    'up': lambda row, index: [row - 1, index] if row - 1 in range(battlefield_size) else [row, index],
    'down': lambda row, index: [row + 1, index] if row + 1 in range(battlefield_size) else [row, index]
}

for i in range(battlefield_size):
    current_row = list(input())

    if 'S' in current_row:
        submarine_loc = [i, current_row.index('S')]

    matrix.append(current_row)

hits = 0
battle_cruisers = 3

while hits < 3 and battle_cruisers:

    command = input()

    matrix[submarine_loc[0]][submarine_loc[1]] = '-'

    submarine_loc = commands_dict[command](submarine_loc[0], submarine_loc[1])

    if matrix[submarine_loc[0]][submarine_loc[1]] == '*':
        hits += 1

    elif matrix[submarine_loc[0]][submarine_loc[1]] == 'C':
        battle_cruisers -= 1


matrix[submarine_loc[0]][submarine_loc[1]] = 'S'

if not battle_cruisers:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
else:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {submarine_loc}!")

[print(''.join(row)) for row in matrix]
