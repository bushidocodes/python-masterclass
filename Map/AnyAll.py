# all and any evaluate each element to truthy or falsy
# all requires all be truthy to return true
# any requires one elem to be truthy to return true

entries = [1, 2, 3, 4, 5]
print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

entries_with_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))

print("+" * 40)

# The biggest gotcha is that an empty list evaluates to true with all
print("all with empty: {}".format(all([])))

# If we want empty lists to evaluate to false
empty = []
print("all with empty: {}".format(bool(empty) and all(empty)))
