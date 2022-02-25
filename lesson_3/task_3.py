""" 3. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве. """

import random
size = 11
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for j in range(0, size)]

if [j for j in array if j < 0]:
    m = array[0]
    p = 0
    for i, item in enumerate(array):
        m = item if (item < m >= 0) or (m < item < 0) else m
        p = i if m == item else p
    print(f'Массив значений:\n {array}')
    print(f'Максимальный отрицательный элемент массива {m} в позиции {p}')
else:
    print('Массив не содержит отрицательных элементов')
