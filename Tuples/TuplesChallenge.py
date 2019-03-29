# Tuples can have a nested structure, like the following
imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"),
    (2, "Psycho"),
    (3, "Mayhem"),
    (3, "Kentish Town Waltz")
)

title, band, year, tracks = imelda
print("Album:", title)
print("Band:", band)
print("Year:", year)
print("Tracks:")
for number, songName in list(tracks):
    print("\t", number,  songName)
