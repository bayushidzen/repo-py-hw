# 4) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))
match quarter:
    case 1:
        print('Вы выбрали первую четверть')
        print('X может принимать значения от 0 до бесконечности')
        print('Y может принимать значения от 0 до бесконечности')
    case 2:
        print('Вы выбрали вторую четверть')
        print('X может принимать значения от минус бесконечности до 0')
        print('Y может принимать значения от 0 до бесконечности')
    case 3:
        print('Вы выбрали третью четверть')
        print('X может принимать значения от минус бесконечности до 0')
        print('Y может принимать значения от минус бесконечности до 0')
    case 4:
        print('Вы выбрали четвертую четверть')
        print('X может принимать значения от 0 до бесконечности')
        print('Y может принимать значения от минус бесконечности до 0')
    case _:
        print('Введите, пожалуйста, число от 1 до 4')