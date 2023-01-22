rows, columns = tuple(map(int, input().split(' ')))

for row in range(rows):
    for letter in range(columns):
        print(f'{chr(97 + row)}{chr(97 + row + letter)}{chr(97 + row)}', end=' ')

    print()
