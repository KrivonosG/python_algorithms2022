"""Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def check(a, even=0, odd=0):
    if a == 0:
        return even, odd
    else:
        m = a % 10
        a = a // 10
        if m % 2 == 0:
            even += 1
        else:
            odd += 1
        return check(a, even, odd)


try:
    numb = int(input('Введите число: '))
    print(f'Количество чётных и нечётных цифр в числе: {check(numb)}')
except ValueError:
    print('Ошибка: Неверный формат числа!')
