class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s = " ".join([str(c) for c in num])
        s = s.replace(" ", "")
        s = int(s) + k
        return [int(i) for i in str(s)]
