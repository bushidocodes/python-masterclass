independentCities = ["Alexandria", "Fairfax City",
                     "Falls Church", "Manassas", "Fredericksburg"]

with open("./FileIO/output.txt", "w") as cityFile:
    for city in independentCities:
        print(city, file=cityFile)


moreIndependentCities = ["Roanoke", "Salem", "Williamsburg"]
with open("./FileIO/output.txt", 'a') as cityFile:
    for city in moreIndependentCities:
        print(city, file=cityFile)

cities = []

with open("./FileIO/output.txt", "r") as cityFile:
    for city in cityFile:
        cities.append(city.strip('\n'))  # Strip leading or trailing newlines

for city in cities:
    print(city)


# This seems like a bad idea, but complex tuples can be written to a textfile and then evaled
# The file could have malicious code injected, which would get executed

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"),
    (2, "Psycho")
)

with open("./FileIO/imeldaBuffer.txt", 'w') as imeldaBuffer:
    print(imelda, file=imeldaBuffer)

with open("./FileIO/imeldaBuffer.txt", 'r') as imeldaBuffer:
    contents = imeldaBuffer.readline()

imelda2 = eval(contents)

print(imelda2)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
