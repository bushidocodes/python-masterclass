print(1+2)
print(7*6)
greeting = "Hello"

# Taking User Input from STDIN
# name = input("Please enter your name ")
# print(greeting + " " + name)


# Multiline String using Triple Quotes
splitString = """Once upon a time
a man was 
in a great forest
grrreeeaat forrest"""

print(splitString)


# A variable is allocated without any keywords
# Valid names must start with a letter or _
# It is considered "pythonic" to use snake case

# Integer
secret_number = 42

# Operators
a = 12
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # Converts to a float to perform division and returns float
print(a // b)  # Converts to a float to perform division and returns integer. This is like taking a floor of the resulting float
print(a % b)


for i in range(1, 4):  # the upper bound is exclusive
    print(i)

# Sequence Data Types

# A String is an array of characters like C
name = "Sean McBride"
print(name[1])

# Python allows us to slice sequence data types using array notation. start index inclusive | end index exclusive | step
print(name[5:])  # From the char at idx to the end
print(name[0:3])  # From the char at idx to the end
print(name[:-1])
print(name[::2])  # From start to end, every 2nd character

# Interestingly, if the step is negative, we can go in reverse order
print(name, "when reversed is", name[::-1])

# Even weirder, you can use the * operator to have a string get repeated
print("Wakka"*10)

# Python has an "in" operator that evaluates to a boolean expressing if a certain substring is present in a string
print("America" in "United States of America")
