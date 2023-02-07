class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trusts = [0] * (n + 1)
        trusted = [0] * (n + 1)

        for i, j in (trust):
            trusts[i] += 1
            trusted[j] += 1
        for i in range(1, n + 1):
            if trusts[i] == 0 and trusted[i] == n - 1:
                return i
        return -1
