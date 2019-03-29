
# Technically, a tuple does not need to be defined with paranthesis. It is just a comma delimited list of elements
t = "a", "b", "c"
print(t)

# However, in practice, it's a good idea to wrap tuples with parenthesis because of ambiguous situations, such as print instead interpreting the tuple as distince arguments
print("a", "b", "c")
print(("a", "b", "c"))

metallica = "Ride the Lightning", "Metallica", 1984
print(metallica)
print(metallica[0])

# Unlike Lists, Tuples are immutable, so the following line is impossible
# metallica[0] = "Master of Puppets"
# But we can create a new Tuple using the previous one
metallicaTwo = ("Master of Puppets", metallica[1], metallica[2])
print(metallicaTwo)

# Because Tuples are immutable, they can be use as Dictionary keys
# Tuples are intended to be used for heterogeneous types
# Lists are intended to be used for homogeneous types


# We can destructure tuples too. This is called "unpacking the tuple" in Python
# However, this can only unplack one level at a time, and it needs to unpack all elements
title, artist, year = metallicaTwo
print(title)

# Tuples can have a nested structure, like the following
imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"),
    (2, "Psycho"),
    (3, "Mayhem")
)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
first, second, third = tracks
print(first)
print(second)
print(third)

# A Tuple can contain a list. The reference to the list is immutable, but the elements in the list can change
