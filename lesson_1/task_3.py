"""Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
 и сколько между ними находится букв"""


class Solution:
    def solve(self, a, b):
        return (ord(a) - ord('a') + 1, ord(b) - ord('a') + 1, ord(b) - ord(a))


s = Solution()
print(s.solve('b', 'e'))
