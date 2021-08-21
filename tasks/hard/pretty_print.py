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
from pprint import pformat
from yapf import FormatCode
# import json
#
data = {'a': 123, 123: [1, 2, 3], 'asd': {'c': 654.54}}
#
#
# print(json.dumps(data, sort_keys=False, indent=4))


# def decorator(func):
#     def wrapper(d, indent=0):
#         print('{')
#         result = func(d, indent=0)
#         print('}')
#         return result
#     return wrapper
#
#
# @decorator
# def pretty(d, indent=0):
#     for key, value in d.items():
#         print(f"{'    ' * indent}{key}:", end='')
#         if isinstance(value, dict):
#             pretty(value, indent+1)
#         else:
#             print(' ' * (indent+1) + str(value))
#
#
# pretty(data)
data_string = pformat(data)
formatted_code, _ = FormatCode(data_string)

print(formatted_code)
