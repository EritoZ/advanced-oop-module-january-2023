size = int(input())
bombs_n = int(input())
matrix = [size * [0] for _ in range(size)]
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

for _ in range(bombs_n):
    coordinates = input().lstrip('(').rstrip(')').split(', ')
    r, c = int(coordinates[0]), int(coordinates[1])

    if {r, c}.issubset(range(size)):
        matrix[r][c] = '*'

for row_i, row in enumerate(matrix):
    for col_i, current_object in enumerate(row):
        if not current_object:
            bombs = [matrix[row_i + row_dir][col_i + col_dir]
                     for row_dir, col_dir in directions if {row_i + row_dir, col_i + col_dir}.issubset(range(size))
                     and matrix[row_i + row_dir][col_i + col_dir] == '*']

            matrix[row_i][col_i] += len(bombs)

    print(' '.join(map(str, row)))
