def stock_availability(inventory: list, delivery_or_sell, *args):
    strings_or_nums = list(args)

    if delivery_or_sell == 'delivery':
        [inventory.append(item) for item in strings_or_nums]

    else:
        if not strings_or_nums:
            inventory.pop(0)

        elif type(strings_or_nums[0]) == int:
            sold = strings_or_nums[0]
            inventory = inventory[sold:]

        else:
            [inventory.remove(order) for order in strings_or_nums if order in inventory
             for _ in range(inventory.count(order))]

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
