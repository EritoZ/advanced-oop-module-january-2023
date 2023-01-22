size = int(input())
commands = input().split()
matrix = []
miner_position = [0, 0]
game_over = False
commands_dict = {
    'left': lambda row, index: [row, index - 1] if index - 1 in range(size) else [row, index],
    'right': lambda row, index: [row, index + 1] if index + 1 in range(size) else [row, index],
    'up': lambda row, index: [row - 1, index] if row - 1 in range(size) else [row, index],
    'down': lambda row, index: [row + 1, index] if row + 1 in range(size) else [row, index]
}
coal_count = 0

for i in range(size):
    row = input().split()

    matrix.append(row)
    coal_count += row.count('c')

    if 's' in row:
        miner_position[0] = i
        miner_position[1] = row.index('s')

for command in commands:

    miner_position = commands_dict[command](miner_position[0], miner_position[1])

    if matrix[miner_position[0]][miner_position[1]] == 'c':
        matrix[miner_position[0]][miner_position[1]] = '*'
        coal_count -= 1

        if coal_count == 0:
            break

    elif matrix[miner_position[0]][miner_position[1]] == 'e':
        game_over = True
        break


if not coal_count:
    print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")

elif game_over:
    print(f"Game over! ({miner_position[0]}, {miner_position[1]})")

else:
    print(f"{coal_count} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
