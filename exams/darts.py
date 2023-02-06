from collections import deque

first_player, second_player = input().split(', ')
player_turns = deque([[first_player, 501, 0], [second_player, 501, 0]])
dartboard = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(7)]

dartboard_dict = {
    'D': lambda x, y: (dartboard[0][y] + dartboard[x][0] + dartboard[6][y] + dartboard[x][6]) * 2,
    'T': lambda x, y: (dartboard[0][y] + dartboard[x][0] + dartboard[6][y] + dartboard[x][6]) * 3,
}

while True:

    coordinates = input().lstrip('(').rstrip(')').split(', ')
    row, col = int(coordinates[0]), int(coordinates[1])
    player_turns[0][2] += 1

    if {row, col}.issubset(range(7)):

        current_object = dartboard[row][col]

        if type(current_object) == int:
            player_turns[0][1] -= current_object

        elif current_object == 'B':
            break

        else:
            player_turns[0][1] -= dartboard_dict[current_object](row, col)

    if player_turns[0][1] < 1:
        break

    player_turns.rotate()

print(f"{player_turns[0][0]} won the game with {player_turns[0][2]} throws!")
