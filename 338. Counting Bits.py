class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = [0] * (n + 1)
        for x in range(n + 1):
            count = Counter(bin(x)[2:])
            countOne = count['1']
            arr[x] = countOne
        return arr
