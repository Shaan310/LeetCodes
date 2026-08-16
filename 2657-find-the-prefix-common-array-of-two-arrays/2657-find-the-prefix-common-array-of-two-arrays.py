class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n=len(A)
        a=set()
        b=set()
        c=[]

        
        for i in range(n):
            a.add(A[i])
            b.add(B[i])

            r=0
            for x in a:
                if x in b:
                    r+=1
            c.append(r)
        return c



        