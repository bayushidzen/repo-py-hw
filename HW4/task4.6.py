# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

def write_file(t):
    f = open('test.txt','w')
    f.write(t)
    print(t)
    
def make_equation():
    equality = str(arr_koef[0]) + '*x^'+ f'{k}'
    for i in range(1, k):
        equality += ' + ' + str(arr_koef[i]) + '*x^'+ f'{k-i}'
    equality += ' = 0 '
    return equality

k = int(input('Укажите значение натуральной степени: '))
arr_koef = []

for i in range(0, k):
    arr_koef.append(random.randint(0,100))
print(arr_koef)

write_file(make_equation())
