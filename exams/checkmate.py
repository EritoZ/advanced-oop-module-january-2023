size = 8
chess_board = []
king_loc = []
safe = True
directions = (
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1)
)

for i in range(size):
    row = input().split()

    if 'K' in row:
        king_loc = [i, row.index('K')]

    chess_board.append(row)


for row_direction, col_direction in directions:
    current_loc = king_loc.copy()

    while True:
        current_loc[0] += row_direction
        current_loc[1] += col_direction

        if set(current_loc).issubset(range(8)):

            current_object = chess_board[current_loc[0]][current_loc[1]]

            if current_object == 'Q':
                print(current_loc)
                safe = False
                break
        else:
            break

if safe:
    print('The king is safe!')
