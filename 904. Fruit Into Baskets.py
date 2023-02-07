class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        d = {}
        i = 0

        for j, val in enumerate(fruits):
            d[val] = d.get(val, 0) + 1 # get(key, value to return if key does not exist); increment curr val by 1
            if len(d) > 2: # if dict has more than 2 types of fruits
                d[fruits[i]] -= 1 # reduce freq of first picked fruit
                if d[fruits[i]] == 0: # if first fruit is gone
                    del d[fruits[i]] # get rid of first fruit
                i += 1               # increse i to next val
        return j - i + 1
