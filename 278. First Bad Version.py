# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n
        while low <= high:
            mid = (high + low) / 2
            if isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid) == True and isBadVersion(mid - 1) == True:
                high = mid - 1
            else:
                low = mid + 1
