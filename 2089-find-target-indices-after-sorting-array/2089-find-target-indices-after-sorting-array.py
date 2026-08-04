class Solution(object):
    def targetIndices(self, nums, target):
        c=[]
        l=0
        e=0
        for i in range(len(nums)):
            if nums[i]<target:
                l+=1
            if nums[i]==target:
                e+=1
        for i in range(e):
            c.append(l + i)
        return c
