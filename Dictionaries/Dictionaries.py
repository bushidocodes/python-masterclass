# Sets and Dictionaries guarantee uniqueness
# Sets are like Lists, but you can't access individual elements
# Sets and Dictionaries are unordered

fruit = {
    "orange": "a sweet orange citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour green citrus fruit"
}

print(fruit)
print(fruit["lemon"])

fruit["pear"] = "An odd shaped apple"
print(fruit)

fruit["pear"] = "Great with Tequilla!"
print(fruit)

del fruit["pear"]
print(fruit)

# Accessing a key that doesn't exist throws an error
# print(fruit["tomato"])

# One way of handling this is by using get, which returns a default value when the key isn't found
print(fruit.get("tomato", "Sorry no tomato!"))

print("="*50)
###################################
# Dictionaries are unordered but we can extract the keys, sort them, and use them to retrieve the values
fruit_keys = list(fruit.keys())
fruit_keys.sort()
for f in fruit_keys:
    print(f, "is", fruit[f])

print("="*50)
###################################
# Or even terser
for f in sorted(fruit.keys()):
    print(f, "is", fruit[f])

print("="*50)
###################################
# Or easier if we don't need to guarantee order
for key in fruit:
    print(key, "is", fruit[key])

print("="*50)
###################################
# We can just return the values too
print(fruit.values())

print("="*50)
###################################
# We can also return ordered pairs of keys and values as a list of tuples
orderedPairs = list(fruit.items())
print(orderedPairs)

# and this can be easier cast back into a dictionary
print(dict(orderedPairs))

print("="*50)
###################################
fruit.clear()
print(fruit)
