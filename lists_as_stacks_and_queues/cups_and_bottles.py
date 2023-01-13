from collections import deque

cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))
wasted = 0

while cups and bottles:

    cups[0] -= bottles.pop()

    if cups[0] <= 0:
        wasted += abs(cups[0])
        cups.popleft()

if cups:
    print(f"Cups: {' '.join(map(str, cups))}")

elif bottles:
    print(f"Bottles: {' '.join(map(str, bottles))}")

print(f"Wasted litters of water: {wasted}")
