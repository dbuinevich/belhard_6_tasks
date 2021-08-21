"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def recursion(n: int):
    if n == 0:
        return 0
    if n > 0:
        ost = n % 10
        return ost + recursion(n // 10)


print(recursion(127))