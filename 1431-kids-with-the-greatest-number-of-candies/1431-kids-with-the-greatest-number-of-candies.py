class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        s=[]
        m=max(candies)
        for c in candies:
            if c+extraCandies>=m:
                s.append(True)
            else:
                s.append(False)
        return s

        