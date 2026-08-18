class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        s={}
        n=len(nums)
        for i in range(n):
            if nums[i] in s:
                if i - s[nums[i]] <= k:
                    return True
            s[nums[i]] = i
        return False
        