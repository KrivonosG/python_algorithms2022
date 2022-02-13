""" https://leetcode.com/problems/remove-duplicates-from-sorted-array/ """



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        index = 0
        k = 1
        for i in range(1, len(nums)):
            if (nums[i] != nums[index]):
                k += 1
                index += 1
                nums[index] = nums[i]
        return k

