""" 4. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

import random

size = 11
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for j in range(0, size)]

set_array = {item: 0 for item in array}
m1 = array[0]
m2 = array[0]
for key in array:
    set_array[key] += 1
    m1 = (key if key < m1 else m1)
    m2 = (key if m1 < key < m2 else m2)


print(f'Массив случайных целых чисел до изменения \n{array}')
print(f'В массиве {set_array[m1]} минимальных элемента {m1}' if set_array[m1] > 1
      else f'Два минимальных элемента массива: {m1} и {m2}')
