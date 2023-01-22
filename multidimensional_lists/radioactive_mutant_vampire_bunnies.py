def left(a_matrix, columns_n, row, index):
    if index - 1 in range(columns_n) and a_matrix[row][index - 1][0] != 'B':
        return True

    return False


def up(a_matrix, rows_n, row, index):
    if row - 1 in range(rows_n) and a_matrix[row - 1][index][0] != 'B':
        return True

    return False


def right(a_matrix, columns_n, row, index):
    if index + 1 in range(columns_n) and a_matrix[row][index + 1][0] != 'B':
        return True

    return False


def down(a_matrix, rows_n, row, index):
    if row + 1 in range(rows_n) and a_matrix[row + 1][index][0] != 'B':
        return True

    return False


def mutating_bunnies(a_matrix, the_rows, the_columns, turn):
    for current_row in range(the_rows):
        for i in range(the_columns):

            if a_matrix[current_row][i][0] == 'B' and a_matrix[current_row][i][1] < turn:

                if left(a_matrix, the_columns, current_row, i):
                    a_matrix[current_row][i - 1] = ['B', turn]

                if right(a_matrix, the_columns, current_row, i):
                    a_matrix[current_row][i + 1] = ['B', turn]

                if up(a_matrix, the_rows, current_row, i):
                    a_matrix[current_row - 1][i] = ['B', turn]

                if down(a_matrix, the_rows, current_row, i):
                    a_matrix[current_row + 1][i] = ['B', turn]

                a_matrix[current_row][i][1] = turn

    return a_matrix


rows, columns = tuple(map(int, input().split(' ')))
matrix = []
player_position = [0, 0, '']
commands_dict = {
    'L': lambda row, index: [row, index - 1, ''] if index - 1 in range(columns) else [row, index, 'alive'],
    'R': lambda row, index: [row, index + 1, ''] if index + 1 in range(columns) else [row, index, 'alive'],
    'U': lambda row, index: [row - 1, index, ''] if row - 1 in range(rows) else [row, index, 'alive'],
    'D': lambda row, index: [row + 1, index, ''] if row + 1 in range(rows) else [row, index, 'alive']
}

for i in range(rows):
    row = list(input())
    for el in range(columns):
        if row[el] == 'B':
            row[el] = ['B', -1]

    if 'P' in row:
        player_position[0] = i
        player_position[1] = row.index('P')
        row[row.index('P')] = '.'

    matrix.append(row)


commands = list(input())

for current_turn, command in enumerate(commands):

    player_position = commands_dict[command](player_position[0], player_position[1])

    matrix = mutating_bunnies(matrix, rows, columns, current_turn)

    if matrix[player_position[0]][player_position[1]][0] == 'B' and not player_position[-1]:
        player_position[-1] = 'dead'

    if player_position[-1]:
        break

for row in matrix:
    print(''.join([el[0] for el in row]))

if player_position[-1] == 'alive':
    print(f'won: {player_position[0]} {player_position[1]}')
else:
    print(f'dead: {player_position[0]} {player_position[1]}')
