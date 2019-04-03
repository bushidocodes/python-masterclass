print(__file__)


# List Comprehension is a method to create a new list with elements based on an existing list
# Syntactically like a for loop without a column
numbers = [1, 2, 3, 4, 5, 6]
squares = [number ** 2 for number in numbers]
squares = [number ** 2 for number in range(1, 101)]
# Set comprehensions work the exact same way
squaresSet = {number ** 2 for number in numbers}

print(squares)
