from collections import deque

eggs = deque(map(int, input().split(', ')))
paper = list(map(int, input().split(', ')))
box_size = 50
boxes = 0

while eggs and paper:

    current_egg = eggs.popleft()

    if current_egg == 13:

        paper[0], paper[-1] = paper[-1], paper[0]

        continue

    if current_egg > 0 and current_egg + paper.pop() <= box_size:

        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')

if paper:
    print(f'Pieces of paper left: {", ".join(map(str, paper))}')
