# Задайте натуральное число N. 
# Напишите программу, которая составит список 
# простых множителей числа N.
# 100 = 2 * 2 * 5 * 5

def factorize(n):
    arr = []
    i = 2
    while i * i <= n:
        while n % i == 0: 
            n //= i
            arr.append(i)
        i += 1
    if n > 1:
        arr.append(n)
    return arr

natur = int(input('Введите натуральное число: '))

print(natur, '=', ' x '.join(str(x) for x in factorize(natur)))