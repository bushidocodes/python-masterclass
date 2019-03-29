fruit = {
    "orange": "a sweet orange citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour green citrus fruit"
}

veg = {
    "cabbage": "every child's favorite",
    "sprouts": "mmmm, lovely",
    "spinach": "Can I have some more fruit please?"
}

# Merge fruit dictionary into veg dictionary. This modifies veg
veg.update(fruit)
print(veg)

# We could also create a new dictionary and merge into that
combo = {}
combo.update(fruit)
combo.update(veg)
print(combo)

# This can be simplified by copy, which returns a (shallow?) copy
comboTwo = fruit.copy()
comboTwo.update(veg)
print(comboTwo)
