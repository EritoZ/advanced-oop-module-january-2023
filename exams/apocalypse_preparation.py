from collections import deque

textiles = deque(map(int, input().split()))
medicaments = list(map(int, input().split()))
healing_items_dict = {
    30: ['Patch', 0],
    40: ['Bandage', 0],
    100: ['MedKit', 0]
}

while textiles and medicaments:

    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    sum_elements = current_textile + current_medicament

    if sum_elements in healing_items_dict:

        healing_items_dict[sum_elements][-1] += 1

    elif sum_elements > 100:

        healing_items_dict[100][-1] += 1

        medicaments[-1] += sum_elements - 100

    else:
        medicaments.append(current_medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not medicaments:
    print("Medicaments are empty.")

else:
    print("Textiles are empty.")

for value, item in sorted(healing_items_dict.items(), key=lambda x: (-x[1][1], x[1][0])):
    if item[1]:
        print(f'{item[0]} - {item[1]}')

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, medicaments[::-1]))}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
