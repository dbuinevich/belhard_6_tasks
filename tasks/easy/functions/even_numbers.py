"""
Написать функцию get_even_number, которая принимает 1 аргумент - номер
четного числа и возвращает само четное число

Например:

- get_even_number(10) -> 20
- get_even_number(3) -> 6
"""


def get_even_number(n):
    number = n * 2
    return number


if __name__ == '__main__':
    assert get_even_number(8) == 16
    print('nice')
