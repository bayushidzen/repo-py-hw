# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

array_length = int(input('Введите N: '))
arr = []
count = 0
for i in range(0, array_length):
    arr.append(random.randint(1, 10))
print(f'Массив {arr}')
num2 = int(input('Какое число нужно посчитать? '))
for i in range(0, array_length):
    if arr[i] == num2:
        count += 1
print(f'Число встречается {count} раз')