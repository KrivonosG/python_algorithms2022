"""Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

range = input('Введите последовательность: ')
patten = input('Введите цифру для поиска: ')
count = 0

for i in range:
    if i == patten:
        count += 1

print(f'Цифра встречается {patten} в последовательности {range}: {count} раз(а)')