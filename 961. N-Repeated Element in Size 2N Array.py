class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        count = Counter(nums)
        return count.keys()[count.values().index(n)]
