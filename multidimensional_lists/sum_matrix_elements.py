rows = list(map(int, input().split(', ')))[0]
matrix = []
total_sum = 0

for row in range(rows):
    matrix.append(list(map(int, input().split(', '))))
    total_sum += sum(matrix[row])

print(total_sum)
print(matrix)
