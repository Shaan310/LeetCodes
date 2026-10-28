class Solution(object):
    def isUgly(self, n):
        if n<=0:
            return False
        for u in [2,3,5]:
            while n%u==0:
                n//=u
        return n == 1
        