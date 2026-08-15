class Solution(object):
    def getSneakyNumbers(self, nums):
        s={}
        c=[]
        for n in nums:
            if n in s:
                c.append(n)
            else:
                s[n]=1
        return c


        