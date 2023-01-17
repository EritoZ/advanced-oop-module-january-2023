from collections import deque

materials_for_toys = list(map(int, input().split()))
materials_magic_levels = deque(map(int, input().split()))
present_recipes = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
crafted_stuff = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}

while materials_for_toys and materials_magic_levels:

    if not materials_for_toys[-1] or not materials_magic_levels[0]:

        if not materials_for_toys[-1]:
            materials_for_toys.pop()

        if not materials_magic_levels[0]:
            materials_magic_levels.popleft()

        continue

    crafting_result = materials_for_toys[-1] * materials_magic_levels[0]

    if crafting_result in present_recipes:
        crafted_stuff[present_recipes[crafting_result]] += 1
        materials_for_toys.pop()
        materials_magic_levels.popleft()

    elif crafting_result < 0:
        materials_for_toys.append(materials_for_toys.pop() + materials_magic_levels.popleft())

    else:
        materials_for_toys[-1] += 15
        materials_magic_levels.popleft()

if (crafted_stuff['Doll'] and crafted_stuff['Wooden train']) \
        or (crafted_stuff['Teddy bear'] and crafted_stuff['Bicycle']):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_for_toys:
    print(f"Materials left: {', '.join(map(str, materials_for_toys[::-1]))}")

if materials_magic_levels:
    print(f"Magic left: {', '.join(map(str, materials_magic_levels))}")

for present, quantity in sorted(crafted_stuff.items()):
    if quantity:
        print(f'{present}: {quantity}')
