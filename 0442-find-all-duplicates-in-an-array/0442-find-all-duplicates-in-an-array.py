class Solution(object):
    def findDuplicates(self, nums):
        s={}
        c=[]
        n=len(nums)
        for i in range(n):
            if nums[i] in s:
                c.append(nums[i])
            else:
                s[nums[i]]=i
        return c

        