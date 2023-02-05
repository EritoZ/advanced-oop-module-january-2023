from collections import deque

materials_presents = list(map(int, input().split()))
genie_magic_levels = deque(map(int, input().split()))
second_try = False

magic_needed_gifts = {
    range(100, 200): ['Gemstone', 0],
    range(200, 300): ['Porcelain Sculpture', 0],
    range(300, 400): ['Gold', 0],
    range(400, 500): ['Diamond Jewellery', 0]
}

while materials_presents and genie_magic_levels:

    material = materials_presents[-1]
    magic_level = genie_magic_levels[0]
    product = material + magic_level

    for magic_range in magic_needed_gifts:

        if product in magic_range:
            magic_needed_gifts[magic_range][1] += 1
            second_try = False
            break

    else:
        if second_try:
            second_try = False
        else:
            if product < 100:
                materials_presents[-1] *= 2

                if product % 2 == 0:
                    genie_magic_levels[0] *= 3
                else:
                    genie_magic_levels[0] *= 2
            else:
                materials_presents[-1] //= 2
                genie_magic_levels[0] //= 2

            second_try = True

            continue

    materials_presents.pop()
    genie_magic_levels.popleft()

gifts = tuple(magic_needed_gifts.values())

if (gifts[0][1] and gifts[1][1]) or (gifts[2][1] and gifts[3][1]):
    print('The wedding presents are made!')
else:
    print("Aladdin does not have enough wedding presents.")

if materials_presents:
    print(f"Materials left: {', '.join(map(str, materials_presents))}")

if genie_magic_levels:
    print(f'Magic left: {", ".join(map(str, genie_magic_levels))}')

[print(f'{name}: {quantity}') for name, quantity in sorted(magic_needed_gifts.values()) if quantity]
