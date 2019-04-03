# Modeling Pi using the slower Gregory-Leibniz Series and the faster Nilakantha Series


def gregory_leibniz(n: int):
    def odd_number():
        num: int = 1
        while True:
            yield num
            num += 2

    def pi_series():
        odds = odd_number()
        approximation = 0
        while True:
            approximation += 4 / next(odds)
            yield approximation
            approximation -= 4 / next(odds)
            yield approximation

    pi = pi_series()
    for _ in range(n):
        print(next(pi))


def nilakantha(n: int):
    def denominator_generator():
        (first, second, third) = (2, 3, 4)
        while True:
            yield first * second * third
            (first, second, third) = (third, third + 1, third + 2)

    def pi_series():
        approximation = 3
        denominator = denominator_generator()
        while True:
            yield approximation
            approximation += 4 / next(denominator)
            yield approximation
            approximation -= 4 / next(denominator)

    pi = pi_series()
    for _ in range(n):
        print(next(pi))


nilakantha(10000000)
