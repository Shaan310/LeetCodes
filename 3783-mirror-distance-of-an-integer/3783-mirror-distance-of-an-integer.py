class Solution(object):
    def mirrorDistance(self, n):
        l=str(n)[::-1]
        return abs(n-int(l))