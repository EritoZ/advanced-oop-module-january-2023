from collections import deque

pizza_orders = deque(map(int, input().split(', ')))
employees = list(map(int, input().split(', ')))
total_pizzas_made = 0

while pizza_orders and employees:

    current_order = pizza_orders.popleft()

    if current_order in range(1, 11):
        current_employee_skill = employees.pop()

        if current_order > current_employee_skill:
            pizza_orders.appendleft(current_order - current_employee_skill)
            current_order = current_employee_skill

        total_pizzas_made += current_order

if not pizza_orders:
    print(f'''All orders are successfully completed!
Total pizzas made: {total_pizzas_made}
Employees: {', '.join(map(str, employees))}''')

else:
    print(f'''Not all orders are completed.
Orders left: {", ".join(map(str, pizza_orders))}''')