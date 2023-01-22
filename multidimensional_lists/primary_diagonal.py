size = int(input())
matrix = [tuple(map(int, input().split())) for row in range(size)]
total_sum = 0

for i in range(size):
    total_sum += matrix[i][i]

print(total_sum)
