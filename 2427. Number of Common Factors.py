class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        r = min(a, b) # take smaller num to iterate through
        count = 0
        for i in range(1, r + 1): # start from1, r + 1 to include the number itself
            if a % i == 0 and b % i == 0:
                count += 1
        return count
