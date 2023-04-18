# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
N = int(input('введите количество элементов в массиве:'))
count = 0  
array_A = []
for i in range(N):
    array_A.append(randint(1,N))
for i in array_A:
    print(i, end= ' ')
print()    
X = int(input('введите число:')) 
a = sorted(array_A)
max_number = max(a)
for max_number in a:
    if max_number < X:
      x = max_number

print(x)




 