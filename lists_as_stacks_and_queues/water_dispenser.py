from collections import deque


def get_people():
    people = deque()

    command = input()
    while command != 'Start':
        people.append(command)

        command = input()

    return people


quantity = int(input())
thirsty_dudes = get_people()

current_command = input()
while current_command != 'End':

    if 'refill' in current_command:
        refill_data = current_command.split()
        water = int(refill_data[1])

        quantity += water
    else:
        thirsty_dude = thirsty_dudes.popleft()
        water = int(current_command)

        if quantity >= water:
            quantity -= water
            print(f"{thirsty_dude} got water")
        else:
            print(f"{thirsty_dude} must wait")

    current_command = input()

print(f"{quantity} liters left")
