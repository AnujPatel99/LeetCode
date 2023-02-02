class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        evenSum = sum(x for x in nums if x % 2 == 0)
        arr = []
        for val, i in queries:
            if nums[i] % 2 == 0:
                evenSum -= nums[i]
            nums[i] = nums[i] + val
            if nums[i] % 2 == 0:
                evenSum += nums[i]
            arr.append(evenSum)
        return arr
