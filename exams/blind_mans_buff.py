rows, columns = map(int, input().split())
playground = []
me_loc = []
touched_opponents = 0
moves = 0
commands_dict = {
    'left': lambda row, col: [row, col - 1] if col - 1 in range(columns) else [row, col],
    'right': lambda row, col: [row, col + 1] if col + 1 in range(columns) else [row, col],
    'up': lambda row, col: [row - 1, col] if row - 1 in range(rows) else [row, col],
    'down': lambda row, col: [row + 1, col] if row + 1 in range(rows) else [row, col]
}

for i in range(rows):
    current_row = input().split()

    if 'B' in current_row:
        me_loc = [i, current_row.index('B')]
        current_row[current_row.index('B')] = '-'

    playground.append(current_row)

command = input()
while command != 'Finish' and touched_opponents != 3:

    future_loc = commands_dict[command](me_loc[0], me_loc[1])
    current_object = playground[future_loc[0]][future_loc[1]]

    if current_object != 'O' and me_loc != future_loc:
        me_loc = future_loc
        moves += 1

        if current_object == 'P':
            touched_opponents += 1
            playground[me_loc[0]][me_loc[1]] = '-'

    command = input()

print(f'''Game over!
Touched opponents: {touched_opponents} Moves made: {moves}''')
