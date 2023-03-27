"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random

def element_in_range(my_list, min_element, max_element):
    indexs = []
    for i in range(len(my_list)):
        if (my_list[i] >= min_element) and (my_list[i] <= max_element):
            indexs.append(i)
    return indexs

def random_list(number):
    my_list = []
    for i in range(number):
        my_list.append(random.randint(1, 9))
    return my_list

n = int(input("Введите число элементов массив: "))
my_l = random_list(n)
print(*my_l)

min_el = int(input("Введите минимальное значения диапозона: "))
max_el = int(input("Введите максимальное значения диапозона: "))
print(f'Значения элементов под индексами {element_in_range(my_l, min_el, max_el)}, принадлежат заданному диапазону')
