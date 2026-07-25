class Solution(object):
    def maxProduct(self, n):
        r = list(map(int,str(n)))
        r.sort()
        return r[-1]*r[-2]

        