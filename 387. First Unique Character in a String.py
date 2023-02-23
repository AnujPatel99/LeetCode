class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        return -1
