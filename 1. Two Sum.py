class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for x, y in enumerate(nums):
            r = target - y
            if r in hash_map:
                return hash_map[r], x
            hash_map[y] = x
            
