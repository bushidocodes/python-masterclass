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
    else:
        meals.append("A meal was skipped!")
print(meals)


meals = [meal for meal in menu if "spam" not in meal]
print(meals)

# Conditional Expressions a.k.a. Ternary Expressions
x = 13
expression = "Twelve" if x == 12 else "unknown"
print(expression)

# Conditional Expressions in List Comprehension
meals = [meal if "spam" not in meal else "A meal was skipped!" for meal in menu]
print(meals)

# Complex Conditional Expressions in List Comprehension
meals = [
    "contains chicken"
    if "chicken" in meal
    else "contains bacon"
    if "bacon" in meal
    else "Contains neither"
    for meal in menu
]
print(meals)
