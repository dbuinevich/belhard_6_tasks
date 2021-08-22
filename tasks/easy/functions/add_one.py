"""
Написать функцию-замыкание add_numb, которая при создании принимает число,
которое нужно прибавлять к другому числу.

После присвоения переменной она должна принимать другое число и прибавлять к
нему первое

Пример:

add_two = add_numb(2)
add_two(3)  # 5

add_three = add_numb(3)
add_three(3) # 6
"""


def add_numb(n):
    def add_one_more(m):
        return n + m
    return add_one_more


if __name__ == '__main__':
    assert (add_numb(5))(2) == 7
    print((add_numb(5))(2))
    print("Решено!")
