string = "1234567890"

# An iterator is created from the string and then used to return the elements one at a time
for char in string:
    print(char)

# This is similar to
letters = "abcdefg"
lettersIterator = iter(letters)
print(lettersIterator)
print(next(lettersIterator))
print(next(lettersIterator))
print(next(lettersIterator))
print(next(lettersIterator))
print(next(lettersIterator))
print(next(lettersIterator))
print(next(lettersIterator))

# What happens if we call next on an empty iterator though?
print(next(lettersIterator))
# The Iterator throws a StopIteration error
# The for loop basically calls next until it iternally catches this error
