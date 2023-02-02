from collections import deque

cat_and_mouse = deque(input().split(', '))
maze = [input().split() for _ in range(6)]
fallen = ''
resting = []

while not fallen:
    coordinates = input().split(', ')
    row, col = int(coordinates[0][1]), int(coordinates[1][0])

    if cat_and_mouse[0] in resting:
        resting.remove(cat_and_mouse[0])

    elif maze[row][col] == 'W':
        print(f"{cat_and_mouse[0]} hits a wall and needs to rest.")

        resting.append(cat_and_mouse[0])

    elif maze[row][col] == 'E':
        break

    elif maze[row][col] == 'T':
        fallen = cat_and_mouse.popleft()

    cat_and_mouse.rotate()

if not fallen:
    print(f"{cat_and_mouse[0]} found the Exit and wins the game!")
else:
    print(f"{fallen} is out of the game! The winner is {cat_and_mouse[0]}.")
