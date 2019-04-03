def fibonacci(numberToReturn: int):
    result = []

    def fibonacciGenerator():
        (current, previous) = (1, 1)
        while True:
            (current, previous) = (current + previous, current)
            yield current

    if numberToReturn >= 1:
        result.append(1)
    if numberToReturn >= 2:
        result.append(1)
    if numberToReturn >= 3:
        fib = fibonacciGenerator()
        for _ in range(numberToReturn - 2):
            result.append(next(fib))
    return result


print(fibonacci(5))
