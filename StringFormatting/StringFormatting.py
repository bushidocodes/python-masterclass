age = 33

# Python will not automatically convert integers to strings
# We can coerce an integer to a string with str()
print("My age is " + str(age) + " years")

# Or we can use replacement fields
print("My age is {0} years".format(age))
print("There are {0} days in {1}".format(31, "January"))

# If we combine multiline strings with replacement fields, we have something like JS Tagged Template Literals
print("""January: {2}
February: {0}
March: {2}
April: {1}""".format(28, 30, 31))

# Python used to support C style string formatting operators, but this has been deprecated in Python 3
print("My age is %d years" % age)
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))
print("Pi is approximately %12.50f" % (22/7))

# The first part is the index of the value and the second is the width to use when formatting
print("My age is {0}".format(age))
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
# The width value can include a decimal, in which case it is the width of the parts before and after the decimal
print("Pi is approximately {0:12.50}".format(22/7))

# if the index isn't provided, they are assumed increment in order and have a 1:1 relationship with the args to format
name = "Sean"
print("Hi. My name is {} and my age is {}".format(name, age))
