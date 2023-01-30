from collections import deque

milligrams_of_caffeine = list(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))
caffeine = 0

while milligrams_of_caffeine and energy_drinks:

    drug_milligrams = milligrams_of_caffeine.pop()

    heart_attack_drink = energy_drinks.popleft()

    total_drug = drug_milligrams * heart_attack_drink

    if caffeine + total_drug > 300:
        energy_drinks.append(heart_attack_drink)

        if caffeine >= 30:
            caffeine -= 30
    else:
        caffeine += total_drug


if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks)) }")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine} mg caffeine.")
