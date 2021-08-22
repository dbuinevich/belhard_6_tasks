"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(class_name):
    number = school_data[class_name]
    school_data[class_name] = number + 1


def decr_students(class_name):
    number = school_data[class_name]
    if number > 0:
        school_data[class_name] = number - 1


def add_class(class_name):
    school_data[class_name] = 0


def remove_class(class_name):
    del school_data[class_name]


def calc_students(school_data):
    return sum(school_data.values())


if __name__ == '__main__':
    number_1 = school_data['1a']
    incr_students('1a')
    assert number_1 == school_data['1a'] - 1

    number_2 = school_data['2a']
    decr_students('2a')
    assert number_2 == school_data['2a'] + 1

    add_class('3a')
    assert 0 == school_data['3a']

    remove_class('2b')
    assert school_data.get('2b') is None

    assert sum(school_data.values()) == calc_students(school_data)
    print('Можешь идти спать)))')
