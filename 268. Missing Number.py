class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_total = sum(range(0, n + 1))
        sum_nums = sum(nums)
        target = sum_total - sum_nums
        return target
