"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент
"""


def factorial(n, result=1, number=1):
    if number <= n:
        return factorial(n, result * number, number + 1)
    else:
        return result


# def factorial(n, result=1):
#     if n > 0:
#         return factorial(n - 1, result * n)
#     else:
#         return result


if __name__ == '__main__':
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6