class Solution(object):
    def countKDifference(self, nums, k):
        c=0
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if abs(nums[i]-nums[j])==k:
                    c+=1
                j+=1
        return c   