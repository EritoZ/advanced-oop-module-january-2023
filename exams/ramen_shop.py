from collections import deque

bowls_ramen = list(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while customers and bowls_ramen:

    current_bowl = bowls_ramen.pop()
    current_customer = customers.popleft()

    if current_bowl > current_customer:
        bowls_ramen.append(current_bowl - current_customer)

    elif current_bowl < current_customer:
        customers.appendleft(current_customer - current_bowl)

if not customers:
    print("Great job! You served all the customers.")

    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_ramen))}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")

    print(f"Customers left: {', '.join(map(str, customers))}")
