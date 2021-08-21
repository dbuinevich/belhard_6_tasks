"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""


def reverse_dict(addict: dict):
    new_dict = {v: k for k, v in addict.items()}
    return new_dict


if __name__ == '__main__':
    addict = {1: 111, 2: 222}
    print(reverse_dict(addict))
    assert reverse_dict(addict) == {111: 1, 222: 2}
