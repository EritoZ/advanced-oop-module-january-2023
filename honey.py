from collections import deque

bees = deque(map(int, input().split()))
nektar = list(map(int, input().split()))
arithmetic_symbols = deque(input().split())
arithmetic_algorithms = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y
}
honey = 0

while bees and nektar:

    collected_honey = []
    bee_value = bees[0]

    for index in range(len(nektar) - 1, -1, -1):

        if nektar[index] >= bees[0]:
            collected_honey.append(nektar[index])
            break
        else:
            nektar.pop()

    if collected_honey:
        if collected_honey[0]:
            honey += abs(arithmetic_algorithms[arithmetic_symbols.popleft()](bee_value, collected_honey[0]))

        bees.popleft()
        nektar.pop()
        collected_honey.clear()


print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

elif nektar:
    print(f"Nectar left: {', '.join(map(str, nektar))}")
