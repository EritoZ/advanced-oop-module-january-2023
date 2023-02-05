from collections import deque


def shopping_list(budget, **kwargs):

    shopping_lst = deque(kwargs.items())
    counter = 0
    message = ''

    if budget >= 100:

        while shopping_lst and counter != 5:
            current_product = shopping_lst.popleft()
            product, price, quantity = current_product[0], current_product[1][0], current_product[1][1]
            total_price = price * quantity

            if total_price <= budget:
                budget -= total_price
                message += f"You bought {product} for {total_price:.2f} leva.\n"
                counter += 1

        return message

    else:
        return "You do not have enough budget."


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))