rows, columns = tuple(map(int, input().split(' ')))
matrix = [input().split() for row in range(rows)]

command = input()
while command != 'END':
    command = command.split()
    current_command = command[0]
    coordinates = [int(num) for num in command[1:] if num.isdigit()]

    if current_command == 'swap' and len(coordinates) == 4 \
            and {coordinates[0], coordinates[2]}.issubset(set(range(rows))) \
            and {coordinates[1], coordinates[3]}.issubset(set(range(columns))):

        (matrix[coordinates[0]][coordinates[1]],
         matrix[coordinates[2]][coordinates[3]]) = (matrix[coordinates[2]][coordinates[3]],
                                                    matrix[coordinates[0]][coordinates[1]])

        [print(' '.join(row)) for row in matrix]

    else:
        print('Invalid input!')

    command = input()
