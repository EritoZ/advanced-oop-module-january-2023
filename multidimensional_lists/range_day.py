size = 5
matrix = []
my_location = [0, 0]
targets = 0
shot = []

for i in range(size):
    row = input().split()

    targets += row.count('x')

    if 'A' in row:
        my_location[0] = i
        my_location[1] = row.index('A')

    matrix.append(row)

n_commands = int(input())
action_dict = {
    'move left': lambda row, index, step: [row, index - step] if index - step in range(size)
                                                                 and matrix[row][index - step] == '.' else [row, index],

    'move right': lambda row, index, step: [row, index + step] if index + step in range(size)
                                                                 and matrix[row][index + step] == '.' else [row, index],

    'move up': lambda row, index, step: [row - step, index] if row - step in range(size)
                                                                 and matrix[row - step][index] == '.' else [row, index],

    'move down': lambda row, index, step: [row + step, index] if row + step in range(size)
                                                                 and matrix[row + step][index] == '.' else [row, index],

    'shoot left': lambda row, index: [(matrix[row][i], row, i) for i in range(index - 1, -1, -1)],

    'shoot right': lambda row, index: [(matrix[row][i], row, i) for i in range(index + 1, size)],

    'shoot up': lambda row, index: [(matrix[i][index], i, index) for i in range(row - 1, -1, -1)],

    'shoot down': lambda row, index: [(matrix[i][index], i, index) for i in range(row + 1, size)]
}
targets_copy = targets

for command in range(n_commands):
    current_command = input().split()
    action = current_command[0]

    if action == 'move':
        steps = int(current_command[2])

        my_location = action_dict[' '.join(current_command[:2])](my_location[0], my_location[1], steps)

    elif action == 'shoot':

        objects_direction = action_dict[' '.join(current_command[:2])](my_location[0], my_location[1])

        if 'x' in [el[0] for el in objects_direction]:

            target = sorted(objects_direction, key=lambda x: x[0], reverse=True)[0]

            targets -= 1
            matrix[target[1]][target[2]] = '.'

            shot.append([target[1], target[2]])

    if not targets:
        break

if not targets:
    print(f"Training completed! All {targets_copy} targets hit.")

else:
    print(f"Training not completed! {targets} targets left.")

print('\n'.join(map(str, shot)))
