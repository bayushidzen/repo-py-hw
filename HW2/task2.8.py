# Реализуйте алгоритм перемешивания списка.
import random
arr = []

for i in range(0,10):
    arr.append(random.randint(0,100))
print(arr)
mixedarr = random.shuffle(arr)
print(mixedarr)