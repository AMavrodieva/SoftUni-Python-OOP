from project.controller import Controller


controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Aquarium_F"))
print(controller.add_aquarium("SaltwaterAquarium", "Aquarium_S"))
print(controller.add_aquarium("Aquarium", "Aquarium"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Other"))
print(controller.insert_decoration("Aquarium_F", "Ornament"))
print(controller.insert_decoration("Aquarium_S", "Plant"))
print(controller.insert_decoration("Aquarium_F", "Other"))
print(controller.add_fish("Aquarium_F", "Other", "Fish_1", "type_1", 10))
print(controller.add_fish("Aquarium_S", "SaltwaterFish", "Fish_1", "type_1", 10))
print(controller.add_fish("Aquarium_F", "FreshwaterFish", "Fish_2", "type_2", 15))
print(controller.add_fish("Aquarium_S", "SaltwaterFish", "Fish_3", "type_1", 10))
print(controller.add_fish("Aquarium_F", "SaltwaterFish", "Fish_4", "type_2", 15))
print(controller.feed_fish("Aquarium_F"))
print(controller.feed_fish("Aquarium_S"))
print(controller.calculate_value("Aquarium_F"))
print(controller.calculate_value("Aquarium_S"))
print(controller.report())




