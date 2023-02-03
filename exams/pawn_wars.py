from collections import deque

size = 8
chess_board = []
pawn_turns = []
finished = False

pawn_moves = {
    'w': {
        'top_left': lambda x, y: [x - 1, y - 1] if {x - 1, y - 1}.issubset(range(size)) else [x, y],
        'top_right': lambda x, y: [x - 1, y + 1] if {x - 1, y + 1}.issubset(range(size)) else [x, y]
    },
    'b': {
        'bottom_left': lambda x, y: [x + 1, y - 1] if {x + 1, y - 1}.issubset(range(size)) else [x, y],
        'bottom_right': lambda x, y: [x + 1, y + 1] if {x + 1, y + 1}.issubset(range(size)) else [x, y]
    }
}

for i in range(size):
    row = input().split()

    if 'w' in row:
        pawn_turns.append(['w', i, row.index('w')])

    elif 'b' in row:
        pawn_turns.append(['b', i, row.index('b')])

    chess_board.append(row)

pawn_turns = deque(sorted(pawn_turns, reverse=True))

while not finished:

    current_pawn = pawn_turns[0]

    chess_board[current_pawn[1]][current_pawn[2]] = '-'

    if current_pawn[0] == 'w':

        if current_pawn[1] == 0:
            print(f"Game over! White pawn is promoted to a queen at "
                  f"{f'{chr(97 + current_pawn[2])}8'}.")

            break

        for move in pawn_moves['w']:

            w_turn_current_object_loc = pawn_moves['w'][move](*current_pawn[1:])

            w_turn_current_object = chess_board[w_turn_current_object_loc[0]][w_turn_current_object_loc[1]]

            if w_turn_current_object == 'b':
                print(f"Game over! White win, capture on "
                      f"{f'{chr(97 + w_turn_current_object_loc[1])}{8 - w_turn_current_object_loc[0]}'}.")

                finished = True
                break

        pawn_turns[0][1] -= 1

        chess_board[pawn_turns[0][1]][pawn_turns[0][2]] = 'w'

    elif current_pawn[0] == 'b':

        if current_pawn[1] == 7:
            print(f"Game over! Black pawn is promoted to a queen at "
                  f"{f'{chr(97 + current_pawn[2])}1'}.")

            break

        for move in pawn_moves['b']:

            b_turn_current_object_loc = pawn_moves['b'][move](*current_pawn[1:])

            b_turn_current_object = chess_board[b_turn_current_object_loc[0]][b_turn_current_object_loc[1]]

            if b_turn_current_object == 'w':
                print(f"Game over! Black win, capture on "
                      f"{f'{chr(97 + b_turn_current_object_loc[1])}{8 - b_turn_current_object_loc[0]}'}.")

                finished = True
                break

        pawn_turns[0][1] += 1

        chess_board[pawn_turns[0][1]][pawn_turns[0][2]] = 'b'

    pawn_turns.rotate()
