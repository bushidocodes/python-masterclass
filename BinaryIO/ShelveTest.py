# The problem with pickling is that all of the contents of the file need to be loaded into memory
# This can be a problem for big data type algorithms (e.g. loading a billion edge edgelist)
# The shelve module is the solution for this
# It provides a "shelf", which is a file that acts like a dictionary
# The keys are strings and the values can be anything that can be pickled
# items on the shelf can be loaded into memory as needed
# The shelf provides the same methods as a dictionary

import shelve

# with shelve.open("./BinaryIO/ShelfTest") as fruit:
fruit = shelve.open("./BinaryIO/ShelfTest")
fruit["orange"] = "a sweet, orange, citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "sour yellow citrus fruit"
fruit["grape"] = "small sweet fruit in bunches"
fruit["lime"] = "sour green citrus fruit"
# print(fruit["lemon"])
# print(fruit["grape"])

fruit["lime"] = "great with tequilla"
# print(fruit["lime"])


while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key == "quit":
        break
    description = fruit.get(shelf_key, "We don't have a {}".format(shelf_key))
    print(description)

fruit.close()
