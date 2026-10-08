class Solution(object):
    def generate(self, numRows):
        c=[]
        for i in range(numRows):
            if(i==0):
                a=[1]
                c.append(a)
            else:
                s=[1]
                j=1
                while(i>j):
                    s.append(a[j-1] + a[j])
                    j+=1
                s.append(1)
                c.append(s)
                a=s
        return c 
        