"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


# def get_even_number(n):
#     for i in range(1, n):
#         yield i * 2

def get_even_number():
    number = 2
    result = 0
    while True:
        result += number
        yield result


even_gen = get_even_number()
print(next(even_gen))
print(next(even_gen))
print(next(even_gen))

if __name__ == '__main__':
    even_gen = get_even_number()
    assert next(even_gen) == 2
    assert next(even_gen) == 4
    assert next(even_gen) == 6
    print('Не знаю, как написать тест для генератора(((')
