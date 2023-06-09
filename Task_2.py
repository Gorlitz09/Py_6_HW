# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
my_list = [randint(0, 10) for _ in range(10)]
min_number = int(input('Введите минимальное число: '))
max_number = int(input('Введите максимальное число: '))
for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        print(i)