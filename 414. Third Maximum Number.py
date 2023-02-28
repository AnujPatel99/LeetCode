class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return max(nums)
        for i in range(2):
            m = max(nums)
            nums = [i for i in nums if i != m]
        return max(nums)
