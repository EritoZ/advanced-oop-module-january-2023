from collections import deque

pumps_amount = int(input())
all_pumps_map = deque([input().split() for pump_index in range(pumps_amount)])
found_route = False

for starting_pump_index in range(len(all_pumps_map)):
    fuel = 0
    check_finish = False
    all_pumps_road = all_pumps_map.copy()

    while not found_route:
        refill = int(all_pumps_road[starting_pump_index][0])
        distance_next_pump = int(all_pumps_road[starting_pump_index][1])

        fuel += refill

        if check_finish and all_pumps_map[starting_pump_index] == all_pumps_road[starting_pump_index]:
            index_finish = starting_pump_index
            found_route = True
        elif distance_next_pump <= fuel:
            fuel -= distance_next_pump
            all_pumps_road.append(all_pumps_road.popleft())
            check_finish = True
        else:
            break

    if found_route:
        break

print(index_finish)
