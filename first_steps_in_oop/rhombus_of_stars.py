def rhombus_of_stars(size: int):

    for i in range(1, size + 1):
        row = ' ' * (size - i) + '* ' * i

        print(row)

    for i in range(size - 1, 0, -1):
        row = ' ' * (size - i) + '* ' * i

        print(row)


size = int(input())

rhombus_of_stars(size)
