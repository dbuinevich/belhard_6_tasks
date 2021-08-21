"""
Написать функцию calc_sum, которая принимает неограниченное количество целых
чисел и возвращает их сумму

для расчета суммы можно воспользоваться функцией sum
"""


def calc_sum(*ints) -> int:
    # count = 0
    # for i in ints:
    #     if isinstance(i, int):
    #         count += i
    #     else:
    #         raise ValueError('Функция принимает целые числа!')
    # return count
    return sum([*ints])


if __name__ == '__main__':
    assert calc_sum(1, 2, 3, 4, 5) == 15
    print('Ваууууууу!!!')
    # try:
    #     calc_sum(1, 2, 3, 4, 'jnj')
    # except ValueError as exc:
    #     print(exc)