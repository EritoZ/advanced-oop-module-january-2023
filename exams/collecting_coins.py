size = int(input())
field = []
player_loc = []
path = []
coins_collected = 0

commands_dict = {
    'left': lambda row, index: [row, (index - 1) % size],
    'right': lambda row, index: [row, (index + 1) % size],
    'up': lambda row, index: [(row - 1) % size, index],
    'down': lambda row, index: [(row + 1) % size, index]
}

for i in range(size):
    current_row = input().split()

    if 'P' in current_row:
        player_loc = [i, current_row.index('P')]
        path.append(player_loc)

    field.append(current_row)

while coins_collected < 100:

    command = input()

    if command in commands_dict:

        player_loc = commands_dict[command](*player_loc)
        path.append(player_loc)

        current_object = field[player_loc[0]][player_loc[1]]

        if current_object.isdigit():
            coins_collected += int(current_object)
            field[player_loc[0]][player_loc[1]] = '.'

        elif current_object == 'X':
            coins_collected = int(coins_collected * 0.5)
            break

if coins_collected >= 100:
    print(f"You won! You've collected {coins_collected} coins.")
else:
    print(f"Game over! You've collected {coins_collected} coins.")

print('Your path:')
print('\n'.join(map(str, path)))
