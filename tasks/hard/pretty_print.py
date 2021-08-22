"""
Написать рекурсивную функцию, которая будет красиво выводить данные в консоль.
Если строчный тип данных, то выводить в кавычках


например:

data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}

{
    'a': 123,
    123: [1, 2, 3],
    'asd': {
        'c': 654.54,
    },
}
"""
"""
from print_dict import pd
data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}

pd(data)
# вот это топовый рабочий вариант без всяких рекурсий
"""

data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}


def pretty(d, n=1, spaces=''):
    tab = '\t' * n
    row = '\n'
    cl_tab = '\t' * (n - 1)
    print(spaces + '{' + row, end='')
    for key, value in d.items():
        if isinstance(value, dict) is True:
            if isinstance(key, str) is True:
                print(f"{tab}'{key}':", end='')
            else:
                print(f"{tab}{key}:", end='')
            pretty(value, n + 1, spaces=' ')
        else:
            if isinstance(key, str) is True:
                print(f"{tab}'{key}': {value},")
            else:
                print(f"{tab}{key}: {value},")
    if n == 1:
        print(cl_tab + '}')
    else:
        print(cl_tab + '},')


pretty(data)
