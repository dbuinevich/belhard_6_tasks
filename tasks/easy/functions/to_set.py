"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


def to_set(list_to_set: list):
    new_set = set(list_to_set)
    return new_set, len(new_set)


if __name__ == '__main__':
    some_list = [1, 2, 3, 4, 5]
    assert to_set(some_list) == ({1, 2, 3, 4, 5}, 5)
