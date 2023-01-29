from collections import deque

food_supplies = list(map(int, input().split(', ')))
stamina = deque(map(int, input().split(', ')))
conquered = []
mountain_dict = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 60
}
index = 0

while food_supplies and stamina and index < len(mountain_dict):

    power = food_supplies.pop() + stamina.popleft()

    if mountain_dict[tuple(mountain_dict.keys())[index]] <= power:
        conquered.append(tuple(mountain_dict.keys())[index])

    else:
        continue

    index += 1

if len(conquered) == len(mountain_dict):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered:
    print(f'Conquered peaks:')
    print('\n'.join(conquered))
