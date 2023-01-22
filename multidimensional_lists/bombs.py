def left(matrix, rows_n, row, index):
    if index - 1 in range(len(matrix[row])) and matrix[row][index - 1] > 0:
        return True

    return False


def up_left(matrix, rows_n, row, index):
    if row - 1 in range(rows_n) and index - 1 in range(len(matrix[row])) and matrix[row - 1][index - 1] > 0:
        return True

    return False


def up(matrix, rows_n, row, index):
    if row - 1 in range(rows_n) and matrix[row - 1][index] > 0:
        return True

    return False


def up_right(matrix, rows_n, row, index):
    if row - 1 in range(rows_n) and index + 1 in range(len(matrix[row])) and matrix[row - 1][index + 1] > 0:
        return True

    return False


def right(matrix, rows_n, row, index):
    if index + 1 in range(len(matrix[row])) and matrix[row][index + 1] > 0:
        return True

    return False


def down_right(matrix, rows_n, row, index):
    if row + 1 in range(rows_n) and index + 1 in range(len(matrix[row])) and matrix[row + 1][index + 1] > 0:
        return True

    return False


def down(matrix, rows_n, row, index):
    if row + 1 in range(rows_n) and matrix[row + 1][index] > 0:
        return True

    return False


def down_left(matrix, rows_n, row, index):
    if row + 1 in range(rows_n) and index - 1 in range(len(matrix[row])) and matrix[row + 1][index - 1] > 0:
        return True

    return False


rows = int(input())
a_matrix = [list(map(int, input().split())) for row in range(rows)]
bombs = input().split()

for bomb in bombs:
    coordinates = bomb.split(',')
    current_row, current_index = int(coordinates[0]), int(coordinates[1])

    bomb_dmg = a_matrix[current_row][current_index]

    if bomb_dmg > 0:
        a_matrix[current_row][current_index] = 0

        if left(a_matrix, rows, current_row, current_index):
            a_matrix[current_row][current_index - 1] -= bomb_dmg

        if up_left(a_matrix, rows, current_row, current_index):
            a_matrix[current_row - 1][current_index - 1] -= bomb_dmg

        if up(a_matrix, rows, current_row, current_index):
            a_matrix[current_row - 1][current_index] -= bomb_dmg

        if up_right(a_matrix, rows, current_row, current_index):
            a_matrix[current_row - 1][current_index + 1] -= bomb_dmg

        if right(a_matrix, rows, current_row, current_index):
            a_matrix[current_row][current_index + 1] -= bomb_dmg

        if down_right(a_matrix, rows, current_row, current_index):
            a_matrix[current_row + 1][current_index + 1] -= bomb_dmg

        if down(a_matrix, rows, current_row, current_index):
            a_matrix[current_row + 1][current_index] -= bomb_dmg

        if down_left(a_matrix, rows, current_row, current_index):
            a_matrix[current_row + 1][current_index - 1] -= bomb_dmg

alive_cells = 0
sum_value = 0

for row in a_matrix:
    filtered_row = [n for n in row if n > 0]

    alive_cells += len(filtered_row)
    sum_value += sum(filtered_row)

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_value}')
for row in a_matrix:
    print(' '.join(map(str, row)))
