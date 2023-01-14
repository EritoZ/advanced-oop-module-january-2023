n_commands = int(input())
cars = set()

for _ in range(n_commands):
    command, car_number = input().split(', ')

    if command == 'IN':
        cars.add(car_number)

    elif command == 'OUT':
        cars.remove(car_number)

if cars:
    print('\n'.join(cars))
else:
    print("Parking Lot is Empty")
