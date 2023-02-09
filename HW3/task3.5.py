# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

num_array = int(input('Введите N: '))
arr = []
sum_array = []
for i in range(0, num_array):
    arr.append(random.randint(1, 10))
print(f'Наш массив {arr}')
for i in range(0, round(num_array/2)):
    sum_array.append(arr[i] + arr[-i-1])
print(f'Попарная сумма массива: {sum_array}')