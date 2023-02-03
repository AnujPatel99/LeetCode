def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_of_zeros = nums.count(0)
        if num_of_zeros == 0:
            return nums
            
        for nums_of_zeros in nums:
            nums.remove(0)
            nums.append(0)
        return nums
