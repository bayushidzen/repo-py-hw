# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
#{F(-n)=(-1)^{n+1}*F(n)}
# Fn = F(n+2)−F(n+1).

num1 = 1
num2 = -1
ne_fi_arr = []
ne_fi_arr.append(num1)
ne_fi_arr.append(num2)
for i in range (-3,-11,-1):
    ne_fi_num = num1-num2
    num1 = num2
    num2 = ne_fi_num
    ne_fi_arr.append(ne_fi_num)
    print(i, ne_fi_arr)