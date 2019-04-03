import timeit

# Guido von Rossum wanted to remove map, filter, and reduce
# https://www.artima.com/weblogs/viewpost.jsp?thread=98196

text = "what have the Romans ever done for us"


# Map
def map_capitals():
    return list(map(str.upper, text))


def list_comp_capitals():
    return [char.upper() for char in text]


# Map
def map_words():
    return list(map(str.upper, text.split(" ")))


def list_comp_words():
    return [word.upper() for word in text.split(" ")]


result_1 = timeit.timeit(map_capitals, globals=globals(), number=100000)
result_2 = timeit.timeit(list_comp_capitals, globals=globals(), number=100000)
result_3 = timeit.timeit(map_words, globals=globals(), number=100000)
result_4 = timeit.timeit(list_comp_words, globals=globals(), number=100000)

print(map_capitals())
print(list_comp_capitals())
print(map_words())
print(list_comp_words())

print("map_capitals:\t\t{}".format(result_1))
print("list_comp_capitals:\t{}".format(result_2))
print("map_words:\t\t{}".format(result_3))
print("list_comp_words:\t{}".format(result_4))

