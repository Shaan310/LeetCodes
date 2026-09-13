class Solution(object):
    def kthFactor(self, n, k):
        c=[]
        for i in range(1,n+1):
            if n%i==0:
                c.append(i)
        if k>len(c):
            return -1
        else:
            return c[k-1]
        