"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""
STR_VAL = 'python is the fastest-growing major programming language'


def dict_from_str(str_val: str):
    letters_list = [char for char in str_val]
    letters_set = set(letters_list)
    letters_dict = {}
    for i in letters_set:
        letters_dict[i] = str_val.count(i)
    return letters_dict


print(dict_from_str(STR_VAL))
