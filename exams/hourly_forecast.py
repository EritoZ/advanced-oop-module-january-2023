def forecast(*args):
    locations_dict = {}
    locations = args

    for location, weather in locations:

        if weather not in locations_dict:
            locations_dict[weather] = []

        locations_dict[weather].append(location)

    locations_dict = sorted(locations_dict.items(), key=lambda x: (x[0] == 'Rainy', x[0] == 'Cloudy', x[0] == 'Sunny'))

    message = [f"{loc} - {weather}" for weather, locs in locations_dict for loc in sorted(locs)]

    return '\n'.join(message)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))