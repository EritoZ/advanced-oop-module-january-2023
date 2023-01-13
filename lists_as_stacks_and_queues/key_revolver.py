from collections import deque

bullet_price = int(input())
barrel_capacity = int(input())
bullets_holding = barrel_capacity
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
intelligence_value = int(input())
opened = False

while bullets:
    bullet_value = bullets.pop()
    bullets_holding -= 1

    if bullet_price <= intelligence_value:
        intelligence_value -= bullet_price
    else:
        break

    if bullet_value <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if bullets and bullets_holding == 0:
        print('Reloading!')
        bullets_holding += barrel_capacity

    if not locks:
        opened = True
        print(f"{len(bullets)} bullets left. Earned ${intelligence_value}" )
        break

if not opened:
    print(f"Couldn't get through. Locks left: {len(locks)}")
