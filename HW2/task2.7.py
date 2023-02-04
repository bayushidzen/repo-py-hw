# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random

num = int(input('Введите N: '))
arr = []
result = 0
for i in range(-num, num+1):
    arr.append(i)
    print(f'Массив {arr}')
#Так как нет готового файла нет попробуем сгененрировать значения самостоятельно, для условных 5 итераций
print('Произведение рандомных чисел из промежутка без генерации файла')
for i in range(0, 5):
    a = random.randint(-num, num+1)
    b = random.randint(-num, num+1)
    result = arr[a] * arr[b]
    print(f'{i+1} a = {a}, b = {b}, result = {result}')
    
#Создал файл и теперь произведения считаем по файлу
print()
print('Произведение по позициям из файла')
f = open('/Volumes/KingSSD/GB/Py/Homeworks/GBPyHW/HW2/file.txt', 'r')
for i in range(0,5):
    c = int(f.readline())
    d = int(f.readline())
    result = arr[c] * arr[d]
    print(f'{i+1} c = {c}, d = {d}, result = {result}')
