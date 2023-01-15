from collections import deque

chocolates = list(map(int, input().split(', ')))
cups_milk = deque(map(int, input().split(', ')))
milkshakes = 0

while milkshakes < 5 and chocolates and cups_milk:
    if chocolates[-1] > 0 and cups_milk[0] > 0:

        if chocolates[-1] == cups_milk[0]:
            chocolates.pop()
            cups_milk.popleft()
            milkshakes += 1

        else:
            cups_milk.append(cups_milk.popleft())
            chocolates[-1] -= 5

    else:
        if chocolates[-1] < 1:
            chocolates.pop()

        if cups_milk[0] < 1:
            cups_milk.popleft()

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join(map(str, cups_milk))}")
else:
    print("Milk: empty")
