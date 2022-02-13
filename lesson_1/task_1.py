# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


# num = int(input('Введите трёхзначное число: '))
# num1 = num % 10
# num2 = (num // 10) % 10
# num3 = num // 100
# print(f'Сумма цифр трехзначного числа равна: {num1 + num2 + num3}')
# print(f'Произведение цифр трехзначного числа равна: {num1 * num2 * num3}')


class Solution:
    def solve(self, num):
        num1 = num % 10
        num2 = (num // 10) % 10
        num3 = num // 100
        return (num1 + num2 + num3, num1 * num2 * num3)


class Test:
    def __init__(self):
        self.data = [(123, (6, 6)), (321, (6, 6))]
        self.t = Solution()

    def run_test(self):
        for k in self.data:
            if (self.t.solve(k[0]) != k[1]):
                print("Test failed!")
                return

    print("All tests passed!")


t = Test()
t.run_test()
