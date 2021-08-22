"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""


def set_diff(a: set, b: set, c: set, symmetric=False):
    if symmetric is False:
        diff = a - b - c
    if symmetric is True:
        diff = a ^ b ^ c
    return diff


if __name__ == '__main__':
    a = {1, 2, 3}
    b = {3, 4, 5}
    c = {5, 6, 7}
    # print(a - b)
    assert set_diff(a, b, c) == {1, 2}
    assert set_diff(a, b, c, True) == {1, 2, 4, 6, 7}
