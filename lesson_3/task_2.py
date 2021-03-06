""" 2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. """

import random

size = 11
min_item = 1
max_item = 100
array = [random.randint(min_item, max_item) for j in range(0, size)]
min_digit = array[0]
max_digit = array[0]
max_el = 0
min_el = 0

print(f'Массив случайных целых чисел до изменения:\n'
      f'{array}')
for i, item in enumerate(array):
    max_digit = (item if item > max_digit else max_digit)
    min_digit = (item if item < min_digit else min_digit)
    max_el = (i if max_digit == item else max_el)
    min_el = (i if min_digit == item else min_el)
array[max_el], array[min_el] = array[min_el], array[max_el]
print(f'Минимальное число {min_digit}, в массиве  находится на {min_el} позиции;\n'
      f'Максимальное число {max_digit}, в массиве  нахолится на {max_el} позиции;')
print(f'Массив случайных целых чисел после изменения:\n'
      f'{array}')
