size = int(input())
matrix = []
alice_position = [0, 0, '']
tea = 0
directions_dict = {
    'right': lambda current_row, col: [current_row, col + 1, ''] if col + 1 in range(size)
                                                                 else [current_row, col, 'lost'],
    'left': lambda current_row, col: [current_row, col - 1, ''] if col - 1 in range(size)
                                                                else [current_row, col, 'lost'],
    'up': lambda current_row, col: [current_row - 1, col, ''] if current_row - 1 in range(size)
                                                              else [current_row, col, 'lost'],
    'down': lambda current_row, col: [current_row + 1, col, ''] if current_row + 1 in range(size)
                                                                else [current_row, col, 'lost']
}

for i in range(size):
    row = input().split()

    if 'A' in row:
        alice_position[0] = i
        alice_position[1] = row.index('A')
        row[row.index('A')] = '*'

    matrix.append(row)

while tea < 10:
    direction = input()

    alice_position = directions_dict[direction](alice_position[0], alice_position[1])

    object = matrix[alice_position[0]][alice_position[1]]
    matrix[alice_position[0]][alice_position[1]] = '*'

    if object[-1].isdigit():
        tea += int(object)

    elif object == 'R' or alice_position[-1]:
        alice_position[-1] = 'lost'
        break

if alice_position[-1]:
    print("Alice didn't make it to the tea party.")

else:
    print('She did it! She went to the party.')

[print(' '.join(row)) for row in matrix]
