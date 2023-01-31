class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newList = nums1 + nums2
        newList.sort()
        if len(newList) % 2 != 0:
            return newList[len(newList) / 2]
        else:
            return float(newList[len(newList) / 2] + newList[(len(newList) / 2) - 1]) / 2
