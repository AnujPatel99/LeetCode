class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: #All negative numbers are not palindromes. ex: -123 != 321-
            return False
        return str(x) == str(x)[::-1]
