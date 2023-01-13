from collections import deque

queue = deque()

command = input()
while command != 'End':

    if command == 'Paid':
        print('\n'.join(queue))
        queue = deque()
    else:
        queue.append(command)

    command = input()

print(f"{len(queue)} people remaining.")
