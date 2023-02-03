# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
def crane_print(p, k, s):
    print(f'Петя собрал {round(p)} журавликов')
    print(f'Катя собрала {round(k)} журавликов') 
    print(f'Сережа собрал {round(s)} журавликов') 
    
cranes_num = int(input('Сколько всего журавликов сделали дети? Введите четное число: '))
if cranes_num < 6:
    print('Дети способны на большее, они не могли собрать так мало журавликов')
else:
    if cranes_num % 6 == 0:
        even = True
    else:
        even = False
    petes_cranes = serge_cranes = cranes_min_part = cranes_num / 6
    kate_cranes = 2 * (petes_cranes + serge_cranes)
    if even:
        crane_print(petes_cranes, kate_cranes, serge_cranes)
    else: 
        crane_print(petes_cranes, kate_cranes, serge_cranes)
        print('Внезапно у детей оказались лишние журавлики, которые делали не они ;) ')