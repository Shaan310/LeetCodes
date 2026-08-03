class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        else:
            while n>1:
                if n%4!=0:
                    return False
                n/=4
        return n==1
        