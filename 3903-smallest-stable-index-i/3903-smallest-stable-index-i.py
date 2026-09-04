class Solution(object):
    def firstStableIndex(self, nums, k):
        for i in range(len(nums)):
            a=max(nums[:i+1])
            b=min(nums[i:])
            if a-b<= k:
                return i
        return -1

        