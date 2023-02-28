class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for c in t:
            if c in s:
                t = t.replace(c, "", 1)
                s = s.replace(c, "", 1)
        return t
