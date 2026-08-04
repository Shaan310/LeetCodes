class Solution(object):
    def targetIndices(self, nums, target):
        c=[]
        nums.sort()
        for i in range(len(nums)):
            if target == nums[i]:
                c.append(i)
            else:
                continue
        return c
        