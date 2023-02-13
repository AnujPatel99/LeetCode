class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low == high:
            return 1 if low % 2 != 0 else 0
        if (high - low + 1) % 2 == 0:
            return (high - low + 1) / 2
        return ((high - low) / 2) + 1 if low % 2 != 0 and high % 2 != 0 else (high - low) / 2
