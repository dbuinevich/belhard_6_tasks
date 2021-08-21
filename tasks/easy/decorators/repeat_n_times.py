"""
Написать функцию bang, которая печатает "Boom"
Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""


def repeat_n_times(func):
    def wrapper(n):
        for i in range(n):
            result = func()
        return result
    return wrapper


@repeat_n_times
def bang():
    print('Boom')


bang(4)