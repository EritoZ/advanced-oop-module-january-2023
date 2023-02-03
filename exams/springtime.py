def start_spring(**kwargs):
    spring_things = kwargs
    sorted_spring_things = {}

    for spring_object, object_type in spring_things.items():

        if object_type not in sorted_spring_things:
            sorted_spring_things[object_type] = []

        sorted_spring_things[object_type].append(f'-{spring_object}')

    sorted_spring_things = dict(sorted(sorted_spring_things.items(), key=lambda x: (-len(x[1]), x[0])))

    for type in sorted_spring_things:
        sorted_spring_things[type] = '\n'.join(sorted(sorted_spring_things[type]))

    return '\n'.join([f'{type}:\n{objects}' for type, objects in sorted_spring_things.items()])


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))