""" https://leetcode.com/problems/reverse-string/ """


#class Solution:
 #   def reverseString(self, s: List[str]) -> None:
 #       """
  #      Do not return anything, modify s in-place instead.
 #       """
 #       for i in range(len(s) // 2):
 #           s[i], s[-(i+1)] = s[-(i+1)], s[i]


class Solution:
    def __init__(self):
        self.i = 0

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if (self.i >= (len(s) // 2)):
            return

        s[self.i], s[-1 - self.i] = s[-1 - self.i], s[self.i]
        self.i += 1
        self.reverseString(s)

