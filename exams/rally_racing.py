size_rally = int(input())
tracked_car_num = input()
tracked_car_loc = [0, 0]
tunnel_info = []
rally = []
kilometers_passed = 0
finished = False

commands_dict = {
    'left': lambda row, index: [row, index - 1] if index - 1 in range(size_rally) else [row, index],
    'right': lambda row, index: [row, index + 1] if index + 1 in range(size_rally) else [row, index],
    'up': lambda row, index: [row - 1, index] if row - 1 in range(size_rally) else [row, index],
    'down': lambda row, index: [row + 1, index] if row + 1 in range(size_rally) else [row, index]
}

for i in range(size_rally):
    current_row = input().split()

    if 'T' in current_row:
        tunnel_info.append([i, current_row.index('T')])

        if current_row.count('T') > 1:
            tunnel_info.append([i, ''.join(current_row).rfind('T')])

    rally.append(current_row)


command = input()
while command != 'End':

    tracked_car_loc = commands_dict[command](tracked_car_loc[0], tracked_car_loc[1])

    kilometers_passed += 10

    if rally[tracked_car_loc[0]][tracked_car_loc[1]] == 'T':

        tracked_car_loc = tunnel_info[0] if tunnel_info[0] != tracked_car_loc else tunnel_info[1]

        rally[tunnel_info[0][0]][tunnel_info[0][1]] = '.'
        rally[tunnel_info[1][0]][tunnel_info[1][1]] = '.'

        kilometers_passed += 20

    elif rally[tracked_car_loc[0]][tracked_car_loc[1]] == 'F':
        finished = True
        break

    command = input()


rally[tracked_car_loc[0]][tracked_car_loc[1]] = 'C'

if finished:
    print(f"Racing car {tracked_car_num} finished the stage!")
else:
    print(f"Racing car {tracked_car_num} DNF.")

print(f"Distance covered {kilometers_passed} km.")

[print(''.join(row)) for row in rally]
