class Solution(object):
    def checkDivisibility(self, n):
        c=0
        p=1
        o=n
        while n>0:
            c+=(n%10)
            p*=(n%10)
            n//=10
        if o%(c+p)==0:
            return True
        return False

        