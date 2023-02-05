from sys import maxsize

board = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(6)]
throws = 3
scored_points = 0

prizes = {
    'Football': range(100, 200),
    'Teddy Bear': range(200, 300),
    'Lego Construction Set': range(300, maxsize)
}

while throws:
    coordinates = input().lstrip('(').rstrip(')').split(', ')
    row, col = int(coordinates[0]), int(coordinates[1])

    if row in range(6) and col in range(6) and board[row][col] == 'B':
        points = [board[i][col] for i in range(6) if type(board[i][col]) == int]
        scored_points += sum(points)
        board[row][col] = 0

    throws -= 1

for prize in prizes:

    if scored_points in prizes[prize]:
        print(f"Good job! You scored {scored_points} points, and you've won {prize}.")
        break
else:
    print(f"Sorry! You need {100 - scored_points} points more to win a prize.")
