rows, columns = tuple(map(int, input().split(', ')))
matrix = [tuple(map(int, input().split(', '))) for row in range(rows)]
most_sum = [0, []]

for i_row in range(rows):
    for i_column in range(columns):

        if i_row == rows - 1 or i_column == columns - 1:
            continue

        if sum([
            matrix[i_row][i_column], matrix[i_row][i_column + 1],
            matrix[i_row + 1][i_column], matrix[i_row + 1][i_column + 1]
        ]) > most_sum[0]:

            most_sum[0] = sum([
                matrix[i_row][i_column], matrix[i_row][i_column + 1],
                matrix[i_row + 1][i_column], matrix[i_row + 1][i_column + 1]
            ])

            most_sum[1] = [
                matrix[i_row][i_column], matrix[i_row][i_column + 1],
                matrix[i_row + 1][i_column], matrix[i_row + 1][i_column + 1]
            ]

if most_sum[1]:
    print(f'''{most_sum[1][0]} {most_sum[1][1]}
{most_sum[1][2]} {most_sum[1][3]}
{most_sum[0]}''')
