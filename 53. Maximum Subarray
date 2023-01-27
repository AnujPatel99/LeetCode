class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max, global_max = 0, max(nums)       #Kadanes Algorithm
        for x in range(len(nums)):
            local_max = max(nums[x], nums[x] + local_max)
            if local_max > global_max:
                global_max = local_max
        return global_max
