def grocery_store(**kwargs):
    grocery_list = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    grocery_list = [f'{ingredient}: {quantity}' for ingredient, quantity in grocery_list]

    return '\n'.join(grocery_list)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print()
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))