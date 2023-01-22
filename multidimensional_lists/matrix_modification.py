rows = int(input())
matrix = [list(map(int, input().split())) for row in range(rows)]

command = input()
while command != 'END':
    command = command.split()

    current_command = command[0]
    row, col, value = tuple(map(int, command[1:]))

    if current_command == 'Add' and row in range(rows) and col in range(len(matrix[0])):

        matrix[row][col] += value

    elif current_command == 'Subtract' and row in range(rows) and col in range(len(matrix[0])):

        matrix[row][col] -= value

    else:
        print("Invalid coordinates")

    command = input()

for row in matrix:
    print(' '.join(map(str, row)))
