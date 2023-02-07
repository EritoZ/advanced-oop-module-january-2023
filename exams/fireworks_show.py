from collections import deque

firework_effects = deque([int(n) for n in input().split(', ') if int(n) > 0])
explosive_powers = [int(n) for n in input().split(', ') if int(n) > 0]
fireworks_made = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
success = False

while firework_effects and explosive_powers and not success:

    current_effect = firework_effects.popleft()
    current_power = explosive_powers.pop()
    sum_values = current_effect + current_power

    if sum_values % 3 == 0 and sum_values % 5 != 0:
        fireworks_made['Palm Fireworks'] += 1

    elif sum_values % 3 != 0 and sum_values % 5 == 0:
        fireworks_made['Willow Fireworks'] += 1

    elif sum_values % 3 == 0 and sum_values % 5 == 0:
        fireworks_made['Crossette Fireworks'] += 1

    else:
        if current_effect - 1 > 0:
            firework_effects.append(current_effect - 1)

        explosive_powers.append(current_power)

    success = not set(fireworks_made.values()).intersection(range(3))

if success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if explosive_powers:
    print(f"Explosive Power left: {', '.join(map(str, explosive_powers))}")

[print(f'{firework}: {count}') for firework, count in fireworks_made.items()]
