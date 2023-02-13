size = 6
mars = []

commands_dict = {
    'left': lambda row, index: [row, (index - 1) % size],
    'right': lambda row, index: [row, (index + 1) % size],
    'up': lambda row, index: [(row - 1) % size, index],
    'down': lambda row, index: [(row + 1) % size, index]
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

    if current_object in deposits_dict:
        print(f"{deposits_dict[current_object][0]} deposit found at ({rover_loc[0]}, {rover_loc[1]})")

        deposits_dict[current_object][1] += 1

    elif current_object == 'R':
        print(f"Rover got broken at ({rover_loc[0]}, {rover_loc[1]})")
        break

if deposits_dict['W'][1] and deposits_dict['M'][1] and deposits_dict['C'][1]:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
