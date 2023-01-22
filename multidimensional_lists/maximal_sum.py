rows, columns = tuple(map(int, input().split(' ')))
matrix = [tuple(map(int, input().split(' '))) for row in range(rows)]
most_sum = [0, []]

for i_row in range(rows - 2):
    for i_column in range(columns - 2):

        if sum([
            matrix[i_row][i_column], matrix[i_row][i_column + 1], matrix[i_row][i_column + 2],
            matrix[i_row + 1][i_column], matrix[i_row + 1][i_column + 1], matrix[i_row + 1][i_column + 2],
            matrix[i_row + 2][i_column], matrix[i_row + 2][i_column + 1], matrix[i_row + 2][i_column + 2]
        ]) >= most_sum[0]:

            most_sum[0] = sum([
                matrix[i_row][i_column], matrix[i_row][i_column + 1], matrix[i_row][i_column + 2],
                matrix[i_row + 1][i_column], matrix[i_row + 1][i_column + 1], matrix[i_row + 1][i_column + 2],
                matrix[i_row + 2][i_column], matrix[i_row + 2][i_column + 1], matrix[i_row + 2][i_column + 2]
            ])

            most_sum[1] = [
                matrix[i_row][i_column], matrix[i_row][i_column + 1], matrix[i_row][i_column + 2],
                matrix[i_row + 1][i_column], matrix[i_row + 1][i_column + 1], matrix[i_row + 1][i_column + 2],
                matrix[i_row + 2][i_column], matrix[i_row + 2][i_column + 1], matrix[i_row + 2][i_column + 2]
            ]

if most_sum[1]:
    print(f'''Sum = {most_sum[0]}
{most_sum[1][0]} {most_sum[1][1]} {most_sum[1][2]}
{most_sum[1][3]} {most_sum[1][4]} {most_sum[1][5]}
{most_sum[1][6]} {most_sum[1][7]} {most_sum[1][8]}''')
