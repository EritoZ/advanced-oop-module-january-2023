size = int(input())
matrix = [list(input()) for row in range(size)]
to_be_removed = 0
knight_moves = (
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
    (-2, 1)
)

while True:

    no_moves_left = True
    knights_removes = []

    for current_row in range(size):
        for index in range(size):

            if matrix[current_row][index] == 'K':
                removed_knights = 0

                for row_movement, col_movement in knight_moves:

                    if (current_row + row_movement in range(size)
                            and index + col_movement in range(size)
                            and matrix[current_row + row_movement][index + col_movement] == 'K'
                    ):
                        removed_knights += 1

                if removed_knights:
                    no_moves_left = False
                    knights_removes.append((current_row, index, removed_knights))

    if no_moves_left:
        break

    removed_knight = max(knights_removes, key=lambda x: x[-1])

    to_be_removed += 1
    matrix[removed_knight[0]][removed_knight[1]] = '0'

print(to_be_removed)
