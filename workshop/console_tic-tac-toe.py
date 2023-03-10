from collections import deque


class BusyFieldError(Exception):
    pass


def choose_side(player):
    while True:
        try:
            side = input(f"{player} would you like to play with 'X' or 'O'? ").capitalize()

            if side not in ('X', 'O'):
                raise ValueError

            other_side = 'O' if side != 'O' else 'X'

        except ValueError:
            print("Side must be 'X' or 'O'.")

        else:
            break

    return side, other_side


def victory_logic(board_size, the_board, chosen_field, player_side):
    row_i, col_i = chosen_field

    horizontal = [the_board[row_i][i] for i in range(board_size)]

    vertical = [the_board[i][col_i] for i in range(board_size)]

    first_diagonal = [the_board[i][i] for i in range(board_size)]

    second_diagonal = [the_board[i][2 - i] for i in range(board_size)]

    return 3 * [player_side] in (
        horizontal, vertical,
        second_diagonal, first_diagonal
    )


player_one = input('Player one name: ')
player_two = input('Player two name: ')
sides = choose_side(player_one)
players = deque([[player_one, sides[0], 0], [player_two, sides[1], 0]])
winner = ''

board = [[' '] * 3 for _ in range(3)]
fields = 9

print(f'''This is the numeration of the board:
|  1  |  2  |  3  |
|  4  |  5  |  6  |
|  7  |  8  |  9  |
{player_one} starts first!''')

while fields and not winner:

    try:
        current_player, side, moves = players[0]

        chosen_index = int(input(f'{current_player}, please choose a free position [1-9]: ')) - 1
        row, col = chosen_index // 3, chosen_index % 3
        field_choice = board[row][col]

        if chosen_index < 0:
            raise IndexError

        elif field_choice in ('X', 'O'):
            raise BusyFieldError

        players[0][2] += 1
        fields -= 1
        board[row][col] = side

        if players[0][2] >= 3 and victory_logic(3, board, [row, col], side):
            winner = current_player

        [print('|  ' + '  |  '.join(row) + '  |') for row in board]

        players.rotate(-1)

    except (IndexError, ValueError):
        print('Field choice must be a number from 1 to 9.')

    except BusyFieldError:
        print('The chosen position is already used.')

if winner:
    print(f'{winner} won!')
else:
    print('Draw!')
