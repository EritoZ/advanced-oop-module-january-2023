from collections import deque

food_for_the_day = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:

    if orders[0] <= food_for_the_day:
        food_for_the_day -= orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    print(f'Orders left: {" ".join(map(str, orders))}')
