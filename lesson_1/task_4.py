"""Определить, является ли год, который ввел пользователем, високосным или не високосным."""


class Solution:
    def solved(self, year):
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


s = Solution()
print(s.solved(1900))