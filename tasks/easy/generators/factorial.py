"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    number = 1
    result = 1
    while True:
        result *= number
        yield result
        number += 1


if __name__ == '__main__':
    factorial_gen = factorial()
    assert next(factorial_gen) == 1
    assert next(factorial_gen) == 2
    assert next(factorial_gen) == 6
