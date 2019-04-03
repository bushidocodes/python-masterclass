import timeit

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


def cond_spam():
    return [meal for meal in menu if "spam" not in meal]


# meals = [meal for meal in menu if "spam" not in meal]
# print(meals)

# print("=" * 50)


def not_spam(meal_list: list):
    return "spam" not in meal_list


def filter_spam():
    return list(filter(not_spam, menu))


print(cond_spam())
print(filter_spam())


print(timeit.timeit(cond_spam, globals=globals()))
print(timeit.timeit(filter_spam, globals=globals()))
