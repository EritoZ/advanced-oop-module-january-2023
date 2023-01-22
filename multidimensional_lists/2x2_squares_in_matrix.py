rows, columns = tuple(map(int, input().split(' ')))
matrix = [tuple(input().split(' ')) for row in range(rows)]
identical_chars_counter = 0

for i_row in range(rows - 1):
    for i_column in range(columns - 1):

        if matrix[i_row][i_column] == matrix[i_row][i_column + 1] == matrix[i_row + 1][i_column] == \
                matrix[i_row + 1][i_column + 1]:

            identical_chars_counter += 1

print(identical_chars_counter)
