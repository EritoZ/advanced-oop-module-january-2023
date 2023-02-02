size = 6
mars = []

commands_dict = {
    'left': lambda row, index: [row, index - 1] if index - 1 in range(size) else [row, size - 1],
    'right': lambda row, index: [row, index + 1] if index + 1 in range(size) else [row, 0],
    'up': lambda row, index: [row - 1, index] if row - 1 in range(size) else [size - 1, index],
    'down': lambda row, index: [row + 1, index] if row + 1 in range(size) else [0, index]
}

deposits_dict = {'W': ['Water', 0], 'M': ['Metal', 0], 'C': ['Concrete', 0]}

for i in range(size):
    current_row = input().split()

    if 'E' in current_row:
        rover_loc = [i, current_row.index('E')]

    mars.append(current_row)

commands = input().split(', ')

for command in commands:

    # noinspection PyUnboundLocalVariable
    rover_loc = commands_dict[command](*rover_loc)
    current_object = mars[rover_loc[0]][rover_loc[1]]

    if current_object in ('W', 'M', 'C'):
        print(f"{deposits_dict[current_object][0]} deposit found at ({rover_loc[0]}, {rover_loc[1]})")

        deposits_dict[current_object][1] += 1

    elif current_object == 'R':
        print(f"Rover got broken at ({rover_loc[0]}, {rover_loc[1]})")
        break

if deposits_dict['W'][1] and deposits_dict['M'][1] and deposits_dict['C'][1]:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
