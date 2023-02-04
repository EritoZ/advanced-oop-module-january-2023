from collections import deque

elfs_energy = deque(map(int, input().split()))
materials_box = list(map(int, input().split()))
counter = 0
toys_made = 0
total_energy_used = 0

while elfs_energy and materials_box:
    counter += 1

    current_elf_energy = elfs_energy.popleft()

    if current_elf_energy >= 5:
        material_n = materials_box.pop()
        s = 2

        if counter % 3 == 0:
            material_n *= 2

        if current_elf_energy >= material_n:
            total_energy_used += material_n

            if counter % 5 == 0:
                elfs_energy.append(current_elf_energy - material_n)
                continue

            elfs_energy.append(current_elf_energy - material_n + 1)
            toys_made += 1

            if counter % 3 == 0:
                toys_made += 1

        else:
            elfs_energy.append(current_elf_energy * 2)
            materials_box.append(material_n if counter % 3 != 0 else material_n // 2)

print(f"Toys: {toys_made}")
print(f"Energy: {total_energy_used}")

if elfs_energy:
    print(f"Elves left: {', '.join(map(str, elfs_energy))}")

if materials_box:
    print(f"Boxes left: {', '.join(map(str, materials_box))}")
