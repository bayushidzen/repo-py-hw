# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
import random

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

arr_orig_len = int(input('Введите длину массива: '))
arr_orig = []

for i in range(0, arr_orig_len):
    arr_orig.append(random.randint(1,20))
arr_orig = quicksort(arr_orig)
print(arr_orig)

arr_2 = []
for i in range(0, len(arr_orig)):
    if arr_orig[i] not in arr_2:
        arr_2.append(arr_orig[i])
print(arr_2)