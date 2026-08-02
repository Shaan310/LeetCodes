class Solution(object):
    def selfDividingNumbers(self, left, right):
        c=[]
        while left<=right:
            j=0
            n = [int(d) for d in str(left)]
            l=len(n)
            for i in range(l):
                if n[i]==0:
                    break
                if left%n[i]==0:
                    j+=1
                else:
                    break
            if j==l:
                c.append(left)
            left+=1
        return c