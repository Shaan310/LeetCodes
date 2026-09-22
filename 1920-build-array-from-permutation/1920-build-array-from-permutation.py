class Solution(object):
    def buildArray(self, nums):
        out=[]
        for i in range(len(nums)):
            out.append(nums[nums[i]])
        return out
        