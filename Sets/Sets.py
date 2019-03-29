# Operation	            Equivalent	Result
# len(s)	 	                    number of elements in set s (cardinality)
# x in s	 	                    test x for membership in s
# x not in s	 	                test x for non-membership in s
# s.issubset(t)	            s <= t	test whether every element in s is in t
# s.issuperset(t)	        s >= t	test whether every element in t is in s
# s.union(t)	            s | t	new set with elements from both s and t
# s.intersection(t)	        s & t	new set with elements common to s and t
# s.difference(t)	        s - t	new set with elements in s but not in t
# s.symmetric_difference(t)	s ^ t	new set with elements in either s or t but not both
# s.copy()	 	                    new set with a shallow copy of s



# There are two ways to define sets. Curly braces with a comma delimited list of elements and the set constructor
farmAnimals = {"sheep", "cow", "hen"}
print(farmAnimals)

for animal in farmAnimals:
    print(animal)

print("="*40)

wildAnimals = set(["lion", "tiger", "panther", "elephant"])
print(wildAnimals)

for animal in wildAnimals:
    print(animal)

print("="*40)
# We add elements to a set with the add method
farmAnimals.add("horse")
wildAnimals.add("horse")
print(farmAnimals)
print(wildAnimals)

print("="*40)
# Sets have union and intersection operations
even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

# Set Union
print(set.union(squares, even))
print(even.union(squares))
print(squares | even)

# Set Intersection
print(squares.intersection(even))
print(set.intersection(squares, even))
print(squares & even)

# Set Difference / Subtraction
print(even.difference(squares))
print(set.difference(even, squares))
print(even - squares)

# Set Difference Action that Mutates the original Set
print("=" * 40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

# Symmetric Difference of Two Sets
# All members of one set or the other, but not both
# This is the opposite of the intersection of the two sets
# Returns all but the intersection
# The results seem to be sorted, but this isn't a documented behavior
print("=" * 40)
firstSet = set(range(0, 40, 2))
print(sorted(firstSet))
cubes_tuple = (1, 8, 27)
cubes = set(cubes_tuple)
print(sorted(cubes))
print("Symmetric even minus cubes")
# Order doesn't matter, so this is the same as two lines down
print(sorted(even.symmetric_difference(cubes)))
print("Symmetric cubes minus even")
print(sorted(cubes.symmetric_difference(even)))
# Symmetric different can also be performed by the ^ operator
print(cubes ^ even)
# symmetric_difference_update mutates the set calling the method
print(cubes)
cubes.symmetric_difference_update(even)
print(cubes)

# There are two ways to remove an item from a python list: remove and discard
print("=" * 40)
# Remove raises an error if the set does not contain the element. discard does not
nums = set(range(1, 11, 1))
print(nums)
nums.discard(1)
nums.discard(11)
print(nums)
nums.remove(2)

# Remove throws a KeyError if the member isn't in the set, so we need to use error handling
try:
    nums.remove(11)
except KeyError:
    print("The item 11 is not a member")

print(nums)

# Is Subset / Is Superset
fibs = set({1, 1, 2, 3, 5, 8, 13, 21, 34})
minifibs = set({1, 1, 2, 3})
if minifibs.issubset(fibs):
    print("minifibs is a subset of fibs")
if fibs.issuperset(minifibs):
    print("fibs is a superset of minifibs")

# Frozen Set is immutable and cannot be changed.
# We can use a frozen set as a dictionary key or even add it as a member of another set
# We can use frozen sets in unions and intersections and we can subtract frozen sets from normal sets
even = frozenset(range(0, 100, 2))
