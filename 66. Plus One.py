class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = [str(c) for c in digits]
        s = ''.join(s)
        num = int(s) + 1
        return [int(x) for x in str(num)]
