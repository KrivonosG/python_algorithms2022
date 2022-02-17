"""Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""


def sum_n_elem(a, numb, n_count, c_sum):
    if a == n_count:
        print(f'Элементов: {n_count}, а их Сумма: {c_sum}')
    elif a < n_count:
        return sum_n_elem(a + 1, numb / 2 * -1, n_count, c_sum + numb)


try:
    n_count_ = int(input("Введите сколько элементов: "))
    sum_n_elem(0, 1, n_count_, 0)
except ValueError:
    print('Вы ввели не число!!!')
