def shopping_cart(*args):
    kitchen = {'Soup': [], 'Pizza': [], 'Dessert': []}
    product_limits = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    meals = args

    for data in meals:

        if data == 'Stop':
            break

        meal, product_for_meal = data

        product_for_meal = f' - {product_for_meal}'

        if len(kitchen[meal]) < product_limits[meal] and product_for_meal not in kitchen[meal]:
            kitchen[meal].append(product_for_meal)

    sorted_kitchen = sorted(kitchen.items(), key=lambda x: (-len(x[1]), x[0]))

    sorted_kitchen = [f'{recipe[0]}:\n' + '\n'.join(sorted(recipe[1])) if recipe[1] else f'{recipe[0]}:'
                      for recipe in sorted_kitchen]

    if kitchen['Soup'] or kitchen['Dessert'] or kitchen['Pizza']:
        return '\n'.join(sorted_kitchen)
    else:
        return "No products in the cart!"


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))