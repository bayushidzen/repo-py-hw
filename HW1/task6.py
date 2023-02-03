# 2) Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

xyz = ["X", "Y", "Z"]
arr = []
for i in range(0,3):
    arr.append(input(f' Введите {xyz[i]}: '))
left = not (arr[0] or arr[1] or arr[2])
right = not arr[0] and not arr[1] and not arr[2]
print(f"Массив {arr}")
if left == right:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
