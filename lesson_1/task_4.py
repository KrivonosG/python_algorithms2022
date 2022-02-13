"""Определить, является ли год, который ввел пользователем, високосным или не високосным."""


class Solution:
    def solved(self, year):
        return year % 4 == 0 or year % 100 == 0 or year % 400 == 0


s = Solution()
print(s.solved(2020))

