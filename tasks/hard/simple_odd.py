"""
Написать 2 генератора:
1) Генератор simple_number первый идет по всем простым числам
(число делится только на 1 и на само себя)
2) Генератор odd_simple, который используется значения первого и возвращает
из них нечетные
"""
import math


def simple_number():
    prime = 2
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(prime) + 1)):
            if prime % x == 0:
                isprime = False
                break
        if isprime:
            yield prime
        prime += 1


# simple = simple_number()
# print(next(simple))
# print(next(simple))
# print(next(simple))
# print(next(simple))


def odd_simple():
    for odd_prime in simple_number():
        if odd_prime % 2 != 0:
            yield odd_prime


odd = odd_simple()
print(next(odd))
print(next(odd))
print(next(odd))
print(next(odd))
