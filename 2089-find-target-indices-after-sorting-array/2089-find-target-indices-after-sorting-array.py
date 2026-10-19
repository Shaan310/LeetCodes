class Solution(object):
    def targetIndices(self, nums, target):
        c=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                c.append(i)
        return c
        