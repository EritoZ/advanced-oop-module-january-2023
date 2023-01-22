rows, columns = tuple(map(int, input().split(', ')))
matrix = [tuple(map(int, input().split())) for row in range(rows)]

for i in range(columns):
    total_sum = 0
    for ind in range(rows):
        total_sum += matrix[ind][i]

    print(total_sum)
