"""Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)"""

def append_to_string(num, result):
    if num == 0 and result == '':
        return result
    else:
        return result + str(num)


def rev_num_h(n, result):
    res_n, num = divmod(n, 10)
    result = append_to_string(num, result)
    if res_n == 0:
        return result
    else:
        return rev_num_h(res_n, result)


def rev_num(n):
    return rev_num_h(n, '')


numb = int(input('Введите число чтобы его перевернуть: '))


print(rev_num(numb))
print(rev_num(345))
print(rev_num(340))


