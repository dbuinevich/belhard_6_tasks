"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(int_list: list):
    new_list = []
    for x in int_list:
        new_list.append(x)
        if new_list.count(x) > 1:
            print('Yes')
        else:
            print('No')


yes_or_no([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 4])
