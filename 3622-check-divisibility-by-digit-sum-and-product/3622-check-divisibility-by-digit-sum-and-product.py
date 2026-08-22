class Solution(object):
    def checkDivisibility(self, n):
        c=0
        p=1
        for ni in str(n):
            c+=int(ni)
            p*=int(ni)
        if n%(c+p)==0:
            return True
        return False

        