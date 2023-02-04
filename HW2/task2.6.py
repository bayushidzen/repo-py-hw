# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

num = int(input('Введите число: '))
result = 0
sum = 0
for i in range(1, num+1):
    result = (1 + 1/i) ** i
    sum = sum + round(result,2)
print(f' Сумма чисел последовательности равна: {sum}')

