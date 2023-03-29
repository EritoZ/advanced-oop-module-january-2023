from project.controller import Controller

controller = Controller()

print(controller.add_aquarium('FreshwaterAquarium', 'Dad'))
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Ornament'))
print(controller.insert_decoration('Dad', 'Plant'))
print(controller.insert_decoration('Dad', 'DAS'))
print(controller.add_fish('Dad', 'FreshwaterFish', 'Dada', '???', 23))
print(controller.add_fish('Dad', 'FreshwaterFish', 'FASS', '???', 23))
print(controller.add_aquarium('FreshwaterAquarium', 'Dad'))
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Ornament'))
print(controller.insert_decoration('Dad', 'Plant'))
print(controller.insert_decoration('Dad', 'DAS'))
print(controller.add_fish('Dad', 'FreshwaterFish', 'Dada', '???', 23))
print(controller.add_fish('Dad', 'FreshwaterFish', 'FASS', '???', 23))
print(controller.aquariums[0].fish[0].size)
print(controller.feed_fish('Dad'))
print(controller.aquariums[0].fish[0].size)

print(controller.report())