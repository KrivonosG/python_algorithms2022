""" https://leetcode.com/problems/move-zeroes/ """



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        lastNonZero = 0
        for i in range(0, len(nums)):
            if (nums[i] != 0):
                tmp = nums[i]
                nums[i] = nums[lastNonZero]
                nums[lastNonZero] = tmp
                lastNonZero += 1