def flights(*args):
    flights_data = args[:args.index('Finish')]
    flights_dict = {}

    for i in range(0, len(flights_data), 2):

        destination, passengers = flights_data[i], flights_data[i + 1]

        if destination not in flights_dict:
            flights_dict[destination] = 0

        flights_dict[destination] += int(passengers)

    return flights_dict


print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))