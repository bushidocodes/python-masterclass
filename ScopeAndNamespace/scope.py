def fact(n):
    """calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib(n):
    if n == 1:
        result = 1
    elif n == 2:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 1
        for _ in range(1, n - 1):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(1, 100):
    print(i, fib(i))
