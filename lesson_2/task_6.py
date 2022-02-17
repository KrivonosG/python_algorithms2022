""" Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр."""


def sum_numbers(number):
    sum = 0
    for i in number:
        sum += int(i)
    return sum


list_number = [j for j in input('Введите натуральные числа: ').split()]

number = 0
sum_max = 0
for j in list_number:
    if sum_numbers(j) > sum_max:
        number = j
        sum_max = sum_numbers(j)

print(f' Число {number} наибольшее по сумме цифр  - {sum_max}')
