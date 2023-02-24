# Вычислить число ПИ c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = float(input('Введите интересующую точность числа Пи: '))
count = 0
num_pi = 3
for i in range(3, int(d), 2):
    if count % 2 == 0: 
        num_pi += 4/((i-1)*i*(i+1))
        count += 1
    else:
        num_pi -= 4/((i-1)*i*(i+1))
        count += 1
print(f'Число Пи с заданной точностью: {round(num_pi,int(d))}')