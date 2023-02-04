class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b  = int(a, 2), int(b, 2) #Convert binary input to decimal
        ans = a + b                 #Sum decimal a + b
        return bin(ans)[2:]         #Return the binary of the sum
