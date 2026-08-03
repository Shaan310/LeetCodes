class Solution(object):
    def checkPowersOfThree(self, n):
        c=0
        m=0
        while c<n:
            c=3**m
            m+=1
        p=m-1
        for i in range(p,-1,-1):
            if n-(3**i) >= 0:
                n=n-(3**i)
            else:
                continue
        return n==0

        

        