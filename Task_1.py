# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введите число прогрессии: '))
d = int(input('Введите разность прогрессии: '))
n = int(input('Введите n-ый член прогрессии: '))
for i in range(n):
    print('Ответ: ', a1 + i * d)