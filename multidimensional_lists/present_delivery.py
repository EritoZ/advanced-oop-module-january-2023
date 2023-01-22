presents = int(input())
size = int(input())
neighborhood = []
santa_loc = [0, 0]
nice_kids = 0

directions = {
    'left': lambda current_row, col: [current_row, col - 1] if col - 1 in range(size) else [current_row, col],
    'right': lambda current_row, col: [current_row, col + 1] if col + 1 in range(size) else [current_row, col],
    'up': lambda current_row, col: [current_row - 1, col] if current_row - 1 in range(size) else [current_row, col],
    'down': lambda current_row, col: [current_row + 1, col] if current_row + 1 in range(size) else [current_row, col]
}

for i in range(size):
    row = input().split()

    nice_kids += row.count('V')

    if 'S' in row:
        santa_loc[0] = i
        santa_loc[1] = row.index('S')
        row[row.index('S')] = '-'

    neighborhood.append(row)

nice_kids_count = nice_kids

command = input()
while command != 'Christmas morning':

    santa_loc = directions[command](santa_loc[0], santa_loc[1])

    if neighborhood[santa_loc[0]][santa_loc[1]] == 'V':
        presents -= 1
        nice_kids -= 1

    elif neighborhood[santa_loc[0]][santa_loc[1]] == 'C':

        for direction in directions:

            location = directions[direction](santa_loc[0], santa_loc[1])

            if neighborhood[location[0]][location[1]] in ('V', 'X'):
                if neighborhood[location[0]][location[1]] == 'V':
                    nice_kids -= 1

                presents -= 1
                neighborhood[location[0]][location[1]] = '-'

                if not presents:
                    break

    neighborhood[santa_loc[0]][santa_loc[1]] = '-'

    if not presents:
        break

    command = input()

neighborhood[santa_loc[0]][santa_loc[1]] = 'S'

if not presents and nice_kids:
    print("Santa ran out of presents!")

[print(' '.join(row)) for row in neighborhood]

if not nice_kids:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")

else:
    print(f"No presents for {nice_kids} nice kid/s.")
