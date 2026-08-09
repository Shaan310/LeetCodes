class Solution(object):
    def alternatingSum(self, nums):
        c=0
        for i in range(len(nums)):
            if i % 2==0:
                c+=nums[i]
            else:
                c-=nums[i]
        return c

        