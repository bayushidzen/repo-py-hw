# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

deci_num = int(input('Введите двоичное число: '))
n = deci_num
bin_arr = []
while n > 0:
    bin_num = n % 2
    bin_arr.append(str(bin_num))
    n = n // 2
bin_arr.reverse()
bin_num = int(''.join(bin_arr))
print(f'Число {deci_num} в двоичной системе = {bin_num}')