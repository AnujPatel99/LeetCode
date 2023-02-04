class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        roman_dict = {}
        roman_dict.update({"I": 1})
        roman_dict.update({"V": 5})
        roman_dict.update({"X": 10})
        roman_dict.update({"L": 50})
        roman_dict.update({"C": 100})
        roman_dict.update({"D": 500})
        roman_dict.update({"M": 1000})
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        for c in range (len(s)):
            sum += roman_dict.get(s[c])
        return sum
