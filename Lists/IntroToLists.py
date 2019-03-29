# # ipAddress = input("Please enter an IP address: ")
# # print(ipAddress.count("."))

# parrotList = ["not pinin'", "no more", "a stiff", "bereft of life"]
# parrotList.append("a Norwegian Blue")
# for state in parrotList:
#     print("This parrot is", state)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even + odd
# print(sorted(numbers))  # Sorts and returns, mutating nothing
# print(numbers)
# numbers.sort()  # Sorts in place, returning nothing
# print(numbers)

listOne = []
listTwo = list()
print(listOne == listTwo)  # Shallow compare by value
print(listOne is listTwo)  # Compare by reference

# Sorted is a pure function that creates a new List, leaving the original unchanged
ninjaTurtles = ["Raphael", "Leonardo", "Michaelangelo", "Donatello"]
sortedTurtles = sorted(ninjaTurtles)
print(ninjaTurtles == sortedTurtles)  # Shallow compare by value
print(ninjaTurtles is sortedTurtles)  # Compare by reference

# An iterable can return members one by one
# All Sequence types in Python are iterables

name = "Sean"
arrayOfChars = list(name)
print(arrayOfChars)
