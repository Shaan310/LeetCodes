class Solution(object):
    def findDuplicate(self, nums):
        s={}
        for i in range(len(nums)):
            if nums[i] in s:
                return nums[i]
            else:
                s[nums[i]]=i
        