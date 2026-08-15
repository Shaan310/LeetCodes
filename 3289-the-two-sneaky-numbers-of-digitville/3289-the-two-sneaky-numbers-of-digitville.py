class Solution(object):
    def getSneakyNumbers(self, nums):
        s=set()
        c=[]
        for n in nums:
            if n in s:
                c.append(n)
            else:
                s.add(n)
        return c


        