size = 6
matrix = [input().split() for _ in range(size)]

current_position = list(map(int, input().lstrip('(').rstrip(')').split(', ')))

commands_dict = {
    'left': lambda row, index: [row, index - 1] if index - 1 in range(size) else [row, index],
    'right': lambda row, index: [row, index + 1] if index + 1 in range(size) else [row, index],
    'up': lambda row, index: [row - 1, index] if row - 1 in range(size) else [row, index],
    'down': lambda row, index: [row + 1, index] if row + 1 in range(size) else [row, index]
}

command = input()
while command != 'Stop':
    command = command.split(', ')

    current_command = command[0]
    direction = command[1]

    current_position = commands_dict[direction](current_position[0], current_position[1])
    current_string = matrix[current_position[0]][current_position[1]]

    if current_command == 'Create':
        value = command[2]

        if current_string == '.':
            matrix[current_position[0]][current_position[1]] = value

    elif current_command == 'Update':
        value = command[2]

        if current_string.isalnum():
            matrix[current_position[0]][current_position[1]] = value

    elif current_command == 'Delete':

        if current_string.isalnum():
            matrix[current_position[0]][current_position[1]] = '.'

    elif current_command == 'Read':

        if current_string.isalnum():
            print(matrix[current_position[0]][current_position[1]])

    command = input()

[print(' '.join(row)) for row in matrix]
