burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# Generates tuples for all of the permeatations. O(n^2) madness
for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)

print("*" * 10)
for burger in burgers:
    for topping in toppings:
        print((burger, topping))
