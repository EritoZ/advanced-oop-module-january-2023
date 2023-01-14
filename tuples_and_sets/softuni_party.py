def collect_guests():
    guests = set()

    command = input()
    while command != 'END':
        guest = command

        guests.add(guest)

        command = input()

    return guests


n_reservations = int(input())
reserved_guests = {input() for guest in range(n_reservations)}
arrived_guests = collect_guests()

unarrived_guests = sorted(reserved_guests.difference(arrived_guests))

print(len(unarrived_guests))
print('\n'.join(unarrived_guests))
