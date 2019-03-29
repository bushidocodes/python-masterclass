import pickle


imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"),
    (2, "Psycho")
)

# We can "pickle" multiple objects into a single file
# They just need to be written and read in the same order
# Please not that the Pickle protocol has different versions, and they are not backwards compatible
# You need to specify the protocol version if loading an older version
with open("./BinaryIO/imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(list(range(0, 10, 3)), pickle_file)

with open("./BinaryIO/imelda.pickle", "rb") as pickle_file_2:
    imelda2 = pickle.load(pickle_file_2)
    even = pickle.load(pickle_file_2)

print(imelda2)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for track in tracks:
    trackNum, trackTitle = track
    print("{}. {}".format(trackNum, trackTitle))
print(even)
