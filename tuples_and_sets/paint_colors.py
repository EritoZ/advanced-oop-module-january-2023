import math
from collections import deque

main_colours = ("red", "yellow", "blue")
secondary_colours = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'},
}
substrings = deque(input().split())
colours = []
order = 0
found_secondary_colours = []

while substrings:

    formed_string_v1 = substrings[0] + substrings[-1] if len(substrings) > 1 else substrings[0]
    formed_string_v2 = substrings[-1] + substrings[0]

    if formed_string_v1 in main_colours or formed_string_v2 in main_colours:

        if formed_string_v1 in main_colours:
            colours.append(substrings.popleft() + substrings.pop()) if len(substrings) > 1 \
                else colours.append(substrings.popleft())

        else:
            colours.append(substrings.pop() + substrings.popleft())

        order += 1

    elif formed_string_v1 in secondary_colours or formed_string_v2 in secondary_colours:

        if formed_string_v1 in secondary_colours:

            found_secondary_colours.append((formed_string_v1, order))

        else:
            found_secondary_colours.append((formed_string_v2, order))

        substrings.popleft()

        if len(substrings) >= 1:
            substrings.pop()

        order += 1

    else:
        substrings[0], substrings[-1] = substrings[0][:len(substrings[0]) - 1], substrings[-1][:len(substrings[-1]) - 1]

        middle_index = math.ceil((len(substrings) - 1) / 2)

        substrings.insert(middle_index - 1, substrings.popleft()) if substrings[0] else substrings.popleft()

        if substrings:
            substrings.insert(middle_index if len(substrings) % 2 == 0 else middle_index - 1, substrings.pop()) \
                if substrings[-1] else substrings.pop()

[colours.insert(index, colour) for colour, index in found_secondary_colours
 if secondary_colours[colour].issubset(set(colours))]

print(colours)
