class Solution(object):
    def digitFrequencyScore(self, n):
        c=[]
        while n>0:
            c.append(n%10)
            n=n//10
        s={}
        for chud in c:
            if chud in s:
                s[chud]+=1
            else:
                s[chud]=1
        p=0
        for key,value in s.items():
            p+=(key*value)
        return p