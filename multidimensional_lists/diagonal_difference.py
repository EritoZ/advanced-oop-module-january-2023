def primary_diagonal_finder(a_matrix, matrix_rows):
    diagonal_els = []

    for i in range(matrix_rows):
        diagonal_els.append(a_matrix[i][i])

    return diagonal_els, sum(diagonal_els)


def secondary_diagonal_finder(a_matrix, matrix_rows):
    diagonal_els = []

    for i in range(matrix_rows - 1, -1, -1):
        diagonal_els.append(a_matrix[matrix_rows - 1 - i][i])

    return diagonal_els, sum(diagonal_els)


rows = int(input())
matrix = tuple([tuple(map(int, input().split(' '))) for row in range(rows)])

first_diagonal, sum_d1 = primary_diagonal_finder(matrix, rows)
second_diagonal, sum_d2 = secondary_diagonal_finder(matrix, rows)

print(abs(sum_d1 - sum_d2))
