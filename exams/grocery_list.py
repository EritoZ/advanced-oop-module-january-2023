def shop_from_grocery_list(*args):
    budget = int(args[0])
    grocery_list: list = args[1]
    products_prices = args[2:]

    for product_name, price in products_prices:

        if product_name in grocery_list:
            if price <= budget:
                budget -= price
                grocery_list.remove(product_name)
            else:
                break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))