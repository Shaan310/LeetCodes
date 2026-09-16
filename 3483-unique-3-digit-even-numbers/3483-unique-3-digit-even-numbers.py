
class Solution(object):
    def totalNumbers(self, digits):
        i=100
        s={}
        c=0
        for di in digits:
            if di not in s:
                s[di]=1
            else:
                s[di]+=1
        
        while i<1000:
            check=True
            p=s.copy()
            for it in str(i):
                if int(it) in p and p[int(it)]>0:
                    p[int(it)]-=1
                else:
                    check=False
                    break
            if check and i%2==0:
                c+=1
            i+=1
        return c
