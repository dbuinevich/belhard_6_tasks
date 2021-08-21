"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""
LIST_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LIST_2 = [i for i in range(5, 15)]


def common_numbers(list_1: list, list_2: list):
    set_1 = set(list_1)
    set_2 = set(list_2)
    intersection = set_1.intersection(set_2)
    final_list = list(intersection)
    final_list.sort(reverse=True)
    return final_list


print(common_numbers(LIST_1, LIST_2))