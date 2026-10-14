class Solution(object):
    def isHappy(self, n):
        p=set()
        while True:
            r=0
            for ni in str(n):
                r+=(int(ni))**2
            if r==1:
                return True
            if r not in p:
                p.add(r)
                n=r
            else:
                return False

        