# Задача 2: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите длину массива: '))
x = int(input('Введите число: '))
array = [i for i in range(1, n+1)]
near_number = 0
for i in range(len(array)):
    if x-array[i] < x-near_number and x-array[i] > 0:
        near_number = i
    elif x-array[i] > x-near_number:
        near_number = i
print(array[near_number])
    
    
# 3-1 < 3 - 0 and 3-1 > 0