# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

num_array = int(input('Введите N: '))
arr = []
sum_array = 0
for i in range(0, num_array):
    arr.append(random.randint(1, 100))
print(f'Наш массив {arr}')
for i in range(1, num_array, 2):
    sum_array = sum_array + arr[i]
    print(arr[i], sum_array)
print(f'Сумма элементов на нечентных позициях: {sum_array}')