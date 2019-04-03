from functools import reduce
from timeit import timeit


def calc_values(x, y: int):
    return x + y


numbers = [2, 3, 5, 8, 13]


def reduce_sum():
    return reduce(calc_values, numbers)


def builtin_sum():
    return sum(numbers)


print(reduce_sum())

print(builtin_sum())

print(timeit(reduce_sum, globals=globals()))
print(timeit(builtin_sum, globals=globals()))
