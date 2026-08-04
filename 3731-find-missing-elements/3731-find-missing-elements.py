class Solution(object):
    def findMissingElements(self, nums):
        l=min(nums)
        r=max(nums)
        c=[]
        s=set(nums)
        for i in range(l,r+1):
            if i in s:
                continue
            else:
                c.append(i)
        return c
        