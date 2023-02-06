class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        left, right = 0, n
        result = []
        for x in range(n):
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right += 1
        return result
