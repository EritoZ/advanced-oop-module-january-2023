rows = int(input())
flat_matrix = []

[flat_matrix.append(int(el)) for row in range(rows) for el in input().split(', ')]

print(flat_matrix)
