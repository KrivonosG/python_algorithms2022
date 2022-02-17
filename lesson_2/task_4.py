"""Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число."""


def rec_metod(num):
    if num == 1:
        return num
    else:
        return rec_metod(num - 1) + num


try:
    num_m = int(input('Введите число: '))
    if rec_metod(num_m) == num_m * (num_m + 1) / 2:
        print(f'Равенство верно {rec_metod(num_m)}')
except ValueError:
    print('Неверный формат!')
