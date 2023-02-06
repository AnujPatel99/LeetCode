class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = lastIndex = 1
        lastVal = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == lastVal:
                continue
            elif nums[i] != lastVal:
                nums[lastIndex] = nums[i]
                lastVal = nums[i]
                lastIndex += 1
                count += 1
        return count
