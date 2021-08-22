"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multiply(n):
    def closure(x):
        return x * n
    return closure


if __name__ == '__main__':
    assert multiply(2)(6) == 12
    print('very nice')
