menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"],
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
print(meals)

# Conditional Comprehensions are like a filter
# We can't have an else block
meals = [meal for meal in menu if "spam" not in meal]
print(meals)

# Conditional Comprehensions are just strung together if there are multiple conditions in an AND relationship
meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
print(meals)

# But you can also use "and" and "or" instead to make things more readable
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)
meals = [meal for meal in menu if "spam" in meal or "chicken" in meal]
print(meals)
