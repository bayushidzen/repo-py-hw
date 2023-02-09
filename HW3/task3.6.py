# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

num_array = int(input('Введите N: '))
arr = []
sum_array = []
maxi = 0
mini = 1000
for i in range(0, num_array):
    arr.append(round(random.random(),3))
print(f'Наш массив {arr}')
for i in range(0, num_array):
    check_numb = arr[i]%1
    if check_numb > maxi:
        maxi = check_numb
    elif check_numb < mini:
        mini = check_numb
print(round(maxi - mini,3))