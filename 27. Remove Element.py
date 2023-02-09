class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = len(nums)
        while nums.count(val) > 0:
            print nums
            nums.remove(val)
            count -= 1
        return count
