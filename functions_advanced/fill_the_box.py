def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    cubes = list(args)

    for i, cube_or_command in enumerate(cubes):

        if box_volume <= 0:
            current_cubes = cubes[i:len(cubes)]

            if 'Finish' in current_cubes:
                current_cubes.remove('Finish')

            return f"No more free space! You have {sum(current_cubes) - box_volume} more cubes."

        elif cube_or_command == 'Finish':
            return f"There is free space in the box. You could put {box_volume} more cubes."

        box_volume -= cube_or_command


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
