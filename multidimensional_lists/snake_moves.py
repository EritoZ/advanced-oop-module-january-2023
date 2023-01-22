rows, columns = tuple(map(int, input().split(' ')))
snek = input()

for row in range(rows):

    current_snek = snek[:columns]

    if columns > len(snek):
        current_snek += snek[:columns - len(snek)]

    print(current_snek if row % 2 == 0 else current_snek[::-1])

    snek = snek[columns - len(snek):] + current_snek
