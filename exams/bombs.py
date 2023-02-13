from collections import deque

bomb_effects = deque(map(int, input().split(',')))
bomb_casings = list(map(int, input().split(',')))
filled_pouch = False
bombs_dict = {
    60: ['Cherry Bombs', 0],
    40: ['Datura Bombs', 0],
    120: ['Smoke Decoy Bombs', 0]
}

while bomb_effects and bomb_casings and not filled_pouch:

    current_bomb_effect = bomb_effects[0]
    current_bomb_casing = bomb_casings[-1]
    sum_values = current_bomb_effect + current_bomb_casing

    if sum_values in bombs_dict:
        bombs_dict[sum_values][1] += 1

        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    check_counters = (bomb[1] >= 3 for bomb in bombs_dict.values())
    filled_pouch = all(check_counters)

if filled_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

for bomb, bomb_count in bombs_dict.values():
    print(f'{bomb}: {bomb_count}')
