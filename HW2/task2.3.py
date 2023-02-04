# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

degree_num = int(input('Введите число: '))
degree = 1
while degree < degree_num:
    print(degree, end=' ')
    degree = degree * 2
    