"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на одну табуляцию

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""
some_list = [1, 2, [1, 2, [5, 7], 3], 8]


def line_print(any_list: list, n=0):
    for element in any_list:
        if isinstance(element, list) is True:
            line_print(element, n+1)
        else:
            tab = '\t' * n
            print(f"{tab}{element}")


line_print(some_list)


