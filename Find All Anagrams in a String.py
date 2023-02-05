class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        c1 = Counter(p)
        c2 = Counter(s[:len(p)])
        for i in range(len(s) - len(p)):
            if c1 == c2:
                result.append(i)
            c2[s[i]] -= 1       # decrese current indexed char freq by 1 [[a],b,c]
            if c2[s[i]] == 0:   # if that char freq is 0 after decreasing, del it: [b, c]
                del c2[s[i]]
            c2[s[i + len(p)]] += 1  # add the next char to the window [b, c, a]
        if c1 == c2: # check last window
            result.append(len(s) - len(p))
        return result
        
