from data import basic_plants_list, plants_list, plants_dict

people = [
    ("John Cleese", "cleese@gmail.com"),
    ("Terry Gilliam", "gilliam@gmail.com"),
    ("Eric Idle", ""),
    ("Terry Jones", "jones@gmail.com"),
    ("Graham Chapman", "chapman@gmail.com"),
    ("Michael Palin", ""),
]


if bool(people) and all([person[1] for person in people]):
    print("Sending Email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grass in this pack")


def hasType(plant_type):
    return any(
        plant for plant in plants_dict if plants_dict[plant].plant_type == plant_type
    )


# for grass in grass_generator:
#     print(grass)

print(hasType("Grass"))
print(hasType("Weed"))
print(hasType("Cactus"))
