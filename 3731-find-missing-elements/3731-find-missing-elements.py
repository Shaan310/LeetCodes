class Solution(object):
    def findMissingElements(self, nums):
        l=min(nums)
        r=max(nums)
        c=[]
        for i in range(l,r+1):
            if i in nums:
                continue
            else:
                c.append(i)
        return c
        