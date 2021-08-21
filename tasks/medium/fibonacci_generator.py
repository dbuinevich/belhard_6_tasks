"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    fib1 = 1
    fib2 = 2
    i = 0
    while i < num_count:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
        i += 1


fibonacci_gen = fibonacci(5)
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))

