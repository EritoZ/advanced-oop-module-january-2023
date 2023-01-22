rows = int(input())
matrix = [input() for row in range(rows)]
target = input()

for row in range(len(matrix)):
    if target in matrix[row]:
        print(f"({row}, {matrix[row].index(target)})")
        break

else:
    print(f'{target} does not occur in the matrix')
