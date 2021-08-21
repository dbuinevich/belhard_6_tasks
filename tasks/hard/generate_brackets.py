"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
generate_brackets(3)
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def generate_brackets(n, sequence='', opening=0, closing=0):
    if len(sequence) < n * 2:
        if opening < n:
            generate_brackets(n, sequence + '(', opening + 1, closing)
        if closing < opening:
            generate_brackets(n, sequence + ')', opening, closing + 1)
    else:
        print(sequence)


generate_brackets(5)
