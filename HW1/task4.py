# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_col = int(input('Введите количество долек шоколадки по вертикали: '))
chocolate_row = int(input('Введите количество долек шоколадки по горизонтали: '))
chocolate_parts = int(input('Сколько долек вы хотите отломить? '))

if chocolate_col > chocolate_row:
    min = chocolate_row
else: 
    min = chocolate_col
if chocolate_parts > min:
    if chocolate_parts % chocolate_col == 0 or chocolate_parts % chocolate_row == 0:
        print(f'Вы можете отломить {chocolate_parts} долек')
    else: 
        print('Неа, так шоколадка не ломается')
else: 
    print('Неа, так шоколадка не ломается')